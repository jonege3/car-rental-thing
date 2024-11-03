from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Set up Neo4j connection
class Neo4jConnector:
    def __init__(self):
        self.uri = os.getenv("NEO4J_URI")
        self.user = os.getenv("NEO4J_USER")
        self.password = os.getenv("NEO4J_PASSWORD")
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        if self.driver:
            self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters)
            return [record for record in result]

# Create a Neo4j connection instance
neo4j_connector = Neo4jConnector()

# Helper function to run queries
def run_query(query, parameters=None):
    return neo4j_connector.query(query, parameters)
