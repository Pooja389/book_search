from flask import render_template,Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

driver = webdriver.Chrome()
all_combined_results = []
intersested_searches = ["pencil heel","navy blue shirt","earings","top for girls"]

for search in intersested_searches:

    driver.get(f"https://www.flipkart.com/search?q={search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

    name_list = []
    products_name = driver.find_elements(By.CLASS_NAME,value="WKTcLC")
    for i in range(5):
        name = products_name[i].text
        name_list.append(name)
         
    price_list = []    
    products_price = driver.find_elements(By.CLASS_NAME,value = "Nx9bqj")
    for i in range(5):
        price = products_price[i].text
        price_list.append(price)

    
    img_list = []
    products_img = driver.find_elements(By.CLASS_NAME,value = "_53J4C-")
    for i in range(5):
        img_url = products_img[i].get_attribute("src")
        img_list.append(img_url)
 
    
    combined_list = list(zip(name_list, price_list, img_list))
    all_combined_results.extend(combined_list)


    time.sleep(2)


input("press enter to leave :")
driver.quit()

@app.route("/")
def home():
    return render_template("index.html",list = all_combined_results)

if __name__ == "__main__":
    app.run(debug=False)