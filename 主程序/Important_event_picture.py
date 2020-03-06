import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from PIL import Image


url = 'https://api.yimian.xyz/coro'
data = requests.get(url).text

city_dic = {}
json_data = json.loads(data)
for p in json_data:
    if 'cities' in json_data:
        for c in p['cities']:
            city_dic[c['cityName']] = c['currentConfirmedCount']
    else:
        city_dic[p['provinceName']] = p['currentConfirmedCount']

mask = np.array(Image.open('../../练习/Python爬虫/heart.jpg'))
cloud = WordCloud(mask=mask, font_path='msyh.ttc', background_color='white').generate_from_frequencies(frequencies=city_dic)
plt.figure()
plt.axis('off')
plt.imshow(cloud, interpolation="bilinear")
plt.savefig('Important_event_picture.png')


