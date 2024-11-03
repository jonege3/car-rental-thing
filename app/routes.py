from flask import request, jsonify
from app import app
from app.models import Car, Customer, Employee

# Car Endpoints
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    car = Car.create_car(data['make'], data['model'], data['year'], data['location'])
    return jsonify(car)

@app.route('/cars/<int:car_id>', methods=['GET'])
def read_car(car_id):
    car = Car.read_car(car_id)
    return jsonify(car)

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.get_json()
    car = Car.update_car(car_id, **data)
    return jsonify(car)

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    Car.delete_car(car_id)
    return jsonify({"message": "Car deleted successfully"})

# Customer Endpoints
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer.create_customer(data['name'], data['age'], data['address'])
    return jsonify(customer)

@app.route('/customers/<int:customer_id>', methods=['GET'])
def read_customer(customer_id):
    customer = Customer.read_customer(customer_id)
    return jsonify(customer)

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    customer = Customer.update_customer(customer_id, **data)
    return jsonify(customer)

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    Customer.delete_customer(customer_id)
    return jsonify({"message": "Customer deleted successfully"})

# Employee Endpoints
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    employee = Employee.create_employee(data['name'], data['address'], data['branch'])
    return jsonify(employee)

@app.route('/employees/<int:employee_id>', methods=['GET'])
def read_employee(employee_id):
    employee = Employee.read_employee(employee_id)
    return jsonify(employee)

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    employee = Employee.update_employee(employee_id, **data)
    return jsonify(employee)

@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    Employee.delete_employee(employee_id)
    return jsonify({"message": "Employee deleted successfully"})

# Rental Endpoints

@app.route('/order-car', methods=['POST'])
def order_car():
    data = request.get_json()
    response = Booking.order_car(data['customer_id'], data['car_id'])
    return jsonify(response)

@app.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    data = request.get_json()
    response = Booking.cancel_order(data['customer_id'], data['car_id'])
    return jsonify(response)

@app.route('/rent-car', methods=['POST'])
def rent_car():
    data = request.get_json()
    response = Booking.rent_car(data['customer_id'], data['car_id'])
    return jsonify(response)

@app.route('/return-car', methods=['POST'])
def return_car():
    data = request.get_json()
    response = Booking.return_car(data['customer_id'], data['car_id'], data['condition'])
    return jsonify(response)


