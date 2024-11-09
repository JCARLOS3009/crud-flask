from flask import Flask, render_template, url_for
from crud import app_crud

app = Flask(__name__)
app.register_blueprint(app_crud)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/main')
def index():
    return render_template('index.html')
# Rota para criar registro de pessoa
@app_crud.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        # Obtendo os dados do formulário enviados pelo método POST
        username = request.form['username']
        email = request.form['email']

        # Conectando ao banco de dados e inserindo o novo usuário
        conexao = sqlite3.connect('dapodik.db')
        cursor = conexao.cursor()

        try:
            # Criando a tabela se ela não existir
            cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT)')
            # Inserindo os dados do novo usuário
            cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
            conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao acessar o banco de dados: {e}")
            return "Erro ao criar usuário."
        finally:
            # Fechando a conexão com o banco de dados
            cursor.close()
            conexao.close()

        # Redirecionando para a página principal após a criação
        return redirect(url_for('app_crud.index'))


app.run(host='0.0.0.0', port=81)
