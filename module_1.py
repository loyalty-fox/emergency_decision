from py2neo import Node,Relationship,Graph,Path,Subgraph,data
# 本地neo4j数据库网址，全局用户名，自己设置的密码
Connect to the database

Function cql_transfer(disaster_type_label)
    Construct query cql0 to retrieve relevant indicators m and n based on the user's input label
    Execute cql0 to obtain indicators m and n
    Prompt the user to input measurement data for m and n
    Divide m and n into ranges and convert them into corresponding strings
    Construct a fuzzy query cql1 to find nodes related to disaster level based on the ranges, using the WITH keyword to retain those nodes (refer to relevant documentation)
    Construct a fuzzy query cql2 to query the level of those nodes and find related rescue protocol nodes, returning personnel dispatch indicators (refer to relevant documentation)
    cql = cql1 + cql2
    Return cql

Set disaster_type_label variable = User input("Enter the type of disaster:")
Pass the label variable to cql_transfer function to generate the SQL statement my_sql
Obtain query results: answers = run(my_sql).data()

Print the answers in a readable format to provide information to the user
