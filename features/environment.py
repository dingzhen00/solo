from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.implicitly_wait(5)
    context.base_url = 'https://jaguardanube-normalslalom-8000.codio-box.uk/'

def after_all(context):
    context.browser.quit()
