import re
import time
from glob import glob

import pandas as pd

cid_to_cat = {
    '1': 'Novel_Poem',
    '170': 'Economic_Management',
    '1230': 'Home_Cook_Beauty',
    '1237': 'Religion_Mysticism',
    '517': 'Art_Culture',
    '55890': 'Health_Hobby_Leisure',
    '987': 'Science',
    '76001' : 'reference_book',
}
today = time.strftime("%Y-%m-%d", time.localtime(time.time()))

filenames = glob('./crawling_data/*.csv')
get_cid = re.compile('cid-[0-9]+')
datas = []

for filename in filenames:
    if today in filename:
        print(filename)
        cid = get_cid.search(filename).group()[4:]
        df = pd.read_csv(filename)
        df['category'] = cid_to_cat[cid]
        datas.append(df)

data = pd.concat(datas, ignore_index=True)

print(data.head())
print(data.shape)
print(data['title'].unique().shape)

data.to_csv(f'./data/raw_{len(data)}_{today}.csv', index=False)