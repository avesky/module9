import requests
import bs4

url = 'https://www.dmacc.edu/about/Pages/welcome.aspx'
response = requests.get(url)
html = response.content
f = open("request_result.txt", "w+")
f.writelines(str(html))
f.close()

soup = bs4.BeautifulSoup(open("request_result.txt"), 'html.parser')
print(soup.prettify())
