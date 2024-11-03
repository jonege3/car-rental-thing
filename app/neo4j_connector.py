from neo4j import GraphDatabase

def run_query(query, parameters=None):
    with driver.session() as session:
        return session.run(query, parameters)
