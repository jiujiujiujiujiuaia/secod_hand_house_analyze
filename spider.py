import requests
import xlrd as xlrd
from xlutils.copy import copy
from lxml import etree
import xlwt as xlwt
import os
import datetime
import re

def getData():

    b = ['建发独墅湾']
    script_dir = os.path.dirname(os.path.abspath(__file__))
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime('%Y%m%d_%H%M%S')
    file_name = 'beike'
    timestamped_filename = f'{file_name}_{timestamp}.xls'
    file_path = os.path.join(script_dir, timestamped_filename)
    for b_1 in b:
        for page in range(1,7):
            url = f'https://su.ke.com/chengjiao/pg{page}rs{b_1}/'

            h = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.9 Safari/537.36',
            'Cookie': ''}


            res = requests.get(url,headers=h)


            xp = etree.HTML(res.text)

            list_l = xp.xpath('//ul[@class="listContent"]/li')

            datalist=[]
            pattern = r'\d+'            
            for na in list_l:
                titles = na.xpath('.//div[@class="title"]/a/text()')[0]#.replace(' ','')
                title = titles.split()
                communityName = title[0]
                layout = title[1]
                areas = title[2]
                matchArea = re.findall(pattern, areas)
                area = matchArea[0]



                houseInfos = na.xpath('.//div[@class="houseInfo"]/text()')[1].strip()#.replace(' ','')
                houseInfo = houseInfos.split(" | ")
                orientation = houseInfo[0]
                type = houseInfo[1]

                dealDate = na.xpath('.//div[@class="dealDate"]/text()')[0].strip()
                totalPrice = na.xpath('.//div[@class="totalPrice"]/span/text()')[0]

                positionInfos = na.xpath('.//div[@class="positionInfo"]/text()')[1].strip()
                positionInfo = positionInfos.split()
                floorInfo = positionInfo[0]
                buildingType = positionInfo[1]
                floorParts = floorInfo.split("(")
                floorType = floorParts[0]
                totalFloors = floorParts[1].strip(")")
                matchTotalFloors = re.findall(pattern, totalFloors)
                totalFloor = matchTotalFloors[0]


                unitPrice = na.xpath('.//div[@class="unitPrice"]/span/text()')[0]

                dealCycleTxts = na.xpath('.//span[@class="dealCycleTxt"]/span/text()')[0]
                matchDealCycleTxt = re.findall(pattern, dealCycleTxts)
                price = matchDealCycleTxt[0] 

                periods = na.xpath('.//span[@class="dealCycleTxt"]/span/text()')[1]
                matchPeriod = re.findall(pattern, periods)
                period = matchPeriod[0]

                house = [communityName,layout,area,orientation,type,dealDate,totalPrice,buildingType,floorType,totalFloor,unitPrice,price,period]
                datalist.append(house)

            index = len(datalist)
            # 检查文件是否已存在，如果不存在则创建新文件
            if not os.path.exists(file_path):
                header = ["小区名","户型结构","总面积","朝向","房屋类型","成交日期","成交价格","建筑类型","楼层类型","总楼层","单价","挂牌价格","交易周期"]
                datalist.insert(0,header)
                workbook = xlwt.Workbook()
                worksheet = workbook.add_sheet('Sheet1')
                rows_old = 0
                for i in range(0, index):
                    for j in range(0, len(datalist[i])):
                        worksheet.write(i + rows_old, j, datalist[i][j])
                workbook.save(file_path)
            else:
            # 打开已存在的文件
                workbook = xlrd.open_workbook(file_path)
                worksheet = workbook.sheet_by_index(0)
                rows_old = worksheet.nrows
              # 获取表格中已存在的数据的行数
                new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
                new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
                for i in range(0, index):
                    for j in range(0, len(datalist[i])):
                        new_worksheet.write(i + rows_old, j, datalist[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
                new_workbook.save(file_path)  # 保存工作簿
            print(f"第{page}页写入成功")

if __name__ == '__main__':
    getData()

