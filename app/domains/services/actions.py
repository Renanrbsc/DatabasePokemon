from typing import Dict

from app.domains.trainers.actions import get as get_all_trainers


def login_admin(admin: Dict) -> bool:
    admin_all = get_all_trainers()
    username = admin.get('username')
    passwd = admin.get('password')

    for index in admin_all:
        if str(username).lower() == str(index.name).lower() \
                or str(username).lower() == str(index.name).lower():
            if passwd == str(index.lastname).lower():
                return True
    return False
