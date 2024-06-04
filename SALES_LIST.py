import mysql.connector

class SALES_LIST:
    #Sales 데이터 다 가져오는부분
    def get_Data(self):
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
                query = "SELECT * FROM SALES"
                cursor.execute(query)
                result = cursor.fetchall()


        except mysql.connector.Error as e:
            print('MYSQL 데이터베이스 연결 오류 발생')
        finally:
            if 'connection' in locals():
                cnx.close()
                print('db연결 해제')
        return result

