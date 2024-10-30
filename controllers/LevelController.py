from flask import jsonify, request
from models.LevelModel import Level
from config import db

def get_levels():
    levels = Level.query.all()
    return jsonify([level.to_dict() for level in levels])

def get_level(id_level):
    level = Level.query.get(id_level)
    if not level:
        return jsonify({'error': 'Level not found'}), 404
    return jsonify(level.to_dict())

def add_level():
    new_level_data = request.get_json()
    new_level = Level(
        name=new_level_data['name']
    )
    db.session.add(new_level)
    db.session.commit()
    return jsonify({'message': 'Level added successfully!', 'level': new_level.to_dict()}), 201

def update_level(id_level):
    level = Level.query.get(id_level)
    if not level:
        return jsonify({'error': 'Level not found'}), 404
    updated_data = request.get_json()
    level.name = updated_data.get('name', level.name)
    db.session.commit()
    return jsonify({'message': 'Level updated successfully!', 'level': level.to_dict()})

def delete_level(id):
    level = Level.query.get(id)
    if not level:
        return jsonify({'error': 'Level not found'}), 404
    db.session.delete(level)
    db.session.commit()
    return jsonify({'message': 'Level deleted successfully!'})