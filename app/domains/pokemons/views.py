from flask import Blueprint, request, jsonify
from app.domains.pokemons.actions import create as create_pokemon, \
                                                   get_by_name as get_pokemon_by_name, \
                                                   get_by_id as get_pokemon_by_id, \
                                                   get as get_pokemons, \
                                                   update as update_pokemon, \
                                                   delete as delete_pokemon, \
                                                   import_txt as import_txt_pokemon

app_pokemons = Blueprint('app.pokemons', __name__)


@app_pokemons.route('/pokemons', methods=['POST'])
def post():
    payload = request.get_json()
    pokemon = create_pokemon(payload)
    return jsonify(pokemon.serialize()), 201


@app_pokemons.route('/pokemons/id/<id>', methods=['GET'])
def get_by_id(id: str):
    pokemon = get_pokemon_by_id(id)
    return jsonify(pokemon.serialize()), 200


@app_pokemons.route('/pokemons/name/<name>', methods=['GET'])
def get_by_name(name: str):
    pokemon = get_pokemon_by_name(name)
    return jsonify(pokemon.serialize()), 200


@app_pokemons.route('/pokemons', methods=['GET'])
def get() -> tuple:
    return jsonify([pokemon.serialize() for pokemon in get_pokemons()]), 200


@app_pokemons.route('/pokemons/<id>', methods=['PUT'])
def put(id: str):
    payload = request.get_json()
    pokemon = update_pokemon(id, payload)
    return jsonify(pokemon.serialize()), 200


@app_pokemons.route('/pokemons/<id>', methods=['DELETE'])
def delete(id: str) -> tuple:
    delete_pokemon(id)
    return jsonify({}), 204


@app_pokemons.route('/pokemons:import_txt_pokemons', methods=['POST'])
def post_txt_pokemons():
    content = request.files['file']
    text = content.stream.read().decode("utf-8")

    list_data = import_txt_pokemon(text)
    return jsonify([pokemon.serialize() for pokemon in list_data]), 201
