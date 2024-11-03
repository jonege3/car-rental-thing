class Car:
    @staticmethod
    def create_car(make, model, year, location, status="available"):
        query = "CREATE (c:Car {make: $make, model: $model, year: $year, location: $location, status: $status}) RETURN c"
        return run_query(query, {"make": make, "model": model, "year": year, "location": location, "status": status})
