#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

# Prodatabase is a 47 entry, 6 column SQL table on the class server with human genes 
# This script pulls a specific entry from the database and dumps the data in JSON format

def main():

    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')

    conn = mysql.connector.connect(user='yyu104', password='pwd', host='localhost', database='yyu104')
    curs = conn.cursor()

    qry = """
            SELECT FBid, feature_type, name, symbol, uniprot_function, protein_family FROM prodatabase
            WHERE FBid LIKE %s OR name LIKE %s OR symbol LIKE %s OR uniprot_function LIKE CONCAT('%', %s, '%') OR protein_family LIKE CONCAT('%', %s, '%')
    """

    curs.execute(qry, (term, term, term, term, term))
    results = { 'match_count': 0, 'matches': list() }
    for (FBid, feature_type, name, symbol, uniprot_function, protein_family) in curs:
        results['matches'].append({"PorteinID": FBid, "Feature_Type":feature_type, "Name":name, "Symbol":symbol, "UniProt_Function":uniprot_function, "Protein_Family":protein_family})
        results['match_count'] += 1

    curs.close()
    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()