from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

url = "https://www.thesun.co.uk/sport/football/"
path = "chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(url)

containers = driver.find_elements(by="xpath", value="//div[@class='teaser__copy-container']")

titles = []
subtitles = []
links = []

for container in containers:

    # getting elements
    title = container.find_element(by="xpath", value="./a/h2").text # title
    subtitle = container.find_element(by="xpath", value="./a/p").text # subtitle
    link = container.find_element(by="xpath", value="./a").get_attribute("href") # subtitle

    # appending elements
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

csv_dict = {"Title":titles,
           "Subtitle":subtitles,
           "Link":links}

df_headline = pd.DataFrame(csv_dict)
df_headline.to_csv("ftbl_headlines.csv")

driver.quit()
