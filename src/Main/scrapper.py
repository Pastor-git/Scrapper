from pandas import ExcelWriter
from selenium import webdriver
import pandas as panda
import numpy as nump
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


excellinput = panda.read_excel ("C:\Python Projects\Scrapper\src\InputExcell\InputData.xlsx")
print (excellinput)

frame = panda.DataFrame(excellinput)
row_number = frame.count()
print(row_number)

# PĘTLA
step = 0
while step < 8:

    website = frame.iat[step, 2]
    # driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    # driver.get(website)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")

    # BRAK PRZYPISANIA
    TEST = driver.find_element(By.XPATH, "//*[contains(text(),'@')]")
    print("SELEMIUN ELEMENT: ", TEST)
    mail = str(TEST)
    # WebElement
    element = driver.find_element(By.XPATH, "//*[contains(text(),'@')]").get_attribute("textContent")
    frame.at[step, 'email'] = mail
    print(element)
    print(frame)
    TEST2 = driver.find_elements(By.XPATH, "//*[contains(text(),'window')]")
    if TEST2 is not None:
        frame.at[step, 'window'] = "tak"
    else:
        frame.at[step, 'window'] = "nie"
    print(frame)
    driver.close()
    driver.quit()

    # instrukcja
    step = step+1


# ZAPIS
frame.to_excel(r'C:\Python Projects\Scrapper\src\OutputExcell\OutputData.xlsx')

#
# print(frame)
# # akceptuj wszystko
# # /html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div
#
# # wyszukiwanie
# # /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
#
