from ORDER_LIST import ORDER_LIST
from datetime import date

class Order_Helper:
    #Check means 전체조회
    def Data_Check(self):
        ol = ORDER_LIST()
        result = ol.get_Order_Data()
        return result
    def Product_Check(self):
        ol = ORDER_LIST()
        result = ol.get_Product_data()
        return result
    def Inventory_Check(self):
        ol = ORDER_LIST()
        data = ol.get_inventory_data()

        # get_inventory_data에서 가지고 온 것 중, 튜플의 두번째 요소가 5이하만 result로 줍니다.
        result = []
        for d in data:
            if d[1] <= 5 : result.append(d)
        print(result)
        return result
    
    # 데이터 포멧 맞춰서 올려줌
    def Order_Appand(self,product_data):
        self.product_data = product_data
        values = [value for sublist in self.product_data for value in sublist]
        appand_data = []
        quantity = int(values[1]) * int(values[2])
        values.append(quantity)
        values.append('진행대기')
        today = date.today()
        appand_data.append(values[0])
        appand_data.append(today)
        appand_data.append(int(values[1]))
        appand_data.append(values[2])
        appand_data.append(quantity)
        appand_data.append('진행대기')
        
        appand_data = tuple(appand_data)
        print(appand_data)
        ol = ORDER_LIST()
        ol.reg_Order_Data(appand_data)


    def Order_format_n_reg(self, data):
        p_name = data[0]
        o_date = date.today()
        o_cost = data[2]
        o_count = 5
        o_quan = o_cost*o_count
        o_state = "진행대기"
        Toappend = (p_name, o_date, o_cost, o_count, o_quan, o_state)

        ol = ORDER_LIST
        
        # reg_order_data가 왜 self를 인자로 가지나욤?!
        ol.reg_Order_Data(self, Toappend)
        print(Toappend)