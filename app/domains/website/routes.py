from flask import Flask, render_template, request, redirect

from app.domains.pokemons.actions import get as get_all_pokemons
from app.domains.trainers.actions import get as get_all_trainers

app = Flask(__name__)
login = []


@app.route('/')
def index():
    return render_template('menu_escolha.html', login=None)


@app.route('/login')
def login_admin():
    admin_all = get_all_trainers()
    username = request.args['username']
    passwd = request.args['password']

    for admin in admin_all:
        if str(username).lower() == str(admin.username).lower() \
                or str(username).lower() == str(admin.email).lower():
            if passwd == str(admin.password).lower():
                login.append(username)
                login.append(passwd)
                return render_template('menu_admin.html')
    return render_template('login.html')


@app.route('/menuadmin')
def menu_admin():
    if login:
        return render_template('menu_admin.html')
    else:
        return render_template('login.html')


@app.route('/menuadminpokemon')
def menu_admin_pokemon():
    if not login:
        return redirect('/menuadmin')
    lista_dados = get_all_pokemons()
    lista = []
    for dados in lista_dados:
        lista.append(dados.list())

    return render_template('menu_admin_pokemon.html', lista=lista)


@app.route('/menuadmin/adicionarpokemon')
def adicionar_pokemon():
    if not login:
        return redirect('/menuadminpokemon')
    return render_template('pokemon_admin_dados.html')


@app.route('/menuadminpokemon/editarpokemon')
def editar_pokemon():
    if not login:
        return redirect('/menuadminpokemon')
    id = request.args['id']
    print(id)
    return render_template('pokemon_admin_dados.html')


@app.route('/sair')
def sair_admin():
    # busca a variavel global para modificar
    global login
    login = []
    return redirect('/')


@app.route('/menupokemon')
def listar_todos_pokemon():
    lista_dados = get_all_pokemons()
    lista = []
    for dados in lista_dados:
        lista.append(dados.list())

    return render_template('Listar_todos_pokemons.html', lista=lista)


app.run(debug=True, port=80)
