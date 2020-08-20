from typing import Dict, List
from database.repository import commit, save
from app.domains.pokemons.models import Pokemon
from utils.convert_txt import convert_txt_for_json


def create(data: Dict[str, str]) -> Pokemon:
    pokemon: Pokemon = Pokemon(
                               id=data['id'],
                               name=data['name'],
                               type=data['type'],
                               height=data['height'], 
                               weight=data['weight'], 
                               category=data['category'],
                               ability=data['ability'], 
                               ability_two=data['ability_two'],
                               weakness=data['weakness'], 
                               weakness_two=data['weakness_two'], 
                               description=data['description']
                               )
    return save(pokemon)


def get() -> List[Pokemon]:
    return Pokemon.query.all()


def get_by_id(id: str) -> Pokemon:
    return Pokemon.query.get(id)


def get_by_name(name: str) -> Pokemon:
    return Pokemon.query.filter_by(name=name).first()


def update(id: str, data: Dict[str, str]) -> Pokemon:
    pokemon: Pokemon = get_by_id(id)
    pokemon.name: str = data.get('name')
    pokemon.type: str = data.get('type')
    pokemon.height: str = data.get('height')
    pokemon.weight: str = data.get('weight')
    pokemon.category: str = data.get('category')
    pokemon.ability: str = data.get('ability')
    pokemon.ability_two: str = data.get('ability_two')
    pokemon.weakness: str = data.get('weakness')
    pokemon.weakness_two: str = data.get('weakness_two')
    pokemon.description: str = data.get('description')
    commit()
    return pokemon


def delete(id: str) -> Pokemon:
    pokemon: Pokemon = get_by_id(id)
    return "Work in progress!"


def import_txt(text: str) -> List[Pokemon]:
    pokemon: Pokemon = Pokemon()
    list_models: List[Pokemon] = list()

    dictionary_list = convert_txt_for_json(text, pokemon.serialize())
    for data in dictionary_list:
        model: Pokemon = Pokemon(
                                 id=data['id'],
                                 name=data['name'],
                                 type=data['type'],
                                 height=data['height'],
                                 weight=data['weight'],
                                 category=data['category'],
                                 ability=data['ability'],
                                 ability_two=data['ability_two'],
                                 weakness=data['weakness'],
                                 weakness_two=data['weakness_two'],
                                 description=data['description']
                                 )
        list_models.append(model)

    for model in list_models:
        save(model)

    return list_models
