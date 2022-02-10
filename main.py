from selenium import webdriver
from selenium.webdriver.common.by import By
#настройки вебдрайвера
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('window-size=1400,600')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36')
wd = webdriver.Chrome('chromedriver', options=options)

inp = 'КАЛАМБЕТ АНТОН ОЛЕГОВИЧ'

def parse(inp):
  url = 'https://zhituli.rosfirm.info/rostov'
  wd.get(url)
  fio = wd.find_element(By.NAME, 'fio')
  btn = wd.find_element(By.NAME, 'searchButton')
  if len(inp) > 3:
      fio.send_keys(inp)
      btn.click()
      table = wd.find_element(By.TAG_NAME, 'table')
      return table.text.split('\n')[1:]
