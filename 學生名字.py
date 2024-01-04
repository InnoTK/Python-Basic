姓名 = ['林冠宇','方家綺','楊詠寶','鄧廷琬','林依臻',
      '盧法豐','李邦軒','李思禾','張沛然','朱宇雄',
      '鄭雅雯','張宏偉','張莉雯','林信明']
學號 = []
for n in range(1,15):
    學號.append('{:03}'.format(n))
print(學號)
# end_string = input("請輸入您想要的結束數字字串(如035)： ")
# end_number = int(end_string)
# 學號 = [str(i).zfill(len(end_string)) for i in range(1, end_number+1)]
# print(學號)