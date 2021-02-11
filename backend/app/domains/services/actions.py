from typing import Dict


def login_admin(admin: Dict) -> bool:
    admin_all = [{"username": "renan", "email": "", "password": "12345"}]
    username = admin.get('username')
    passwd = admin.get('password')

    for index in admin_all:
        if str(username).lower() == str(index['username']).lower() \
                or str(username).lower() == str(index['email']).lower():
            if passwd == str(index['password']).lower():
                return True
    return False
