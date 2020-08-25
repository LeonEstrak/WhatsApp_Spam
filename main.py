from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# You can replace below path with the absolute path
# to a text file within your computer

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Replace '<Name>' with the name of your friend
# or the name of a group
target = '"<Name>"'

# This is the interval of time after which each message will be sent
waitTime = 2

# If the recipient of the messages sends the safeWord then the infinite loop
# of sending the messages will be terminated
safeWord = "Stop"

while True:
    try:
        x_arg = "//span[@title = " + target + "]"
        group_title = driver.find_element_by_xpath(x_arg)
        group_title.click()
        break
    except Exception as e:
        print(e)
        time.sleep(2)
        continue

inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)

while True:
    # Change the MyFile.txt contents to alter the messages
    file1 = open("MyFile.txt", "r")
    for line in file1.readlines():
        actions = ActionChains(driver)
        actions.move_to_element(input_box)
        actions.click().send_keys(line).send_keys(Keys.ENTER).send_keys(
            Keys.SPACE
        ).perform()
        time.sleep(waitTime)
    file1.close()
    check_box = driver.find_elements_by_class_name("eRacY")
    if check_box[len(check_box) - 1].text == safeWord:
        break

driver.close()
