import requests
import demjson
import re
from bs4 import BeautifulSoup
import pymysql

def getInfo(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Host': 'ccclub.cmbchina.com',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
    response = requests.get(url=url,headers=headers).text
    soap = BeautifulSoup(response, 'lxml').prettify()
    regName = re.compile('''<a href="(.*?)" onclick=".*?" target="_blank">
             <img alt="(.*?)" border="0" height="80" src="(.*?)"''')
    regNumber = re.compile(r'共(\d+)条，转到第<input type="text" id="uc_page_goPage" value="" />页/(\d+)页</div>')
    number = re.findall(regNumber,response)[0][1]
    cardinfo = re.findall(regName,soap)
    return [number,cardinfo]

connection= pymysql.connect(host="127.0.0.1",user="root",
    password="941208",db="creditcard",port=3306,charset='utf8')



#info = {'infoNum':number[0][0],"pages":number[0][1],'pagecount':1,'cardInfo':cardinfo}
url1 = 'http://ccclub.cmbchina.com/ccproduct/cardlist.aspx'
mainInfo = getInfo(url1)
#print(mainInfo)
number = int(mainInfo[0])
print(number)
x=0
for i in range(1,number):
    with connection.cursor() as cursor:
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        print('第{}页'.format(i))
        url = r'http://ccclub.cmbchina.com/ccproduct/cardlist.aspx?PageNo={}'.format(i)
        cardInfo = getInfo(url)[1]
        for info in cardInfo:
            #print(info)
            cursor.execute("SELECT * FROM mycreditcard_zsyh_apply")
            print('x=',x)

            if info[0][0]=='.':
                #print(info)
                c = 'http://ccclub.cmbchina.com/ccproduct/{}'.format(info[0][2:])
                infomate = (x, c, info[1], info[2])
            else:
                infomate = (x,info[0],info[1],info[2])
            cursor.execute("INSERT INTO mycreditcard_zsyh_apply (id,card_address,card_name,pic_address) VALUES (%s,%s,%s, %s)",infomate)
            x+=1
        connection.commit()
