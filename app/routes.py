from flask import request, jsonify
from app import app
from app.models import Car

@app.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    car = Car.create_car(data['make'], data['model'], data['year'], data['location'])
    return jsonify(car)
