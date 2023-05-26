from selenium import webdriver
from selenium.webdriver.common.by import By


def get_madata():
    driver = webdriver.Chrome()

    driver.get("https://hello.iitk.ac.in/index.php/user/login")

    title = driver.title
    driver.implicitly_wait(0.5)

    logid = driver.find_element(by=By.ID, value="edit-name")
    pawd = driver.find_element(by=By.ID, value="edit-pass")
    subbt = driver.find_element(by=By.ID, value="edit-submit")
    
    logid.send_keys("ggg")
    pawd.send_keys("kkk")
                                
    subbt.click()
    gg = driver.find_element_by_xpath('//a[@href="https://hello.iitk.ac.in/mth114m2223s2/"]')
    gg.click()

    while(True):
       pass


get_madata()