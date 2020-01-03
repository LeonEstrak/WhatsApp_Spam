from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# You can replace below path with the absolute path
# to a text file within your computer

file1 = open("MyFile.txt","r")
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Replace '<Name>' with the name of your friend
# or the name of a group
target = '"<Name>"'

while True:
    try:
        x_arg = '//span[@title = '+target+']'
        group_title = driver.find_element_by_xpath(x_arg)
        group_title.click()
        break;
    except Exception as e:
        print(e);
        time.sleep(2);
        continue;

inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)

#Change the MyFile.txt contents to alter the messages

while True:
    for line in file1.readlines():
        actions = ActionChains(driver)
        actions.move_to_element(input_box)
        actions.click().send_keys(line).send_keys(Keys.ENTER). send_keys(Keys.SPACE).perform()
        time.sleep(30)

file1.close()
driver.close()
