from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome(executable_path='/mnt/d/github/python_dev/sec20_automation/chromedriver.exe')
print(driver)
driver.get("http://www.python.org")