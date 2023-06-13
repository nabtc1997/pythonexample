from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from config import TOKEN


profile_id = "6183fc9aed92727a706"

gl = GoLogin({
    'token': TOKEN,
    'profile_id': profile_id,
})

if platform == "linux" or platform == "linux2":
    chrome_driver_path = './chromedriver'
elif platform == "darwin":
    chrome_driver_path = './mac/chromedriver'
elif platform == "win32":
    chrome_driver_path = 'chromedriver.exe'

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
time.sleep(3)
gl.stop()
