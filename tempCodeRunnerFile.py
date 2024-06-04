
        self.treeview.heading("#0", text="No",anchor="center")
        for col_lis in column :
            if col_lis=="매출일자" or col_lis=="합계액" or col_lis=="진행상태":
                self.treeview.column(col_lis,width=300,anchor="center")