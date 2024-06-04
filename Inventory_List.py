import pymysql

inventoryList=[]

connect = pymysql.connect(host='localhost', user='root', 
                          password='1234', db='twosome_db',\
                          charset='utf8mb4')
cur = connect.cursor()

query = "SELECT * FROM inventory"
cur.execute(query)
connect.commit()

datas=cur.fetchall()

for data in datas:
    inventoryList.append(data)

def getInventoryList():
    return inventoryList

def setInventoryList(InvenList):
    
    return