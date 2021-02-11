from typing import Dict, List
from backend.database.repository import commit, save
from backend.app.domains.trainers.models import Trainer


def create(data: Dict[str, str]) -> Trainer:
    trainer: Trainer = Trainer(
                               id=data['id'],
                               name=data['name'],
                               lastname=data['lastname'],
                               age=data['age'], 
                               city=data['city']
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