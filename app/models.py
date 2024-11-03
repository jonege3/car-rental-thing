from app.neo4j_connector import run_query

class Car:
    @staticmethod
    def create_car(make, model, year, location, status="available"):
        query = """
        CREATE (c:Car {make: $make, model: $model, year: $year, location: $location, status: $status})
        RETURN c
        """
        return run_query(query, {"make": make, "model": model, "year": year, "location": location, "status": status})

    @staticmethod
    def read_car(car_id):
        query = "MATCH (c:Car) WHERE ID(c) = $car_id RETURN c"
        return run_query(query, {"car_id": car_id})

    @staticmethod
    def update_car(car_id, **kwargs):
        updates = ', '.join(f"c.{key} = ${key}" for key in kwargs)
        query = f"""
        MATCH (c:Car) WHERE ID(c) = $car_id
        SET {updates}
        RETURN c
        """
        params = {"car_id": car_id, **kwargs}
        return run_query(query, params)

    @staticmethod
    def delete_car(car_id):
        query = "MATCH (c:Car) WHERE ID(c) = $car_id DETACH DELETE c"
        return run_query(query, {"car_id": car_id})

class Customer:
    @staticmethod
    def create_customer(name, age, address):
        query = """
        CREATE (c:Customer {name: $name, age: $age, address: $address})
        RETURN c
        """
        return run_query(query, {"name": name, "age": age, "address": address})

    @staticmethod
    def read_customer(customer_id):
        query = "MATCH (c:Customer) WHERE ID(c) = $customer_id RETURN c"
        return run_query(query, {"customer_id": customer_id})

    @staticmethod
    def update_customer(customer_id, **kwargs):
        updates = ', '.join(f"c.{key} = ${key}" for key in kwargs)
        query = f"""
        MATCH (c:Customer) WHERE ID(c) = $customer_id
        SET {updates}
        RETURN c
        """
        params = {"customer_id": customer_id, **kwargs}
        return run_query(query, params)

    @staticmethod
    def delete_customer(customer_id):
        query = "MATCH (c:Customer) WHERE ID(c) = $customer_id DETACH DELETE c"
        return run_query(query, {"customer_id": customer_id})

class Employee:
    @staticmethod
    def create_employee(name, address, branch):
        query = """
        CREATE (e:Employee {name: $name, address: $address, branch: $branch})
        RETURN e
        """
        return run_query(query, {"name": name, "address": address, "branch": branch})

    @staticmethod
    def read_employee(employee_id):
        query = "MATCH (e:Employee) WHERE ID(e) = $employee_id RETURN e"
        return run_query(query, {"employee_id": employee_id})

    @staticmethod
    def update_employee(employee_id, **kwargs):
        updates = ', '.join(f"e.{key} = ${key}" for key in kwargs)
        query = f"""
        MATCH (e:Employee) WHERE ID(e) = $employee_id
        SET {updates}
        RETURN e
        """
        params = {"employee_id": employee_id, **kwargs}
        return run_query(query, params)

    @staticmethod
    def delete_employee(employee_id):
        query = "MATCH (e:Employee) WHERE ID(e) = $employee_id DETACH DELETE e"
        return run_query(query, {"employee_id": employee_id})
