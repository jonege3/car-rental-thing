from flask import Flask
from app.neo4j_connector import neo4j_connector

app = Flask(__name__)

# Close Neo4j connection when app stops
@app.teardown_appcontext
def close_neo4j_connection(exception):
    neo4j_connector.close()

from app import routes  # Import routes to register them with the app
