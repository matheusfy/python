import operations

class App():
    
    def __init__(self) -> None:
        self.db_connection = operations.DB_CONNECTION()
    
    
    def run():
        # run application
        while True:
            pass
            
        return False


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