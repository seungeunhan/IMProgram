import Inventory_List
import datetime

class InventoryHelper:
    
    InventoryList=Inventory_List.getInventoryList()
    notImmList=[]
    ImmList=[]

    # 날짜 입력 > 남은 기간(일단위) 출력
    def DateCalculate(self,End):
        state = 0
        End =datetime.datetime.strptime(End,'%Y-%m-%d')
        today = datetime.datetime.now()

        state=(End-today).days

        return state

    def getInventoryList(self,category):

        state=0
        tempList=[]
        temp2ImmList=[]
        notImmList=[]
        ImmList=[]

        #전체 카테고리가 아니라면 임박아님 제품리스트에 추가
        if category != 'All':
            for Listslice in self.InventoryList:
                if Listslice[0]==category:
                    tempList.append(Listslice)
        else: #전체 카테고리면 전체 정보
            tempList=self.InventoryList

        # 카테고리 자르고 저장
        for Listslice in tempList:
            temp2ImmList.append(Listslice[1:5])

        for Listslice in temp2ImmList:
            if self.DateCalculate(str(Listslice[3])) <= 7:
                ImmList.append(Listslice)
            else:
                notImmList.append(Listslice)

        return ImmList,notImmList

    def UpdateInventory(InvenList):

        return

    def DelInventroy(InvenList):


        return

    def SearchInventroy():


        return

    def DateSearchResult(date):

        resultList=[]
        return resultList

    def NameSearchResult(Name):
        resultList=[]

        return resultList

    def Sort_AscenDing():

        return

