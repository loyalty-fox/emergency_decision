import csv
from py2neo import Graph,Node,Relationship,NodeMatcher

# Connect to the local database Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Import Nodes
with open(nodes.csv):
  data = line.split_by_comma
  Create an empty node properties dictionary node_properties
  For each column in data:
      If data[i] is not empty:
          Add data[i] to node_properties with attribute name header[i]
  node = Node(label, **node_properties)
# Save the node to the graph
  graph.create(node)

# 导入关系
with open(relationship.csv):
  For each line in csv:
    data = line.split_by_comma
    start_node_id, relationship_type, end_node_id = data[0], data[1], data[2]
    
    # Search for start node and end node in the database
    start_node = graph.node.match(start_node_id)
    end_node = graph.node.match(end_node_id)
    
    If start_node in graph and end_node in graph:
        relationship = Relationship(start_node, relationship_type, end_node)
        g.create(relationship)
