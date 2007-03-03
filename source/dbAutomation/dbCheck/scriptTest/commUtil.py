# -*- coding: utf-8 -*-

def query(cursor, sql):
    cursor.execute(sql)
    rs = cursor.fetchall()
    cursor.close()   
    return rs     

def insert1(conn,statement,inData):
    cursor = conn.cursor()
    cursor.execute(statement, inData)  #all in one
    cursor.close()
    conn.commit()