import mysql.connector

class ORDER_LIST:
    #ORDER 데이터 다 가져오는부분
    def get_Order_Data(self):
        try:
            cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='twosome_db'
            )

            if cnx.is_connected():
                data_list = []
                print('DB 연결 완료')
                cursor = cnx.cursor()
                query = 'select * from orders order by order_date desc'
                cursor.execute(query)
                result = cursor.fetchall()

        except mysql.connector.Error as e:
            print('MYSQL 데이터베이스 연결 오류 발생')
        finally:
            if 'connection' in locals():
                cnx.close()
                print('db연결 해제')
        return result
    
    def get_Product_data(self):
        try:
            cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='twosome_db'
            )

            if cnx.is_connected():

                print('DB 연결 완료')
                cursor = cnx.cursor()
                query = 'select product_name, product_cost from products;'
                cursor.execute(query)
                result = cursor.fetchall()
        except mysql.connector.Error as e:
            print('MYSQL 데이터베이스 연결 오류 발생')
        finally:
            if 'connection' in locals():
                cnx.close()
                print('db연결 해제')
        return result       
    
    def get_inventory_data(self):
        try:
            cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='twosome_db'
            )

            if cnx.is_connected():
                
                print('DB 연결 완료')
                cursor = cnx.cursor()
                query = 'select 제품명, 수량, 단가 from inventory'
                cursor.execute(query)
                reuslt =  cursor.fetchall()
                cnx.commit()
            
        except mysql.connector.Error as e:
            print(e)
            print('MYSQL 데이터베이스 연결 오류 발생')
        finally:
            if 'connection' in locals():
                cnx.close()
                print('db연결 해제')
        return reuslt

    def reg_Order_Data(self,value):
        try:
            cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='twosome_db'
            )

            if cnx.is_connected():
                
                print('DB 연결 완료')
                cursor = cnx.cursor()
                query = 'INSERT INTO ORDERS(PRODUCT_NAME, ORDER_DATE, ORDER_COST, ORDER_COUNT, ORDER_QUANTITY,ORDER_STATE) VALUES(%s, %s, %s, %s, %s, %s)'
                cursor.execute(query, value)
                cnx.commit()
            
        except mysql.connector.Error as e:
            print(e)
            print('MYSQL 데이터베이스 연결 오류 발생')
        finally:
            if 'connection' in locals():
                cnx.close()
                print('db연결 해제')
        

        
        #cursor.execute(sql, data)

        #cnx.commit()
        #cnx.close()
    