from flask import Flask, render_template, request, redirect, url_for
from django.conf import settings
from .models import Produto
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = settings.MEDIA_ROOT

# Listar Produtos
@app.route('/')
def listar_produtos():
    produtos = Produto.objects.all()
    return render_template('listar.html', produtos=produtos)

# Criar Produto
@app.route('/criar', methods=['GET', 'POST'])
def criar_produto():
    if request.method == 'POST':
        try:
            foto = request.files.get('foto')
            dados = request.form
            
            produto = Produto(
                nome=dados['nome'],
                preco=dados['preco'],
                tamanho=dados.get('tamanho'),
                cor=dados.get('cor'),
                quantidade=dados['quantidade']
            )

            if foto:
                foto_path = os.path.join('produtos', foto.filename)
                produto.foto.save(foto_path, foto)

            produto.save()
            return redirect('/')
        
        except Exception as e:
            return str(e), 400
    
    return render_template('criar.html')

# Editar Produto
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = Produto.objects.get(id=id)
    
    if request.method == 'POST':
        try:
            foto = request.files.get('foto')
            dados = request.form

            produto.nome = dados['nome']
            produto.preco = dados['preco']
            produto.tamanho = dados.get('tamanho')
            produto.cor = dados.get('cor')
            produto.quantidade = dados['quantidade']

            if foto:
                foto_path = os.path.join('produtos', foto.filename)
                produto.foto.save(foto_path, foto)

            produto.save()
            return redirect('/')
        
        except Exception as e:
            return str(e), 400
    
    return render_template('editar.html', produto=produto)

# Deletar Produto
@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_produto(id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('/')

# Servir arquivos de mídia
@app.route('/media/<path:filename>')
def media_file(filename):
    return send_from_directory(settings.MEDIA_ROOT, filename)