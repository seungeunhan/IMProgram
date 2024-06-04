import pymysql
from datetime import datetime

SangMi_List=[]

connect = pymysql.connect(host='localhost', user='root', 
                          password='1234', db='twosome_db',\
                          charset='utf8mb4')
cur = connect.cursor()

query = "SELECT * FROM sangmi "
cur.execute(query)
connect.commit()

datas=cur.fetchall()


for data in datas:
    SangMi_List.append(data)



def getSangMiList():

    return SangMi_List


