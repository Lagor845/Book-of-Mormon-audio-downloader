from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options)
    print("Using Firefox")
except:
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options)
        print("Using Chrome")
    except:
        try:
            options = webdriver.SafariOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Safari(options)
            print("Using Safari")
        except:
            try:
                options = webdriver.EdgeOptions()
                options.add_argument("--start-maximized")
                driver = webdriver.Edge(options)
                print("Using Edge")
            except:
                quit()

urls = ["https://www.churchofjesuschrist.org/study/scriptures/dc-testament?lang=eng","https://www.churchofjesuschrist.org/study/scriptures/nt?lang=eng","https://www.churchofjesuschrist.org/study/scriptures/ot?lang=eng","https://www.churchofjesuschrist.org/study/scriptures/bofm?lang=eng","https://www.churchofjesuschrist.org/study/scriptures/pgp?lang=eng"]

with open("config","r") as file:
    data = file.read()
    string = data.split("\n")
    string = string[-1].split(":")
    option = urls[int(string[1].strip(" "))-1]

with open("links.txt","w") as file:
    file.write("")

driver.get(option)

first = True
while True:
    if len(driver.current_url.split("/")) == 8:

        try:
            driver.find_element(By.CSS_SELECTOR,".button-DWtvB[class]").click()
        except:
            pass
        try:
            driver.find_elements(By.CSS_SELECTOR,".cOOPXM")[2].click()
            driver.implicitly_wait(0.2)
            link = driver.find_elements(By.CSS_SELECTOR,".elLczx")[1].get_attribute('href')
            with open("links.txt","a") as file:
                file.write(link + "\n")
        except:
            pass
        try:
            driver.find_elements(By.CSS_SELECTOR,".dwNsNv")[1].click()
        except:
            break
    
    else:
        if first != True:
            try:
                try:
                    try:
                        driver.find_element(By.CSS_SELECTOR,".button-DWtvB[class]").click()
                    except:
                        pass
                    driver.find_elements(By.CSS_SELECTOR,".cOOPXM")[2].click()
                    link = driver.find_elements(By.CSS_SELECTOR,".elLczx")[1].get_attribute('href')
                    with open("links.txt","a") as file:
                        file.write(link + "\n")
                except:
                    pass
                driver.find_elements(By.CSS_SELECTOR,".dwNsNv")[1].click()
            except:
                break
        else:
            driver.find_elements(By.CSS_SELECTOR,".dwNsNv")[0].click()
            first = False

print("Finished")
driver.quit()