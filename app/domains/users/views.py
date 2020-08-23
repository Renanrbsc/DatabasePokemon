from flask import Blueprint, request, jsonify
from app.domains.users.actions import create as create_user, \
                                                get_by_username as get_user_by_username, \
                                                get_by_id as get_user_by_id, \
                                                get as get_users, \
                                                update as update_user, \
                                                delete as delete_user, \
                                                import_txt as import_txt_users

app_users = Blueprint('app.users', __name__)


@app_users.route('/users', methods=['POST'])
def post():
    payload = request.get_json()
    user = create_user(payload)
    return jsonify(user.serialize()), 201


@app_users.route('/users/id/<id>', methods=['GET'])
def get_by_id(id: str):
    user = get_user_by_id(id)
    return jsonify(user.serialize()), 200


@app_users.route('/users/username/<username>', methods=['GET'])
def get_by_username(username: str):
    user = get_user_by_username(username)
    return jsonify(user.serialize()), 200


@app_users.route('/users', methods=['GET'])
def get() -> tuple:
    return jsonify([user.serialize() for user in get_users()]), 200


@app_users.route('/users/<id>', methods=['PUT'])
def put(id: str):
    payload = request.get_json()
    user = update_user(id, payload)
    return jsonify(user.serialize()), 200


@app_users.route('/users/<id>', methods=['DELETE'])
def delete(id: str) -> tuple:
    delete_user(id)
    return jsonify({}), 204


@app_users.route('/users:import_txt_users', methods=['POST'])
def post_txt_users():
    content = request.files['file']
    text = content.stream.read().decode("utf-8")

    list_data = import_txt_users(text)
    return jsonify([user.serialize() for user in list_data]), 201
