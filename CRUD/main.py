import json
from flask import Flask, request
from Repository.UsuarioRepository import UsuarioRepository
from Entities.Usuario import Usuario
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Vazio'

@app.route('/add_user', methods=['POST'])
def add_user():
    content = request.get_json(silent=True)
    
    try:
        if request.method == 'POST':
            user = Usuario()
            
            user.nome = content['nome']
            user.idade = content['idade']
            user.endereco = content['endereco']
            user.senha = content['senha']
            user.cpf = content['cpf']

            if not UsuarioRepository().add_user(user=user):
                return 'falha na insercao do usuario'

    except(Exception) as error:
        return f'Erro ao tentar inserir usuario {error}'

    return 'inserido com sucesso'

@app.route('/get_allusers', methods=['GET'])
def Get_AllUsers():

    lst_users = []
    repo_User = UsuarioRepository()
    for user in repo_User.get_users():
      lst_users.append(user._as_dict()) 
    try:
        return json.dumps(lst_users)
    except (Exception) as error:
        print("erro json: " + error)
        return []


if __name__ == '__main__':
    app.run(debug=True)