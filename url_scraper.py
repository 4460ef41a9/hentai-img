from cloudscraper import CloudScraper
from bs4 import BeautifulSoup
from re import search as rsearch
from shutil import rmtree, move
import os, zipfile

url = input("Enter the url: ")
folder = url.split("/")[-2]
basedir = os.getcwd()

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
  soup = BeautifulSoup(source, "lxml")
  images = soup.find_all("amp-img")
  try:
    os.mkdir(os.path.join(os.getcwd(), folder))
  except:
    pass
  os.chdir(os.path.join(os.getcwd(), folder))
  for image in images:
    link = image["src"]
    name = link.split("/")
    if rsearch(r"jpg|jpeg|png", link.split(".")[-1]):
      with open(f"{name[-1]}", "wb") as f:
        f.write(scraper.get(f"{link}").content)
        print("Writing: ", name[-1])
    else:
      print("This url is not valid!")

def prepare_zip(folder):
  os.chdir(basedir)
  new_file = folder + '.cbz'
  zipf = zipfile.ZipFile(new_file, 'w', zipfile.ZIP_DEFLATED)
  for dir_path, dir_names, files in os.walk(folder):
    f_path = dir_path.replace(dir_path, '')
    f_path = f_path and f_path + os.sep
    for file in files:
      zipf.write(os.path.join(dir_path, file), f_path + file)
  zipf.close()
  print("File Created successfully..")
  return new_file

def move_dls(folder):
  os.chdir(basedir)
  try:
    os.chdir("Downloads")
  except FileNotFoundError:
    os.mkdir("Downloads")
    os.chdir("Downloads")
  move(basedir + "/" + folder+ ".cbz", basedir + "/Downloads")
  rmtree(os.path.join(basedir, folder))
  
imagedown(url, folder)
prepare_zip(folder)
move_dls(folder)