import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def inputPandaCode(code):
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.pandaguestexperience.com")
    
    codeList = code.split("-")

    for i in range(1, 7):
        element = driver.find_element_by_name("CN"+str(i))
        print(codeList[i-1])
        element.send_keys(codeList[i-1])

    try:
        link = driver.find_element_by_id("NextButton")
        link.click()
    except selenium.common.exceptions.NoSuchElementException:
        print('Wrong survey code')
        driver.quit()

def fillSurvey():
    nextButton = driver.find_elements_by_id("NextButton")
    while len(nextButton) != 0:
        optionButton = driver.find_elements_by_class_name("radioSimpleInput")
        for i in range(0, len(optionButton), 5):
            optionButton[i].click()
        nextButton = driver.find_elements_by_id("NextButton")
        if len(nextButton) == 0:
            break
        nextButton[0].click()

def main():
    code = input("Give survey code with '-' in between\n")
    inputPandaCode(code)
    fillSurvey()
    

if __name__ == "__main__":
    main()
