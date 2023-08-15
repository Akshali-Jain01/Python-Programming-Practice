import requests,json
url="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=8bc7c6a4ca1a42b2a973cebd279768d4"
ans= requests.get(url).text
print(ans)
ans_dict=json.loads(ans)
print(ans_dict)
arts = ans_dict['articles']

for article in arts:
    print(article['title'])

