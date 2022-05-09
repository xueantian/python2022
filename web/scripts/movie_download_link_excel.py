
import requests
import re
import openpyxl
from openpyxl.styles import Font,Alignment,Side,Border

url='https://www.dytt8.net/html/gndy/jddy/20160320/50523.html' # IMDB评分8分左右影片500多部
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
resp=requests.get(url)
resp.encoding='gb2312'
#print(resp.text)

#To get the page link for each movie
obj1=re.compile(r"<p><strong>.*?<a href=\"(?P<page_link>https://.*?)\">",re.S)
result1=obj1.finditer(resp.text)

# RE To find the download link and movie name of each movie
obj2=re.compile(r"href=\"(?P<download_link>magnet:.*?)\"><strong><font",re.S)
obj3=re.compile(r"<title>(?P<movie_name>.*?)</title>",re.S)

# create a excel file
workbook=openpyxl.Workbook()
sheet=workbook.active

#set the excel
font=Font(name='Calibri',size=12,bold=True,color='ff0000')
font2=Font(name='Calibri',size=10,bold=True,color='ff0000')
alignment=Alignment(horizontal='center',vertical='center',wrap_text=True)
side=Side(style='thin',color='000000')
border=Border(left=side,right=side,top=side,bottom=side)

#Set the A1, and B1 for Title
sheet['A1'].value='电影名称'
sheet['B1'].value='电影下载地址'
sheet.row_dimensions[1].height = 25.8
sheet['A1'].font=font
sheet['B1'].font=font
sheet['A1'].alignment=alignment
sheet['B1'].alignment=alignment
sheet.column_dimensions['A'].width = 80
sheet.column_dimensions['B'].width = 200
#put the download link and movie name to 数组
download_links=[]
movie_names=[]
i=0
lst=[]
for it in result1:
    url2=it.group('page_link')

    # to access the page of each movie
    resp2=requests.get(url2,headers=headers)
    resp2.encoding = 'gb2312'
    #print(resp2.text)

    # To find the download link and movie name of each movie
    result2 = obj2.finditer(resp2.text)
    result3=obj3.finditer(resp2.text)
    for ittt in result3:
        movie_names.append(ittt.group('movie_name'))
        #print(movie_names)

    for itt in result2:
        download_links.append(itt.group('download_link'))
        #print(download_links)



#    final_list=dict(zip(movie_names,download_links))


    print('第 {} 个电影的下载地址'.format(i+1))
    print(url2)
    print(movie_names[i])
    print(download_links[i])
    i+=1

# put the movie name and download link to excel file
a=2
for item in movie_names:
    sheet['A{}'.format(a)].value = item
    sheet['B{}'.format(a)].value = download_links[a-2]
    a+=1


# to save the excel file
workbook.save('movie_download_link.xlsx')







