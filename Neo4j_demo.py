from neo4j import GraphDatabase

class neo4j_data_load:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run(self):
        with self.driver.session() as session:
            result = session.execute_write(self.execute_queries)
            print(result)

    @staticmethod
    def execute_queries(tx):

        csv_path_edu = "file:///sng_education.csv"
        csv_path_work = "file:///sng_work.csv"
        csv_path_transaction = "file:///sng_transaction.csv"
        csv_path_trips = "file:///sng_trips.csv"

        q_edu = """LOAD CSV WITH HEADERS FROM '{filepath}' AS row
                        MERGE (person:Person {name: row.name, passportnumber:row.passportnumber})
                        MERGE (institute:Institute {nameofinstitution: row.nameofinstitution,course:row.course,startyear:row.startyear,endyear:row.endyear})
                        MERGE (country:Country{country: row.country})
                        MERGE (person)-[:STUDIED_AT]->(institute)
                        MERGE (institute)-[:SITUATED_IN]->(country)"""
        q_edu = q_edu.replace('{filepath}',csv_path_edu)

        q_work = """LOAD CSV WITH HEADERS FROM '{filepath}' AS row
                        MERGE (person:Person {name: row.name, passportnumber:row.passportnumber})
                        MERGE (organization:Organization {nameoforganization: row.nameoforganization,designation:row.designation,startyear:row.startyear,endyear:row.endyear})
                        MERGE (country:Country{country: row.country})
                        MERGE (person)-[:WORKED_AT]->(organization)
                        MERGE (organization)-[:SITUATED_IN]->(country)"""
        q_work = q_work.replace('{filepath}',csv_path_work)

        
        q_transaction = """LOAD CSV WITH HEADERS FROM '{filepath}' AS row
                        MERGE (person:Person {name: row.name, passportnumber:row.passportnumber})
                        MERGE (transaction:Transaction {cardnumber: row.cardnumber,transactiondate:row.transactiondate,merchant:row.merchant,amount:row.amount})
                        MERGE (country:Country{country: row.country})
                        MERGE (person)-[:PERFORMED]->(transaction)
                        MERGE (transaction)-[:PERFORMED_IN]->(country)"""
        q_transaction = q_transaction.replace('{filepath}',csv_path_transaction)

        q_trips = """LOAD CSV WITH HEADERS FROM '{filepath}' AS row
                        MERGE (person:Person {name: row.name, passportnumber:row.passportnumber})
                        MERGE (country_dep:Country{country: row.departurecountry})
                        MERGE (country_arr:Country{country: row.arrivalcountry})
                        MERGE (country_citizen:Country{country: row.citizenship})
                        MERGE (person)-[:TRAVELLED_FROM{departuredate:row.departuredate}]->(country_dep)
                        MERGE (person)-[:TRAVELLED_TO{arrivaldate:row.arrivaldate}]->(country_arr)
                        MERGE (person)-[:CITIZEN_OF]->(country_citizen)"""
        q_trips = q_trips.replace('{filepath}',csv_path_trips)
        
        result1 = tx.run(q_edu)
        result2 = tx.run(q_work)
        result3 = tx.run(q_transaction)
        result4 = tx.run(q_trips)

        return str(result1)+str(result2)+str(result3)+str(result4)


if __name__ == "__main__":
    task = neo4j_data_load("neo4j://localhost:7687", "neo4j", "password")
    task.run()
    task.close()
