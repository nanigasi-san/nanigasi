from selenium import webdriver
browser = webdriver.Edge(executable_path='C:/Users/Kaito Yamada/Downloads/MicrosoftWebDriver.exe')
browser.get('https://www.amazon.co.jp')
browser.find_element_by_xpath("//*[@id=\"twotabsearchtextbox\"]").send_keys("Python")

browser.find_element_by_xpath("//*[@id=\"nav-search\"]/form/div[2]/div/input").click()
