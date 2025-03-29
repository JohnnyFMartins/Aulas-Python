from flask import Blueprint, current_app, redirect, render_template, request, url_for
from models.produto import Produto


produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/')
def index():
    produtos = Produto.listar(current_app.mysql)
    return render_template('index.html', produtos=produtos)

@produto_bp.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':
        # deseja criar um produto
        nome = request.form['nome']
        preco = request.form['preco']
        Produto.salvar(Produto(None, nome, preco), current_app.mysql) # salvar no banco
        return redirect(url_for('produto.index'))
    return render_template('criar.html') # pagina de form

# http://localhost:5000/produto/editar/321321
@produto_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        Produto.atualizar(Produto(id, nome, preco), current_app.mysql)
        return redirect(url_for('produto.index')) # retornar para a pagina inicial
    prod = Produto.buscar_por_id(current_app.mysql, id) # buscar produto para atualizar
    return render_template('editar.html', produto=prod) # retornar a pagina editar

@produto_bp.route('/deletar/<int:id>')
def deletar(id):
    Produto.deletar(current_app.mysql, id)
    return redirect(url_for('produto.index'))