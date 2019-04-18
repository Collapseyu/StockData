import csv
import re
def financialAndasset():
    csv_file = csv.reader(open('quarterstockFinancial.csv', 'r'))
    stock = []
    for i in csv_file:
        stock.append(i)
    del stock[0]
    # print(len(stock))
    csv_file = csv.reader(open('fincialReportAfter.csv', 'r'))
    report = []
    for i in csv_file:
        report.append(i)
    last = report[0][0]
    tmp = []
    reportAfter = []
    for i in report:
        if i[0] != last:
            reportAfter.append(tmp)
            last = i[0]
            tmp = []
            tmp.append(i)
        else:
            tmp.append(i)
    for i in reportAfter:
        i.sort(key=lambda x: x[1], reverse=False)
    print(reportAfter)
    totalData = [
        ['股票编号', '日期', '日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '换手率', '日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '换手率',
         '流动比率', '速动比率']]
    print(len(totalData[0]))
    for i in reportAfter:
        date = i[0][1]
        for j in i:
            flag = 0
            tmp = []
            for m in stock:
                if m[0] == j[0]:
                    flag = 1
                    if m[1] > date and m[1] <= j[1]:
                        tmp.append([m[1], m[2], m[3], m[4], m[5], m[6], m[7]])
                else:
                    if flag == 1:
                        break
            if tmp != []:
                tmp.sort(key=lambda x: x[0], reverse=False)
                totalTmp = [j[0], j[1]]
                for x in tmp:
                    for a in x:
                        totalTmp.append(a)
                totalTmp.append(j[2])
                totalTmp.append(j[3])
                # print(totalTmp)
                if len(totalTmp) != 18:
                    print(date)
                    date = j[1]
                    continue
                else:
                    totalData.append(totalTmp)
            print(date)
            date = j[1]

    print(totalData)
    return totalData
def save(str,totalData):
    with open(str, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in totalData:
            writer.writerow(row)
        f.close()
def addPriandPro():
    csv_file = csv.reader(open('financialAndratio.csv', 'r'))
    stock = []
    for i in csv_file:
        stock.append(i)
    del stock[0]
    print(stock)
    csv_file = csv.reader(open('reportData_priceAndpro.csv', 'r'))
    price = []
    for i in csv_file:
        price.append(i)
    print(price)
    totalData = [
        ['股票编号', '日期', '日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '换手率', '日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '换手率',
           '基本每股收益','净利率', '流动比率', '速动比率']]
    # [['股票编号','报告日期','日期','收盘价','涨跌幅','换手率','日期','收盘价','涨跌幅','换手率','基本每股收益','流动比率','速动比率']]
    order = []

    for i in price:
        flag = 0
        for j in stock:
            if j[0] == i[0]:
                flag = 1
                if j[1] == i[1]:
                    tmp = []
                    for z in range(16):
                        tmp.append(j[z])
                        # tmp=[j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18],j[19],j[20],j[21],j[22],j[23],j[24],j[25],j[26],j[27],j[28],j[29],j[30],j[31],j[32],j[33],j[34],j[35],j[36],j[37],j[38],j[39],j[40],j[41],j[10],j[11],j[12],j[13],j[14],j[15],i[2],j[-2],j[-1]]
                    tmp.append(i[2])
                    tmp.append(i[3])
                    tmp.append(j[-2])
                    tmp.append(j[-1])
                    totalData.append(tmp)
            else:
                if flag == 1:
                    break
    print(order)
    print(totalData)
    totalData2 = totalData
    totalData3 = []
    tmp = []
    del totalData2[0]
    last = totalData2[0][0]
    for i in totalData2:
        if i[0] != last:
            totalData3.append(tmp)
            last = i[0]
            tmp = []
            tmp.append(i)
        else:
            tmp.append(i)
    print(totalData3)
    for i in totalData3:
        i.sort(key=lambda x: x[1], reverse=False)
    returnData=[]
    for i in totalData3:
        for j in i:
            returnData.append(j)
    return returnData
def addAsset():
    csv_file = csv.reader(open('Datawithoutasset.csv', 'r'))
    stock = []
    for i in csv_file:
        stock.append(i)
    print(stock)
    csv_file1 = csv.reader(open('eastReportasset2.0.csv', 'r'))
    Assert= []
    for i in csv_file1:
        Assert.append(i)
    del Assert[0]
    print(Assert)
    totalData = [
        ['股票编号', '日期', '日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '换手率', '日期', '开盘价', '最高价', '最低价', '收盘价', '涨跌幅', '换手率',
         '基本每股收益', '净利率','流动资产','速动资产','流动负债', '流动比率', '速动比率']]
    for i in Assert:
        flag = 0
        for j in stock:
            if j[0] == i[0]:
                flag = 1
                if j[1] == i[1]:
                    tmp = []
                    for z in range(18):
                        tmp.append(j[z])
                        # tmp=[j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13],j[14],j[15],j[16],j[17],j[18],j[19],j[20],j[21],j[22],j[23],j[24],j[25],j[26],j[27],j[28],j[29],j[30],j[31],j[32],j[33],j[34],j[35],j[36],j[37],j[38],j[39],j[40],j[41],j[10],j[11],j[12],j[13],j[14],j[15],i[2],j[-2],j[-1]]
                    tmp.append(i[3])
                    tmp.append(str(float(i[3])-float(i[2])))
                    tmp.append(i[4])
                    tmp.append(j[-2])
                    tmp.append(j[-1])
                    totalData.append(tmp)
            else:
                if flag == 1:
                    break
    print(totalData)
    totalData2 = totalData
    totalData3 = []
    tmp = []
    del totalData2[0]
    last = totalData2[0][0]
    for i in totalData2:
        if i[0] != last:
            totalData3.append(tmp)
            last = i[0]
            tmp = []
            tmp.append(i)
        else:
            tmp.append(i)
    print(totalData3)
    for i in totalData3:
        i.sort(key=lambda x: x[1], reverse=False)
    returnData = []
    for i in totalData3:
        for j in i:
            returnData.append(j)
    return returnData
def bpDataSet():
    csv_file = csv.reader(open('finalData.csv', 'r'))
    data = []
    for i in csv_file:
        tmp = []
        for j in i:
            tmp.append(j)
        data.append(tmp)
    print(data)
    bpDataWave= []
    bpDatawithoutWave=[]
    for i in range(1,len(data)):
        flag=0
        tmp=[]
        for j in range(23):
            if data[i-1][j]=='' or data[i][j]=='':
                flag=1
                break
        if flag==1:
            break
        tmp.append(data[i-1][0])
        tmp.append(data[i-1][1])
        for z in range(2,21):
            if z==2 or z==9 or z==17:
                continue
            tmp.append(float(data[i - 1][z]))
        tmp.append(float(data[i][-2]))
        tmp.append(float(data[i][-1]))
        if abs(float(data[i-1][17])-float(data[i][17]))>10:
            bpDataWave.append(tmp)
        else:
            bpDatawithoutWave.append(tmp)
    print(bpDataWave)
    return bpDataWave,bpDatawithoutWave
totalData,totalData1=bpDataSet()
save('bpDataWave.csv',totalData)
save('bpDataWithoutWave.csv',totalData1)