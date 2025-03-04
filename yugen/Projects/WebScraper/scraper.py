import requests
import random
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://pixelford.com/blog'
rand_num = random.randint(1,100000)

# print(requests.get(url=url, headers={'user-agent' : f'Hello {rand_num}'}))
response = requests.get(url=url, headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})

html = response.content
soup = BeautifulSoup(html, 'html.parser')

# a_tags = soup.find_all('a', class_ = 'entry-title-link')
# time_tags = soup.find_all('time', class_ = 'entry-time')
# for tag in a_tags:
#     pprint(tag.get_text())

# ------------------------------------------
# Challenge: Get the text of all the a relevant a tags using map function

# titles = list(map(lambda tag : tag.get_text(), a_tags))
# post_times = list(map(lambda tag : tag.get_text(), time_tags))
blogs = soup.find_all('article', class_ = 'type-post')

# for blog in blogs:
#     post_title = blog.find('a', class_ = 'entry-title-link').get_text()
#     post_dt = blog.find('time', class_ = 'entry-time').get('datetime')
#     post_content = blog.find('div', class_ = 'entry-content').find('p').get_text()

data = list(map(lambda blog : {
            'post_title' : blog.find('a', class_ = 'entry-title-link').get_text(),
            'post_dt' : blog.find('time', class_ = 'entry-time').get('datetime'),
            'post_content' :blog.find('div', class_ = 'entry-content').find('p').get_text()
            }, blogs
            )
        )

pprint(data)
