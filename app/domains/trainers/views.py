from flask import Blueprint, request, jsonify
from app.domains.trainers.actions import create as create_trainer, \
                                         get_by_id as get_trainer_by_id, \
                                         get as get_trainers, \
                                         update as update_trainer, \
                                         delete as delete_trainer

app_trainers = Blueprint('app.trainers', __name__)


@app_trainers.route('/trainers', methods=['POST'])
def post():
    payload = request.get_json()
    trainer = create_trainer(payload)
    return jsonify(trainer.serialize()), 201


@app_trainers.route('/trainers/<id>', methods=['GET'])
def get_by_id(id : str):
    trainer = get_trainer_by_id(id)
    return jsonify(trainer.serialize()), 200


@app_trainers.route('/trainers', methods=['GET'])
def get() -> tuple:
    return jsonify([trainer.serialize() for trainer in get_trainers()]), 200


@app_trainers.route('/trainers/<id>', methods=['PUT'])
def put(id: str):
    payload = request.get_json()
    trainer = update_trainer(id, payload)
    return jsonify(trainer.serialize()), 200


@app_trainers.route('/trainers/<id>', methods=['DELETE'])
def delete(id: str) -> tuple:
    delete_trainer(id)
    return jsonify({}), 204
