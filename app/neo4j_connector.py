from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Neo4jConnector:
    def __init__(self):
        self.uri = os.getenv("NEO4J_URI")
        self.user = os.getenv("NEO4J_USER")
        self.password = os.getenv("NEO4J_PASSWORD")
        
        if not all([self.uri, self.user, self.password]):
            raise ValueError("Neo4j connection details are missing in the environment variables.")

        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        """Closes the Neo4j connection gracefully."""
        if self.driver:
            self.driver.close()

    def run_query(self, query, params=None):
        """Executes a query against the Neo4j database."""
        try:
            with self.driver.session() as session:
                result = session.run(query, params or {})
                return [record.data() for record in result]  # Return records as a list of dictionaries
        except Exception as e:
            print(f"Error executing query: {e}")
            return []

# Create a Neo4j connection instance
neo4j_connector = Neo4jConnector()

# Helper function to run queries
def run_query(query, params=None):
    return neo4j_connector.run_query(query, params)  # Use the instance method to execute queries
