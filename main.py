import pandas as pd
import colorama

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from datetime import datetime
from colorama import Fore

colorama.init(autoreset=True)

now = datetime.now()
thedate = now.strftime("-%m_%d_%Y")

url = "https://www.thesun.co.uk/sport/football/"
path = "chromedriver.exe"

options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
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

file = f"ftbl_headlines{thedate}.csv"

df_headline = pd.DataFrame(csv_dict)
df_headline.to_csv(file)

print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Successfully extracted the news source! Outputted the data in {Fore.LIGHTGREEN_EX + file}")

driver.quit()
