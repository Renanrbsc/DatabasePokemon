from typing import Dict, List
from database.repository import commit, save
from app.domains.users.models import User
from utils.convert_txt import convert_txt_for_json


def create(data: Dict[str, str]) -> User:
    user: User = User(
                      id=data['id'],
                      username=data['username'],
                      password=data['password'],
                      email=data['email']
                      )
    return save(user)


def get() -> List[User]:
    return User.query.all()


def get_by_id(id: str) -> User:
    return User.query.get(id)


def get_by_username(username: str) -> User:
    return User.query.filter_by(username=username).first()


def update(id: str, data: Dict[str, str]) -> User:
    user: User = get_by_id(id)
    user.username: str = data.get('username')
    user.password: str = data.get('password')
    user.email: str = data.get('email')
    commit()
    return user


def delete(id: str) -> User:
    user: User = get_by_id(id)
    return "Work in progress!"


def import_txt(text: str) -> List[User]:
    user: User = User()
    list_models: List[User] = list()

    dictionary_list = convert_txt_for_json(text, user.serialize())
    for data in dictionary_list:
        model: User = User(
                           id=data['id'],
                           username=data['username'],
                           password=data['password'],
                           email=data['email']
                           )
        list_models.append(model)

    for model in list_models:
        save(model)

    return list_models
