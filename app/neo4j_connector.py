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

    def run_query(query, params=None):
		with driver.session() as session:
			result = session.run(query, params or {})
			return [record.data() for record in result]  # Ensure you're fetching data correctly

# Create a Neo4j connection instance
neo4j_connector = Neo4jConnector()

# Helper function to run queries
def run_query(query, parameters=None):
    return neo4j_connector.query(query, parameters)
