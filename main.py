from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from time import sleep

#      _______________________________________________________________
#     / Replace the sites underneath with the sites you want to use  /
#    /______________________________________________________________/ 

SITES = '''
https://www.youtube.com/watch?v=rPwvR_Mvrck&ab_channel=TF1INFO
https://writtenrealms.com/
https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal
https://www.canada.ca/fr/sante-canada/services/publications/vie-saine/comment-preparer-fumee-feux-foret.html
'''.split('\n')

driver = webdriver.Chrome()

def get_element_safely(by, content, time=5, ec=EC.element_to_be_clickable, ignored_exceptions=StaleElementReferenceException):
    return WebDriverWait(driver, time, ignored_exceptions=ignored_exceptions).until(ec((by, content)))

def click_search_button():
    for i in get_element_safely(By.CLASS_NAME, 'material-icons', ec=EC.presence_of_all_elements_located)[::-1]:
        if i.text == 'search':
            search_button = i
            search_button.click()
            break

driver.get('https://www.mybib.com/')
print(driver.title)

first_x = get_element_safely(By.CLASS_NAME, 'material-icons')
first_x.click()

for site in SITES:
    if not site:
        continue

    try:
        get_element_safely(By.CLASS_NAME, 'mu-raised-button-wrapper').click()
    except ElementClickInterceptedException:
        print('Retrying + Add Citation')
        driver.implicitly_wait(5)
        get_element_safely(By.CLASS_NAME, 'mu-raised-button-wrapper').click()
    
    search = get_element_safely(By.CLASS_NAME, 'rounded-l-sm')
    search.send_keys(site)

    try:
        click_search_button()
    except ElementClickInterceptedException:
        driver.implicitly_wait(5)
        click_search_button()

    # site = driver.find_element(By.CLASS_NAME, 'flex.py-4.px-5.text-left.w-full')
    site = get_element_safely(By.CLASS_NAME, 'flex.py-4.px-5.text-left.w-full', time=10)
    site.click()

    for i in range(3):
        driver.implicitly_wait(3)
        try:
            no_element = get_element_safely(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/button[1]', time=2)
        except TimeoutException:
            break
        else:
            no_element.click()

    elements = get_element_safely(By.XPATH, '/html/body/div[3]/div/div/div/div[3]/button')
    #     try:
    # for e in elements:
    #         print(e.text)
    #     except StaleElementReferenceException:
    #         print('stale element')
    print(elements)
    # input('Save button click > ')
    elements.click()
    # driver.implicitly_wait(5)

input(r'''
   .------\ /------.
   |       -       |
   |               |
   |               |
   |               |
_______________________
===========.===========     I'm proud of you
  / ~~~~~     ~~~~~ \      /
 /|   o         o    \    /
 W   ---  / \  ---   W
 \.      |o o|      ./
  |                 |
  \    #########    /
   \  ## ----- ##  /
    \##         ##/
     \_____v_____/
> ''')
