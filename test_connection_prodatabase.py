#!/usr/local/bin/python3
#For Local Use: !/usr/bin/env python3

import sys
import re
import mysql.connector
import random

def main():

    #DEBUG check that mysql connector fetched data
    conn = mysql.connector.connect(user='yyu104', password='pwd', host='localhost', database='yyu104')
    curs = conn.cursor()

    verification_qry = """
        SELECT FBid, feature_type, name, symbol, uniprot_function, protein_family FROM odorbase WHERE ind = %s
    """

    random_index = random.randrange(0,47)
    curs.execute(verification_qry,(random_index,))
    '''
    for (ind, FBid, feature_type, name, symbol, uniprot_function, protein_family) in curs:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(ind, FBid, feature_type, name, symbol, uniprot_function, protein_family))
    '''
    results = dict()
    for (FBid, feature_type, name, symbol, uniprot_function, protein_family) in curs:
        results = {"ProteinID": FBid, "Feature Type":feature_type, "Name":name, "Symbol":symbol, "UniProt Function":uniprot_function, "Protein Family":protein_family}
    print(results)
    # Close database resources
    curs.close()
    conn.close()

if __name__ == '__main__':
    main()