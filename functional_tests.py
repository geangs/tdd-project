from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox( options=options)
browser.get('http://localhost:8000')

assert 'To-Do' in browser.title

broswer.quit