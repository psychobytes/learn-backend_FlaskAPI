from flask import Blueprint
from controllers.UserController import get_users, get_user, add_user, update_user, patch_user, delete_user

user_bp = Blueprint('User_bp', __name__)

user_bp.route('/api/users', methods=['GET'])(get_users)
user_bp.route('/api/users/<int:user_id>', methods=['GET'])(get_user)
user_bp.route('/api/users', methods=['POST'])(add_user)
user_bp.route('/api/users/<int:user_id>', methods=['PATCH'])(patch_user)
user_bp.route('/api/users/<int:user_id>', methods=['UPDATE'])(update_user)
user_bp.route('/api/users/<int:user_id>', methods=['DELETE'])(delete_user)