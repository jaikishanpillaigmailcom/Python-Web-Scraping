import csv
from urllib.request import  urlopen
from bs4 import BeautifulSoup

html=urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj=BeautifulSoup(html,'lxml')
table=bsObj.find_all("table",{"class":"wikitable"})[0]
rows=table.find_all("tr")
csvfile=open("editor.csv",'wt',newline='')
w=csv.writer(csvfile)
try:
    for row in rows:
        csvrow=[]
        for cell in row.find_all(['td','th']):
            csvrow.append(cell.get_text())
        w.writerow(csvrow)
finally:
    csvfile.close()
