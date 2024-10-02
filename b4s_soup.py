import pandas as pd
import requests
from bs4 import BeautifulSoup
web_link = 'https://www.satellite-calculations.com/Satellite/satellitelist.php?AMATEURALLNEAR'
link_get = requests.get(web_link)
web_html = link_get.content
soup = BeautifulSoup (web_html, 'html.parser')
data = soup.find('table', id='main')


heads = []
headers = data.find_all('th')

for th in headers:
    th_txt = th.text
    heads.append(th_txt)
    
    
td_list = []
all_tr = data.find_all('tr')
for tr in all_tr:
    all_td = tr.find_all('td')
    for td in all_td:
        td_txt=td.text
        td_list.append(td_txt)
dat = []
df = pd.DataFrame(dat)

df.to_excel('python_b4s.xlsx', index=False)
 
print("Data has been exported to 'python_b4s.xlsx'.")
