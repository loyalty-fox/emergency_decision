from py2neo import Node,Relationship,Graph,Path,Subgraph,data

# Connect to the local database Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

Function cql_transfer(disaster_type_label)
    # Execute cql_0 to obtain indicators num and loss
    cql_0 = 'MATCH node where node.label = "disaster_type_label" return RETURN keys(node).'
    parm_1, parm_2 = run(cql_0)
    
    # Remind the user to enter measurement data
    parm_1 = input("Enter the parm_1:")
    parm_2 = input("Enter the parm_2:")
    
    # Construct a fuzzy query cql_1 
    cql_1 = 'MATCH (n:ClassificationCriteria) where n.name=~".*{}.*" and n.parm1="{}" and n.parm2 ="{}" WITH n '.format(disaster_type_label, parm_1, parm_2)
    # Construct a fuzzy query cql_2 
    cql_2 = 'MATCH (m:RescueGuidelines) where m.disaster_level=n.level return n.level,n.reference_file,m.personnel_dispatch,m.reference_file'
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
