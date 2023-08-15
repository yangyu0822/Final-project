#!/usr/local/bin/python3
#For Local Use: !/usr/bin/env python3

import sys
import re


def main():

    # Code parses the random human proteins derived text file into an array
    index=1
    data=[]
    with open("SimpleData.txt") as file:
        for line in file:
            if '#' not in line:
                line = re.sub('\n','',line)
                split_line=re.split('\t',line)
                split_line.insert(0,index)
                index+=1
                data.append(split_line)
                #DEBUG: print(split_line)
    file.close()
    
    #with open("FB_SimpleData.txt") as file:
        #for line_num, line in enumerate(file, 1):
            #if line.count('\t') != 6:  # We expect 6 tabs for 7 values
                #print(f"Issue on line {line_num}: {line.strip()}")

    #print(data[:5]) #DEBUG
    for entry in data:
        print(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6])
        print(type(entry[0]),type(entry[1]))


    # Code uses mysql connector to build mySQL database on the class server from array
    conn = mysql.connector.connect(user='yyu104', password='pass', host='localhost', database='yyu104')
    curs = conn.cursor()
    build_table = """
        INSERT INTO prodatabase (ind, FBid, feature_type, name, symbol, uniprot_function, protein_family)
             VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for entry in data:
        curs.execute(build_table,(entry[0],entry[1],entry[2],entry[3],entry[4],entry[5],entry[6]))
        #print(entry) #DEBUG

    conn.commit()
    print('finished build') #DEBUG

    # Close database resources
    curs.close()
    conn.close()

    
if __name__ == '__main__':
    main()