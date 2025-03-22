from flask import Flask
from flask_mysqldb import MySQL # biblioteca mysql flask
import config
from controllers.produto_controller import produto_bp


app = Flask(__name__) # Intanciar o flask
app.config.from_object(config) # Configurando variaveis

mysql = MySQL(app)

# passa a conexao para os controllers
app.mysql = mysql

# registrar o controller
app.register_blueprint(produto_bp)

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)