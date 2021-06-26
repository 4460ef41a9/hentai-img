from selenium import webdriver #Used selenium because cloudscraper doesnt work with bs4 for some odd reason
from bs4 import BeautifulSoup
from cloudscraper import CloudScraper
import os

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
url = input("Enter the Url: ")
folder = url.split("/")[-2]

def imagedown(url, folder):
  scraper = CloudScraper.create_scraper()
  driver.get(url)
  source = driver.page_source
  soup = BeautifulSoup(source, "html.parser")
  images = soup.find_all("amp-img")
  try:
    os.mkdir(os.path.join(os.getcwd(), folder))
  except:
    pass
  os.chdir(os.path.join(os.getcwd(), folder))
  for image in images:
    link = image["src"]
    name = link.split("/")
    with open(f"{name[-1]}", "wb") as f:
      f.write(scraper.get(f"{link}").content)
      print("Writing: ", name[-1])

imagedown(url, folder)
driver.quit()