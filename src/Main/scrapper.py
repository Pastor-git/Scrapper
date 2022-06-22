from pandas import ExcelWriter
from selenium import webdriver
import pandas as panda
import numpy as nump
from selenium.webdriver.common.by import By

excellinput = panda.read_excel ("C:\Python Projects\Scrapper\src\InputExcell\InputData.xlsx")
print (excellinput)

frame = panda.DataFrame(excellinput)
row_number = frame.count()
print(row_number)

# PĘTLA
step = 0
while step < 8:

    website = frame.iat[step,2]
    driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
    driver.get(website)
    # BRAK PRZYPISANIA
    TEST = driver.find_element(By.XPATH, "//*[contains(text(),'@')]")
    print("SELEMIUN ELEMENT: ", TEST)
    mail = str(TEST)
    frame.at[step, 'email'] = mail
    print(frame)
    driver.close()
    driver.quit()
    # instrukcja
    step = step+1


# ZAPIS
frame.to_excel(r'C:\Python Projects\Scrapper\src\OutputExcell\OutputData.xlsx')

#
# website = frame.iat[0,2]
#
# print(website)
# # ------------------------------------------------
# driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver.exe")
# driver.get(website)
#
# mail = driver.find_element(By.XPATH, "//*[contains(text(),'@')]")
#
# print(mail)
#
# # mail = "text"
#
# frame.at[0,'email'] = mail
#
# print(frame)
# # akceptuj wszystko
# # /html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div
#
# # wyszukiwanie
# # /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
#
# # ZAPIS
# frame.to_excel(r'C:\Python Projects\Scrapper\src\OutputExcell\OutputData.xlsx')
#
# # writer = ExcelWriter
# driver.close()
# driver.quit()