from py2neo import Node,Relationship,Graph,Path,Subgraph,data

# Connect to the local database
graph = Graph("bolt://localhost:7474", auth=("neo4j", "password"))

Function cql_transfer(disaster_type_label)
    Construct query cql0 to retrieve relevant indicators m and n based on the user's input label
    Execute cql0 to obtain indicators m and n
    Prompt the user to input measurement data for m and n
    Divide m and n into ranges and convert them into corresponding strings
    Construct a fuzzy query cql_1 to find nodes related to disaster level based on the ranges, using the WITH keyword to retain those nodes (refer to relevant documentation)
    Construct a fuzzy query cql_2 to query the level of those nodes and find related rescue protocol nodes, returning personnel dispatch indicators (refer to relevant documentation)
    cql = cql_1 + cql_2
    Return cql

disaster_type_label = input("Enter the type of disaster:")
my_sql = cql_transfer(disaster_type_label) 

# Obtain query results: 
answers = run(my_sql).data()

# Convert the query result into readable reference information
print("\n#############################################\n")
print("The {} level is:".format(label) + answers[0]['n.level'])
print("Disaster grading criteria reference:" + answers[0]['n.reference document'])
print("Number of rescue personnel to dispatch:" + answers[0]['m.personnel dispatch'])
print("Personnel dispatch criteria reference:" + answers[0]['m.reference document'])
