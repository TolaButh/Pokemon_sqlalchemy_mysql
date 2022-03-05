from turtle import title
from pokemons import app, db
from pokemons.models import Pokemon
from flask import jsonify, render_template, redirect, request, url_for

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/pokemons')
def pokemons():
    pokemons = Pokemon.query.all()
    return render_template('pokemons.html', title='Show all Pokemons', pokemons=pokemons)

@app.route('/pokemon/add', methods=['GET', 'POST'])
def add_pokemon():
    if request.method == 'POST':
        poke_name = request.form.get('poke_name')
        poke_type = request.form['poke_type']
        category = request.form.get('category')

        pokemon = Pokemon(poke_name=poke_name, poke_type=poke_type, category=category)
        db.session.add(pokemon)
        db.session.commit()

        return redirect(url_for('pokemons'))

    return render_template('add_pokemon.html', title='New Pokemon')

@app.route('/pokemon/search', methods=['POST'])
def search_pokemon():
    if request.method == 'POST':
        poke_name = request.form.get('poke_name')
        pokemons = Pokemon.query.filter(Pokemon.poke_name.like('%{}%'.format(poke_name))).all()

        return render_template('pokemons.html', title='Search Pokemon', pokemons=pokemons)

@app.route('/pokemons/ajax')
def pokemons_with_ajax():
    return render_template('pokemons_ajax.html', title='Pokemon with Ajax')

@app.route('/search_pokemon_ajax', methods=['GET','POST'])
def search_pokemon_ajax():
    if request.method == 'POST':
        poke_name = request.form.get('query')
        # print(poke_name)
        pokemons = Pokemon.query.filter(Pokemon.poke_name.like('%{}%'.format(poke_name))).all()

        return jsonify({
            'htmlpokemons': render_template('pokemons_list.html', pokemons=pokemons)
        })

@app.route('/pokemons/api')
def pokemons_api():
    pokemons = Pokemon.query.all()
    list_pokemons = [ pokemon.as_dict() for pokemon in pokemons ]
    return jsonify(list_pokemons)
        
        