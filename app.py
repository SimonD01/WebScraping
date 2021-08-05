import requests
from bs4 import BeautifulSoup as BS

response = requests.get(
    "https://www.fiaformula2.com/Standings/Driver")
soup = BS(response.content, 'html.parser')

standings = soup.select(".driver-name-wrapper")


for drivers in standings:
    driver = drivers.select(".driver-name > .visible-desktop-up")
    num = drivers.select(".pos")
    print(driver[0].text)
    print(num[0].text)
