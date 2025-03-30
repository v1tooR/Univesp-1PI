import os
import django
import sys
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from decimal import Decimal
from config import TEMPLATE_DIR, MEDIA_PRODUTOS_DIR, FLASK_SECRET_KEY, FLASK_DEBUG

# Inicializar Django antes de importar modelos
os.environ['DJANGO_SETTINGS_MODULE'] = 'manage'
django.setup()

# Agora podemos importar modelos Django
from app.models import Produto

# Inicialização do Flask
app = Flask(__name__, template_folder=TEMPLATE_DIR)
app.secret_key = FLASK_SECRET_KEY
app.config['DEBUG'] = FLASK_DEBUG

# Função auxiliar para salvar imagens
def salvar_imagem(arquivo):
    """Salva a imagem enviada e retorna o caminho relativo."""
    if not arquivo or arquivo.filename == '':
        return None
        
    filename = secure_filename(arquivo.filename)
    filepath = os.path.join(MEDIA_PRODUTOS_DIR, filename)
    arquivo.save(filepath)
    
    # Retorna o caminho relativo para salvar no banco
    return f'produtos/{filename}'

# Rota para servir arquivos de mídia
@app.route('/media/<path:filename>')
def media_files(filename):
    """Serve os arquivos de mídia."""
    media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')
    return send_from_directory(media_dir, filename)

# Rotas principais da aplicação
@app.route('/')
def index():
    """Página inicial - Lista todos os produtos."""
    try:
        produtos = Produto.objects.all()
        return render_template('index.html', produtos=produtos)
    except Exception as e:
        print(f"Erro ao listar produtos: {e}")
        return render_template('index.html', produtos=[], erro=str(e))

@app.route('/produto/adicionar', methods=['GET', 'POST'])
def adicionar_produto():
    """Rota para adicionar um novo produto."""
    if request.method == 'POST':
        try:
            # Obtém dados do formulário
            nome = request.form.get('nome')
            preco = Decimal(request.form.get('preco').replace(',', '.'))
            tamanho = request.form.get('tamanho') or None
            cor = request.form.get('cor') or None
            quantidade = int(request.form.get('quantidade'))
            
            # Processar upload de imagem
            imagem = request.files.get('foto')
            caminho_imagem = salvar_imagem(imagem) if imagem and imagem.filename else None
            
            # Criar o produto
            produto = Produto(
                nome=nome,
                preco=preco,
                tamanho=tamanho,
                cor=cor,
                quantidade=quantidade,
                foto=caminho_imagem
            )
            produto.save()
            
            print(f"Produto '{nome}' adicionado com sucesso!")
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Erro ao adicionar produto: {e}")
            return render_template('adicionar_produto.html', erro=str(e))
    
    return render_template('adicionar_produto.html')

@app.route('/produto/editar/<int:produto_id>', methods=['GET', 'POST'])
def editar_produto(produto_id):
    """Rota para editar um produto existente."""
    try:
        produto = Produto.objects.get(id=produto_id)
        
        if request.method == 'POST':
            try:
                # Atualiza os dados do produto
                produto.nome = request.form.get('nome')
                produto.preco = Decimal(request.form.get('preco').replace(',', '.'))
                produto.tamanho = request.form.get('tamanho') or None
                produto.cor = request.form.get('cor') or None
                produto.quantidade = int(request.form.get('quantidade'))
                
                # Processar upload de nova imagem, se houver
                imagem = request.files.get('foto')
                if imagem and imagem.filename != '':
                    caminho_imagem = salvar_imagem(imagem)
                    produto.foto = caminho_imagem
                
                produto.save()
                print(f"Produto '{produto.nome}' atualizado com sucesso!")
                return redirect(url_for('index'))
            except Exception as e:
                print(f"Erro ao atualizar produto: {e}")
                return render_template('editar_produto.html', produto=produto, erro=str(e))
        
        return render_template('editar_produto.html', produto=produto)
    except Produto.DoesNotExist:
        print(f"Produto com ID {produto_id} não encontrado")
        return redirect(url_for('index'))

@app.route('/produto/excluir/<int:produto_id>')
def excluir_produto(produto_id):
    """Rota para excluir um produto."""
    try:
        produto = Produto.objects.get(id=produto_id)
        nome = produto.nome
        produto.delete()
        print(f"Produto '{nome}' excluído com sucesso!")
    except Produto.DoesNotExist:
        print(f"Produto com ID {produto_id} não encontrado")
    except Exception as e:
        print(f"Erro ao excluir produto: {e}")
    
    return redirect(url_for('index'))

# Inicialização da aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)