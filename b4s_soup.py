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
# for tr in all_tr:
#     all_td = tr.find_all('td')
#     for td in all_td:
#         td_txt=td.text
#         td_list.append(td_txt)
# dat = []
# dat.append(heads)
# dat.append(td_list)



filtered_data = []
collect = False


for tr in all_tr:
    all_td = tr.find_all('td')
    if len(all_td) > 2:
        
        first_td = all_td[2].text.strip()
   
        if first_td == "EXPRESS-AM7":
            collect = True
            
        if collect:
            row = []
            for i in [0, 1, 2, 3, 4, 13, 21, 30]:
                row.append(all_td[i].text.strip())
            filtered_data.append(row)
            
        if first_td == 'EUTELSAT 36B':
            break
        
headers_selected = []

for i in [0, 1, 2, 3, 4, 13, 21, 30]:
        headers_selected.append(heads[i])

df = pd.DataFrame(filtered_data, columns=headers_selected)

excel = df.to_excel('python_b4s.xlsx')

print('done')