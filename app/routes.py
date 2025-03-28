from flask import Flask, render_template, request, redirect, send_from_directory
from django.conf import settings
from .models import Produto
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = settings.MEDIA_ROOT

# Rotas CRUD
@app.route('/')
def listar_produtos():
    produtos = Produto.objects.all()
    return render_template('listar.html', produtos=produtos)

@app.route('/criar', methods=['GET', 'POST'])
def criar_produto():
    if request.method == 'POST':
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

    return render_template('criar.html')

# ... (Rotas editar, deletar e comprar do código anterior)