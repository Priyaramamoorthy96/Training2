from neo4j.v1 import GraphDatabase
uri = "bolt://localhost:7687"
userName = "neo4j"
password = "PILLOWS112012;"
graphDB_Driver = GraphDatabase.driver(uri, auth=(userName, password)
Daniel = """MATCH (a:Actor),(b:movies),(c:movies),(d:movies)
WHERE a.name = "DANEIL_RADCLIFF" AND b.name = "HARRY_POTTER" AND c.name = "JUNGLE" AND d.name="HORNS"
CREATE (a)-[rd:HARRY_POTTER]->(b), (a)-[re:Yossi]->(c), (a)-[rf:Perrish]->(d)"""

Robert  = """MATCH (a:Actor),(b:movies),(c:movies),(d:movies)
WHERE a.name = "ROBERT_PATINSION" AND b.name = "TWILIGHT" AND c.name = "HARRY_POTTER" AND d.name="GOOD_TIME"
CREATE (a)-[rd:Cedric]->(b), (a)-[re:Edward]->(c), (a)-[rf:Connie]->(d)"""

Jacob = """MATCH (a:Actor),(b:movies),(c:movies),(d:movies)
WHERE a.name = "JACOB_BLACK" AND b.name = "HARRY_POTTER" AND c.name = "TWILIGHT" AND d.name="TRACERS"
CREATE (a)-[rd:Albert]->(b), (a)-[re:Tylor]->(c), (a)-[rf:Nick]->(d)"""

Emma = """MATCH (a:Actor),(b:movies),(c:movies),(d:movies)
WHERE a.name = "EMMA_WATSON" AND b.name = "HARRY_POTTER" AND c.name = "CIRCLE" AND d.name="BEAUTY_BEAST"
CREATE (a)-[rd:Hermione]->(b), (a)-[re:Tylor]->(c), (a)-[rf:Nick]->(d)"""

Hardwicke = """MATCH (a:directors),(b:movies),(c:movies)
WHERE a.name = "HARDWICKE" AND b.name = "HARRY_POTTER" AND c.name = "TWILIGHT" 
CREATE (a)-[rd:Directed_on_2007 ]->(b), (a)-[re:Directed_on_2009]->(c)"""

Aaron = """MATCH (a:directors),(b:movies),(c:movies)
WHERE a.name = "AARON" AND b.name = "GOOD_TIME" AND c.name = "CIRCLE" 
CREATE (a)-[rd:Directed_on_2017 ]->(b), (a)-[re:Directed_on_2015]->(c)"""

Alexandre = """MATCH (a:directors),(b:movies),(c:movies)
WHERE a.name = "ALEXANDRE" AND b.name = "TRACERS" AND c.name = "HORNS" 
CREATE (a)-[rd:Directed_on_2015]->(b), (a)-[re:Directed_on_2013]->(c)"""

Bill = """MATCH (a:directors),(b:movies),(c:movies)
WHERE a.name = "BILL" AND b.name = "BEAUTY_BEAST" AND c.name = "JUNGLE" 
CREATE (a)-[rd:Directed_on_2017 ]->(b), (a)-[re:Directed_on_2015]->(c)"""

Year1 = """MATCH (a:movies),(b:movies)
WHERE a.name = "GOOD_TIME" AND b.name = "CIRCLE"
CREATE (a)-[rd:RelesedOn_2016]->(b)"""

Year2 = """MATCH (a:movies),(b:movies)
WHERE a.name = "TRACERS" AND b.name = "HORNS"
CREATE (a)-[rd:RelesedOn_2014]->(b)"""

Year3 = """MATCH (a:movies),(b:movies)
WHERE a.name = "JUNGLE" AND b.name = "BEAUTY_BEAST"
CREATE (a)-[rd:RelesedOn_2017]->(b)"""

heros = ["Daneil_Radcliff","Robert_Patinsion","Jacob_Black","Emma_Watson"]
movies = ["Harry_Potter", "Jungle", "Horns", "Twilight", "Good_Time" , "Tracers" , "Beauty_Beast" , "Circle"]
directors = ["Hardwicke", "Aaron", "Alexandre", "Bill"]
relations = [Daniel,Robert,Jacob,Emma,Hardwicke,Aaron,Alexandre,Bill,Year1,Year2,Year3]

with graphDB_Driver.session() as graphDB_Session:
    inc = 0
    for hero in heros:
        createnode = "create(" + hero.lower()+ ": Actor{name:" + '"' +hero.upper() + '"' + "})"
        graphDB_Session.run(createnode)
        inc = inc + 1   

    inc = 0
    for movie in movies:
        createnode = "create(" + movie.lower()+ ":movies{name:" + '"' +movie.upper() + '"' + "})"
        graphDB_Session.run(createnode)
        inc = inc + 1

    inc = 0
    for director in directors:
        createnode = "create(" + director.lower()+ ":directors{name:" + '"' +director.upper() + '"' + "})"
        graphDB_Session.run(createnode)
        inc = inc + 1

    inc = 0
    for relation in relations:
        graphDB_Session.run(relation)  
        inc = inc + 1

print("Movie Database created on Graph Format")
