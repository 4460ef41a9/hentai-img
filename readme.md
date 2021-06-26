# hentai-img
Image downloader for hentai-img.com and sites related to it

# requirements
* Selenium
* Cloudscraper
* bs4

Or simply do:
```
pip install -r requirements.txt
```

# Usage
1. You will need to download selenium webdriver for your respective browser engine and replace the path to your webdriver at line 6.
```python
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
```
2. Then simply run the with ```py main.py```
3. Make sure the url starts with ```https:\\hentai-img.com\story``` instead of ```https:\\hentai-img.com\image```

# Todo List
- [X] Remove selenium from the script
- [ ] Support for surls with ```https:\\hentai-img.com\image```
- [ ] Tagging downloaded files