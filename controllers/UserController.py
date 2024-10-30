from flask import jsonify, request
from models.UserModel import User
from models.LevelModel import Level
from config import db

def get_users():
    users = User.query.all()
    users_with_levels = []
    for user in users:
        # Ambil category terkait dari book
        level = Level.query.get(user.level_id)
        # Tambahkan detail buku beserta nama category
        users_with_levels.append({
            'user_id': user.user_id,
            'username': user.username,
            'password': user.password,
            'full_name': user.full_name,
            'status': user.status,
            'level_name': level.name if level else "No Level"
        })
    response = {
        'status': 'success',
        'data': {
            'users': users_with_levels
        },
        'message': 'Users retrieved successfully'
    }
    return jsonify(response), 200

def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404
    level = Level.query.get(user.level_id)
    user_data = {
        'user_id': user.user_id,
        'username': user.username,
        'password': user.password,
        'full_name': user.full_name,
        'status': user.status,
        'level_name': level.name if level else "No Level"
    }
    response = {
        'status': 'success',
        'data': {
            'users': user_data
        },
        'message': 'Users retrieved successfully'
    }
    return jsonify(response), 200

def add_user():
    new_user_data = request.get_json()
    new_user = User(
        username=new_user_data['username'],
        password=new_user_data['password'],
        full_name=new_user_data['full_name'],
        status=new_user_data['status'],
        level_id=new_user_data['level_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User  added successfully!', 'user': new_user.to_dict()}), 201

def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User  not found'}), 404
    updated_data = request.get_json()
    user.username = updated_data.get('username', user.username)
    user.password = updated_data.get('password', user.password)
    user.full_name = updated_data.get('full_name', user.full_name)
    user.status = updated_data.get('status', user.status)
    user.level_id = updated_data.get('level_id', user.level_id)

    db.session.commit()
    return jsonify({'message': 'User  updated successfully!', 'user': user.to_dict()})

def patch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User  not found'}), 404
    patch_data = request.get_json()
    if 'username' in patch_data:
        user.username = patch_data['username']
    if 'password' in patch_data:
        user.password = patch_data['password']
    if 'full_name' in patch_data:
        user.full_name = patch_data['full_name']
    if 'status' in patch_data:
        user.status = patch_data['status']
    if 'level' in patch_data:
        level = Level.query.get(patch_data['level_id'])
        if level:
            user.level_id = patch_data['level_id']
        else:
            return jsonify({'error': 'Level not found'}), 404
        
    db.session.commit()
    return jsonify({'message': 'User  partially updated successfully!', 'user': user.to_dict()})

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User  not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User  deleted successfully!'})