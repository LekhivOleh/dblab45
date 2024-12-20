from flask import Blueprint, jsonify
from src.booking.services.room_has_amenity_service import RoomHasAmenityService
from src.booking.dao.room_has_amenity_dao import RoomHasAmenityDao
from src import db

room_has_amenity_bp = Blueprint('room_has_amenity_bp', __name__)
room_has_amenity_dao = RoomHasAmenityDao(db.session)
room_has_amenity_service = RoomHasAmenityService(room_has_amenity_dao)

amenity_has_room_bp = Blueprint('amenity_has_room_bp', __name__)
amenity_has_room_dao = RoomHasAmenityDao(db.session)
amenity_has_room_service = RoomHasAmenityService(amenity_has_room_dao)

@room_has_amenity_bp.route('/rooms/<int:room_id>/amenities', methods=['GET'])
def get_amenities_by_room(room_id):
    amenities = room_has_amenity_service.get_amenities_by_room(room_id)
    if amenities is None:
        return jsonify({'error': 'Room not found'}), 404
    return jsonify([amenity.serialize() for amenity in amenities])

@amenity_has_room_bp.route('/amenities/<int:amenity_id>/rooms', methods=['GET'])
def get_rooms_by_amenity(amenity_id):
    rooms = room_has_amenity_service.get_rooms_by_amenity(amenity_id)
    if rooms is None:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify([room.serialize() for room in rooms])