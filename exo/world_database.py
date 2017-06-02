import sqlite3


def list_of_tables_in_database(database):
    """ return the list of all tables name in a given database
        this list is ordered according to names
    """
    request = """   select name from sqlite_master
                    where type = 'table'
                    order by name asc                """
    results = database.execute(request).fetchall()

    # method 1 - if we prefer the list in intention mecanism
    listOfTables = list(i[0] for i in results)

    # method 2 - if we prefer the lambda-function mecanism
    # listOfTables = (lambda l:list(i[0] for i in l)) (results)

    return listOfTables


def database_description(database, databaseFileName):
    """ print the description of any of the tables in database """
    tables = list_of_tables_in_database(database)
    nbTables = len(tables)
    print("\nDescription of the database " + databaseFileName + " - " +
          str(nbTables) + " tables (alphabetic sort on names):")
    for tableName in tables:
        request = "pragma table_info(" + tableName + ")"
        resultat = database.execute(request).fetchall()
        print("\nDescription of the table:", tableName)
        for column in resultat:
            print("%i | %-55s | %-15s | %d | %11s | %d" % column)


def show_query_results(query, format):
    """ print every result of an SQL query according to a specified format """
    print("\n Results of: " + query)

    for i in base.execute(query).fetchall():
        print(format % i)
    print("-*" * 40)


databaseFileName = "world.db"

# 'connexion' à la base de données
base = sqlite3.connect(databaseFileName)
data = base.cursor()

# print(list_of_tables_in_database(data))
print(list_of_tables_in_database(base))
print(database_description(base, databaseFileName))

request_01 = "SELECT name,population FROM country WHERE population > 200000000"
request_02 = "SELECT COUNT(*) FROM (SELECT name,population FROM country WHERE population > 70000000 ORDER BY population DESC)"
request_02b = "SELECT name,population FROM country WHERE population > 70000000"
request_03 = "SELECT name,population FROM country WHERE population > 70000000 ORDER BY name"
request_04 = "SELECT name,population FROM country WHERE population > 70000000 ORDER BY population DESC"
request_05 = "SELECT name,population FROM country WHERE population > 200000000"

show_query_results(request_01, "%25s : %21d")
show_query_results(request_02, "%d")
show_query_results(request_02b, "%25s : %21d")
show_query_results(request_03, "%25s : %21d")
show_query_results(request_04, "%25s : %21d")
show_query_results(request_05, "%25s : %21d")

# fermeture de la connexion à la base
base.close()
