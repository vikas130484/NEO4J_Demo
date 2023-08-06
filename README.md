
<!-- Neo4j Demo -->
## Neo4j Demo

**Technical Assignment**

### Installation/Configuration

_Follow following steps in sequence to complete the requisite assignment._

1 Run the following command to start the neo4j docker.

  ```sh
  docker run --name Neo4j_Demo -p7474:7474 -p7687:7687 -d -v "C:/Users/Vikas Kumar/OneDrive/Desktop/NEO4J_Demo/data:/data" -v "C:/Users/Vikas Kumar/OneDrive/Desktop/NEO4J_Demo/logs:/logs" -v "C:/Users/Vikas Kumar/OneDrive/Desktop/NEO4J_Demo/import:/var/lib/neo4j/import" -v "C:/Users/Vikas Kumar/OneDrive/Desktop/NEO4J_Demo/plugins:/plugins" --env NEO4J_AUTH=neo4j/password --env NEO4J_dbms_connector_https_advertised__address="localhost:7473" --env NEO4J_dbms_connector_http_advertised__address="localhost:7474" --env NEO4J_dbms_connector_bolt_advertised__address="localhost:7687" neo4j:latest
  ```
 



 
