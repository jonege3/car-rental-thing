from app.neo4j_connector import run_query

class Car:
    @staticmethod
    def create_car(make, model, year, location, status="available"):
        query = """
        CREATE (c:Car {make: $make, model: $model, year: $year, location: $location, status: $status})
        RETURN c
        """
        result = run_query(query, {"make": make, "model": model, "year": year, "location": location, "status": status})
        if result and result[0]:
            car_node = result[0]['c']
            return {
                'id': car_node.id,
                'make': car_node['make'],
                'model': car_node['model'],
                'year': car_node['year'],
                'location': car_node['location'],
                'status': car_node['status'],
            }
        return None

    @staticmethod
    def read_car(car_id):
        query = "MATCH (c:Car) WHERE ID(c) = $car_id RETURN c"
        result = run_query(query, {"car_id": car_id})
        if result and result[0]:
            car_node = result[0]['c']
            return {
                'id': car_node.id,
                'make': car_node['make'],
                'model': car_node['model'],
                'year': car_node['year'],
                'location': car_node['location'],
                'status': car_node['status'],
            }
        return None

    @staticmethod
    def update_car_status(car_id, status):
        query = """
        MATCH (c:Car) WHERE ID(c) = $car_id
        SET c.status = $status
        RETURN c
        """
        result = run_query(query, {"car_id": car_id, "status": status})
        if result and result[0]:
            car_node = result[0]['c']
            return {
                'id': car_node.id,
                'make': car_node['make'],
                'model': car_node['model'],
                'year': car_node['year'],
                'location': car_node['location'],
                'status': car_node['status'],
            }
        return None

    @staticmethod
    def delete_car(car_id):
        query = "MATCH (c:Car) WHERE ID(c) = $car_id DETACH DELETE c"
        run_query(query, {"car_id": car_id})
        return {'status': 'success', 'message': 'Car deleted successfully'}

class Customer:
    @staticmethod
    def create_customer(name, age, address):
        query = """
        CREATE (c:Customer {name: $name, age: $age, address: $address})
        RETURN c
        """
        result = run_query(query, {"name": name, "age": age, "address": address})
        if result and result[0]:
            customer_node = result[0]['c']
            return {
                'id': customer_node.id,
                'name': customer_node['name'],
                'age': customer_node['age'],
                'address': customer_node['address'],
            }
        return None

    @staticmethod
    def read_customer(customer_id):
        query = "MATCH (c:Customer) WHERE ID(c) = $customer_id RETURN c"
        result = run_query(query, {"customer_id": customer_id})
        if result and result[0]:
            customer_node = result[0]['c']
            return {
                'id': customer_node.id,
                'name': customer_node['name'],
                'age': customer_node['age'],
                'address': customer_node['address'],
            }
        return None

    @staticmethod
    def update_customer(customer_id, **kwargs):
        updates = ', '.join(f"c.{key} = ${key}" for key in kwargs)
        query = f"""
        MATCH (c:Customer) WHERE ID(c) = $customer_id
        SET {updates}
        RETURN c
        """
        params = {"customer_id": customer_id, **kwargs}
        result = run_query(query, params)
        if result and result[0]:
            customer_node = result[0]['c']
            return {
                'id': customer_node.id,
                'name': customer_node['name'],
                'age': customer_node['age'],
                'address': customer_node['address'],
            }
        return None

    @staticmethod
    def delete_customer(customer_id):
        query = "MATCH (c:Customer) WHERE ID(c) = $customer_id DETACH DELETE c"
        run_query(query, {"customer_id": customer_id})
        return {'status': 'success', 'message': 'Customer deleted successfully'}

class Employee:
    @staticmethod
    def create_employee(name, address, branch):
        query = """
        CREATE (e:Employee {name: $name, address: $address, branch: $branch})
        RETURN e
        """
        result = run_query(query, {"name": name, "address": address, "branch": branch})
        if result and result[0]:
            employee_node = result[0]['e']
            return {
                'id': employee_node.id,
                'name': employee_node['name'],
                'address': employee_node['address'],
                'branch': employee_node['branch'],
            }
        return None

    @staticmethod
    def read_employee(employee_id):
        query = "MATCH (e:Employee) WHERE ID(e) = $employee_id RETURN e"
        result = run_query(query, {"employee_id": employee_id})
        if result and result[0]:
            employee_node = result[0]['e']
            return {
                'id': employee_node.id,
                'name': employee_node['name'],
                'address': employee_node['address'],
                'branch': employee_node['branch'],
            }
        return None

    @staticmethod
    def update_employee(employee_id, **kwargs):
        updates = ', '.join(f"e.{key} = ${key}" for key in kwargs)
        query = f"""
        MATCH (e:Employee) WHERE ID(e) = $employee_id
        SET {updates}
        RETURN e
        """
        params = {"employee_id": employee_id, **kwargs}
        result = run_query(query, params)
        if result and result[0]:
            employee_node = result[0]['e']
            return {
                'id': employee_node.id,
                'name': employee_node['name'],
                'address': employee_node['address'],
                'branch': employee_node['branch'],
            }
        return None

    @staticmethod
    def delete_employee(employee_id):
        query = "MATCH (e:Employee) WHERE ID(e) = $employee_id DETACH DELETE e"
        run_query(query, {"employee_id": employee_id})
        return {'status': 'success', 'message': 'Employee deleted successfully'}

class Rental:
    @staticmethod
    def create_rental(car_id, customer_id, rental_date, return_date):
        # Update the car status to 'rented'
        Car.update_car_status(car_id, "rented")

        query = """
        MATCH (c:Car), (cu:Customer)
        WHERE ID(c) = $car_id AND ID(cu) = $customer_id
        CREATE (cu)-[r:RENTED {rental_date: $rental_date, return_date: $return_date}]->(c)
        RETURN r
        """
        result = run_query(query, {"car_id": car_id, "customer_id": customer_id, "rental_date": rental_date, "return_date": return_date})
        return result

    @staticmethod
    def read_rental(rental_id):
        query = "MATCH (cu:Customer)-[r:RENTED]->(c:Car) WHERE ID(r) = $rental_id RETURN cu, r, c"
        result = run_query(query, {"rental_id": rental_id})
        if result and result[0]:
            rental_info = result[0]
            return {
                'customer': {
                    'id': rental_info['cu'].id,
                    'name': rental_info['cu']['name']
                },
                'car': {
                    'id': rental_info['c'].id,
                    'make': rental_info['c']['make'],
                    'model': rental_info['c']['model']
                },
                'rental_details': {
                    'rental_date': rental_info['r']['rental_date'],
                    'return_date': rental_info['r']['return_date']
                }
            }
        return None

    @staticmethod
    def update_rental(rental_id, **kwargs):
        updates = ', '.join(f"r.{key} = ${key}" for key in kwargs)
        query = f"""
        MATCH ()-[r:RENTED]->()
        WHERE ID(r) = $rental_id
        SET {updates}
        RETURN r
        """
        params = {"rental_id": rental_id, **kwargs}
        result = run_query(query, params)
        if result and result[0]:
            rental_node = result[0]['r']
            return {
                'id': rental_node.id,
                'rental_date': rental_node['rental_date'],
                'return_date': rental_node['return_date'],
            }
        return None

    @staticmethod
    def delete_rental(rental_id):
        # First, find the rental details to get the associated car ID
        query = """
        MATCH ()-[r:RENTED]->(c:Car)
        WHERE ID(r) = $rental_id
        RETURN ID(c) AS car_id
        """
        car_id_result = run_query(query, {"rental_id": rental_id})
        if car_id_result and car_id_result[0]:
            car_id = car_id_result[0]['car_id']

            # Delete the rental relationship
            delete_query = "MATCH ()-[r:RENTED]->() WHERE ID(r) = $rental_id DELETE r"
            run_query(delete_query, {"rental_id": rental_id})

            # Update the car status back to 'available'
            Car.update_car_status(car_id, "available")

            return {'status': 'success', 'message': 'Rental deleted successfully and car status updated to available'}
        return {'status': 'error', 'message': 'Rental not found'}

