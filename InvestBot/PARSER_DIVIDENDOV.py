
import requests
from bs4 import BeautifulSoup
import pandas as pd
def DIV_DAY_PLZ(a):

        url = f'https://smart-lab.ru/q/{a}/dividend/'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        trs = soup.find('div', style="display: inline-block; margin-left: 15px").find_all('td')
        if trs == []:
            return []
        else:


            trs = str(trs)
            trs = trs.replace("</strong>",'')
            trs = trs.replace("<strong>",'')
            trs = trs.replace("<",'')
            trs = trs.replace(">",'')
            trs = trs.replace("/",'')



            trs = trs.split('td')
            trs.pop(0)


            try:
             trs.pop(len(trs)-1)
            except:
               pass
            for i in range(0,len(trs)):
               try:
                  if trs[i] == ', ':
                   try:
                       trs.remove(', ')
                   except:
                        pass
               except:
                   pass

            if trs[0]==a or trs[0] == a+'P':
             trs.pop(8)
            else:
                trs.pop(0)
            return trs