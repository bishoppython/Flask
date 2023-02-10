from flask import Flask, render_template, request, redirect, session, flash


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#Tornando as Variaveis de uso Global
jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('GoW', 'Rack n Slash', 'PS4')
jogo3 = Jogo('FIFA23', 'Esporte', 'PC')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)  #Faz referencia ao próprio arquivo
app.secret_key = 'alura'

@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console) # Cria-se uma instancia
    lista.append(jogo)

    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' Logado com Sucesso!')
        return redirect('/')
    else:
        flash('Usuário Não Logado!')
        return redirect('/login')

app.run(debug=True)