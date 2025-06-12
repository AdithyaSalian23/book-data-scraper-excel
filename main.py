from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")

wb = Workbook()
ws = wb.active
ws.append(["Title", "Price"])  

books = driver.find_elements(By.CLASS_NAME, "product_pod")
for book in books:
    title = book.find_element(By.TAG_NAME, "h3").text
    price = book.find_element(By.CLASS_NAME, "price_color").text
    ws.append([title, price])

wb.save("books.xlsx")
print("✅ Data saved to books.xlsx")

time.sleep(5)
driver.quit()