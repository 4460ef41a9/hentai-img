from cloudscraper import CloudScraper
from bs4 import BeautifulSoup
import os, warnings, re

url = input("Enter the url: ")
folder = url.split("/")[-2]
warnings.simplefilter("ignore")

def url_change(url):
  url_split = url.split("/")
  url_split[3] = "story"
  return "/".join(str(v) for v in url_split)

def imagedown(url, folder):
  scraper = CloudScraper.create_scraper()
  if url.split("/")[3] == "image":
    url_change(url)
    source = scraper.get(url_change(url)).text
  else:
    source = scraper.get(url).text
  soup = BeautifulSoup(source)
  images = soup.find_all("amp-img")
  try:
    os.mkdir(os.path.join(os.getcwd(), folder))
  except:
    pass
  os.chdir(os.path.join(os.getcwd(), folder))
  for image in images:
    link = image["src"]
    name = link.split("/")
    if re.search(r"jpg|jpeg|png", link.split(".")[-1]):
      with open(f"{name[-1]}", "wb") as f:
        f.write(scraper.get(f"{link}").content)
        print("Writing: ", name[-1])
    else:
      print("This url is not valid!")

imagedown(url, folder)