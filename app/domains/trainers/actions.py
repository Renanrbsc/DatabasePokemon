from typing import Dict, List
from database.repository import commit, save
from app.domains.trainers.models import Trainer
from app.domains.pokemons.actions import get_by_name as get_pokemon_by_name


def create(data: Dict[str, str]) -> Trainer:
    trainer: Trainer = Trainer(
                               id=data['id'],
                               name=data['name'],
                               lastname=data['lastname'],
                               age=data['age'], 
                               city=data['city'],
                               pokemons=[get_pokemon_by_name(pokemon) for pokemon in data['pokemons']],
                               user_id=data['user_id']
                               )
    return save(trainer)


def get() -> List[Trainer]:
    return Trainer.query.all()


def get_by_id(id: str) -> Trainer:
    return Trainer.query.get(id)


def get_by_name(name: str) -> Trainer:
    return Trainer.query.filter_by(name=name).first()


def update(id: str, data: Dict[str, str]) -> Trainer:
    trainer: Trainer = get_by_id(id)
    trainer.name: str = data.get('name')
    trainer.lastname: str = data.get('lastname')
    trainer.age: str = data.get('age')
    trainer.city: str = data.get('city')
    commit()
    return trainer


def delete(id: str) -> Trainer:
    trainer: Trainer = get_by_id(id)
    return "Work in progress!"


def import_txt(text: str) -> List[Trainer]:
    trainer: Trainer = Trainer()
    list_models: List[Trainer] = list()

    dictionary_list = convert_txt_for_json(text, trainer.serialize())
    for data in dictionary_list:
        model: Trainer = Trainer(
                                 id=data['id'],
                                 name=data['name'],
                                 lastname=data['lastname'],
                                 age=data['age'], 
                                 city=data['city'],
                                 pokemons=[get_pokemon_by_name(pokemon) for pokemon in data['pokemons']],
                                 user_id=data['user_id']
                                 )
        list_models.append(model)

    for model in list_models:
        save(model)

    return list_models