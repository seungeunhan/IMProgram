import Sangmi_List_file
import datetime 

class SangMi_Helper:

    # 상미 리스트를 가져옵니다./
    SangmiList = Sangmi_List_file.getSangMiList()

    def imbak_lst_call(self):
        imbak_lst = []

        now = datetime.datetime.now()

        for item in self.SangmiList:
            if 0 < (item[2] - now).total_seconds() < 86400 and item[4] == "사용중":
                imbak_lst.append(item)
        
        return imbak_lst
    
    # 카테고리별로 자른 것을 반환합니다.
    def category_lst_call(self, category):
        

        if category != "All":
            category_lst = [i for i in self.SangmiList if i[-1] == category]
        else: 
            category_lst = self.SangmiList

        imbak_lst = []

        now = datetime.datetime.now()

        for item in category_lst:
            if 0 < (item[2] - now).total_seconds() < 86400 and item[4] == "사용중":
                imbak_lst.append(item)
            else:
                pass
    
        not_imbak_lst = []

        for item in category_lst:
            if 0 < (item[2] - now).total_seconds() < 86400:
                pass
            else:
                not_imbak_lst.append(item)
        
        return imbak_lst, not_imbak_lst


