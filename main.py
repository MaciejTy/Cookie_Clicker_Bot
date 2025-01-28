from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def check_prices():
    money = float(driver.find_element(By.ID, value="money").text.replace(",", ""))

    time_machine = driver.find_element(By.ID, value="buyTime machine").text.split()
    time_machine_price = int((time_machine[3]).replace(",", ""))
    time_machine_button = driver.find_element(By.ID, value="buyTime machine")

    portal = driver.find_element(By.ID, "buyPortal").text.split()
    portal_price = int((portal[2]).replace(",", ""))
    portal_button = driver.find_element(By.ID, "buyPortal")

    alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab").text.split()
    alchemy_lab_price = int((alchemy_lab[3]).replace(",", ""))
    alchemy_lab_button = driver.find_element(By.ID, "buyAlchemy lab")

    shipment = driver.find_element(By.ID, "buyShipment").text.split()
    shipment_price = int((shipment[2]).replace(",", ""))
    shipment_button = driver.find_element(By.ID, "buyShipment")

    mine = driver.find_element(By.ID, "buyMine").text.split()
    mine_price = int((mine[2]).replace(",", ""))
    mine_button = driver.find_element(By.ID, "buyMine")

    factory = driver.find_element(By.ID, "buyFactory").text.split()
    factory_price = int((factory[2]).replace(",", ""))
    factory_button = driver.find_element(By.ID, "buyFactory")

    grandma = driver.find_element(By.ID, "buyGrandma").text.split()
    grandma_price = int((grandma[2]).replace(",", ""))
    grandma_button = driver.find_element(By.ID, "buyGrandma")

    cursor = driver.find_element(By.ID, "buyCursor").text.split()
    cursor_price = int((cursor[2]).replace(",", ""))
    cursor_button = driver.find_element(By.ID, "buyCursor")

    if money > time_machine_price:
        time_machine_button.click()
    elif money > portal_price:
        portal_button.click()
    elif money > alchemy_lab_price:
        alchemy_lab_button.click()
    elif money > shipment_price:
        shipment_button.click()
    elif money > mine_price:
        mine_button.click()
    elif money > factory_price:
        factory_button.click()
    elif money > grandma_price:
        grandma_button.click()
    elif money > cursor_price:
        cursor_button.click()


clicker = driver.find_element(By.ID, value="cookie")

while True:
    clicker.click()
    if int(time.time()) % 5 == 0:
        check_prices()

