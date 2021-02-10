from flask import Blueprint, jsonify, request
from typing import Tuple, Any, Dict

from app.domains.services.actions import login_admin

app_services = Blueprint('app.services', __name__)


@app_services.route('/login', methods=['POST'])
def login() -> Tuple[Any, int]:
    user_login: Dict = request.get_json()
    bool_login = login_admin(user_login)
    print(user_login)
    print(bool_login)

    return jsonify({'access_token': bool_login}), 201
