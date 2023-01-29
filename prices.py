from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from tabulate import tabulate
#URL to your X-KOM list
URL = 'https://www.x-kom.pl/lista/39ml4sp6k'
def pricecheck(url):
    item_names = []
    item_prices = []
    driver = webdriver.Chrome (executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    # maximize with maximize_window()
    driver.maximize_window()
    driver.get(url)
    # iterate through list and get text
    name = driver.find_elements(By.CLASS_NAME, "sc-1yjqabt-8")
    price = driver.find_elements(By.CLASS_NAME, "iripud")
    if len(name) > 0 and len(price) > 0:
        for i in range(min(len(name), len(price))):
            item_names.append(name[i].text)
            item_prices.append(price[i].text)
    else:
        print("No elements found.")
    driver.close()
    df = pd.DataFrame({'item_name': item_names, 'item_price': item_prices})

    return df
print(tabulate(pricecheck(URL), headers='keys', tablefmt='psql'))
