from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_driver_path = "C:/Users/Timany/Downloads/chromedriver_win32/chromedriver.exe"
s = Service(chrome_driver_path)
#driver = webdriver.Chrome(service = s)
driver = webdriver.Chrome(service = s,options=chrome_options)
#driver = webdriver.Chrome(service = s,options=chrome_options)
driver.get("https://www.amazon.com/dp/B07Q5BZFLB/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B07Q5BZFLB&pd_rd_w=rovDM&content-id=amzn1.sym.eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_p=eb7c1ac5-7c51-4df5-ba34-ca810f1f119a&pf_rd_r=G63QMZ2AT84A9CH32232&pd_rd_wg=nnFSA&pd_rd_r=00751a18-2da9-4199-863e-f4ef557cdbe3&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw")
price = driver.find_element(By.ID, 'productTitle')
print(price.text)
print("WHAT IS GOING ON")

button = driver.find_element(By.NAME, 'submit.add-to-cart')
button.click()
#price = driver.find_element(By.XPATH,'//span[@class="a-price-whole"]')
#print(price.text)
#driver.quit()