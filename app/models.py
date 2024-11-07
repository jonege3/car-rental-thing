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

class Employee:
    @staticmethod
    def create_employee(name, position, salary, location):
        query = """
        CREATE (e:Employee {name: $name, position: $position, salary: $salary, location: $location})
        RETURN e
        """
        result = run_query(query, {"name": name, "position": position, "salary": salary, "location": location})
        if result and result[0]:
            employee_node = result[0]['e']
            return {
                'name': employee_node['name'],
                'position': employee_node['position'],
                'salary': employee_node['salary'],
                'location': employee_node['location'],
            }
        return None

    @staticmethod
    def read_employee(employee_id):
        query = "MATCH (e:Employee) WHERE ID(e) = $employee_id RETURN e"
        result = run_query(query, {"employee_id": employee_id})
        if result and result[0]:
            employee_node = result[0]['e']
            return {
                'name': employee_node['name'],
                'position': employee_node['position'],
                'salary': employee_node['salary'],
                'location': employee_node['location'],
            }
        return None

    @staticmethod
    def update_employee_salary(employee_id, salary):
        query = """
        MATCH (e:Employee) WHERE ID(e) = $employee_id
        SET e.salary = $salary
        RETURN e
        """
        result = run_query(query, {"employee_id": employee_id, "salary": salary})
        if result and result[0]:
            employee_node = result[0]['e']
            return {
                'name': employee_node['name'],
                'position': employee_node['position'],
                'salary': employee_node['salary'],
                'location': employee_node['location'],
            }
        return None

    @staticmethod
    def delete_employee(employee_id):
        query = "MATCH (e:Employee) WHERE ID(e) = $employee_id DETACH DELETE e"
        run_query(query, {"employee_id": employee_id})
        return {'status': 'success', 'message': 'Employee deleted successfully'}

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
