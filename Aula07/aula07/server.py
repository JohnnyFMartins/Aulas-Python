from flask import Flask, jsonify, request, render_template

# Criando apicação em Flask!
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# GET -> Buscar algo
@app.route("/helloword", methods=["GET"])
def helloworld():
    return jsonify({"message": "Ola Mundo"})

# Lista de tarefas
tarefas = [
    {"id": 1, "titulo": "Estudar Python", "feita": False},
    {"id": 2, "titulo": "Estudar Saas", "feita": False},
    {"id": 3, "titulo": "Estudar AWS", "feita": False},
]

# GET - Buscar Informações
@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)

#POST - Criar uma nova tarefa
"""
JavaScript (Front) -> fetch
ReactJS (front) - axios
Insomnia (Aplicativo) -> Simular um Front 
Postman (Aplicativo) -> Simular um Front

Back-End -> Modelo de API -> FULL REST
Full-Stack - Aquitetura MVC (Model, View, Controller)
"""
@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa = request.json # pegar a informação do body
    nova_tarefa['id'] = len(tarefas) + 1 # adicionando novo id
    tarefas.append(nova_tarefa) # adicionando nova tarefa na lista
    return jsonify(nova_tarefa), 201 # 201 -> created -> criado com sucesso

@app.route("/tarefas", methods=["GET"])
def get_tarefas():
    return jsonify(tarefas)

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)