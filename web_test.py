# -*- coding: utf-8 -*-


from selenium import webdriver
import time


driver = webdriver.Chrome('D:\\Data\\shared\\script\\python\\SCB\\webdriver\\chrome\\v80\\chromedriver.exe')
driver.maximize_window()
url = "https://www.douban.com/"
driver.get(url)
driver.find_element_by_class_name('lnk-movie').click()
elements = driver.find_elements_by_tag_name('a')

for element in elements:
    if '排行榜' in element.text:
        element.click()

        elements2 = driver.find_elements_by_tag_name('a')
        for element2 in elements2:
            if '喜剧' in element2.text:
                element2.click()

#time.sleep(3)
#driver.quit()


'''
driver = webdriver.Ie('D:\\Data\\shared\\script\\python\\SCB\\webdriver\\IE\\IEDriverServer.exe')
driver.maximize_window()
url = "https://www.douban.com/"
driver.get(url)
driver.find_element_by_class_name('lnk-movie').click()
'''

'''
#xpath
driver = webdriver.Chrome('D:\\Data\\shared\\script\\python\\SCB\\webdriver\\chrome\\v80\\chromedriver.exe')
driver.maximize_window()
url = "https://www.douban.com/"
driver.get(url)
driver.find_element_by_xpath("//a[@class='lnk-movie']").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath("//div[@id='db-nav-movie']//li[4]//a[1]").click()
#driver.switch_to.window(driver.window_handles[2])
time.sleep(2)
driver.find_element_by_xpath("//div[@id='db-nav-movie']//li[7]//a[1]").click()
'''