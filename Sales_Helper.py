from SALES_LIST import SALES_LIST


class Sales_Helper:
    
    def Check_Sales():
        sa = SALES_LIST()
        result = sa.get_Data()
        return result


