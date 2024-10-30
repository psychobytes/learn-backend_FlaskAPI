from flask import Blueprint
from controllers.LevelController import get_levels, get_level, add_level, update_level, delete_level

level_bp = Blueprint('Level_bp', __name__)

level_bp.route('/api/level', methods=['GET'])(get_levels)
level_bp.route('/api/level/<int:id_level>', methods=['GET'])(get_level)
level_bp.route('/api/level', methods=['POST'])(add_level)
level_bp.route('/api/level/<int:id_level>', methods=['PUT'])(update_level)
level_bp.route('/api/level/<int:id_level>', methods=['DELETE'])(delete_level)