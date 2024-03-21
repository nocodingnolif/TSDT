from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options, executable_path="E:/xuexi/firefox/geckodriver.exe")
driver.get("https://localhost：8000")
assert 'Django' in browser.page_source
