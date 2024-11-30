from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

##SITES = ('https://google.com', 'https://en.wikipedia.org/wiki/Main_Page', 'https://writtenrealms.com/')

SITES = '''https://www.youtube.com/watch?v=rPwvR_Mvrck&ab_channel=TF1INFO
https://writtenrealms.com/
https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal
https://www.canada.ca/fr/sante-canada/services/publications/vie-saine/comment-preparer-fumee-feux-foret.html
https://www.ualberta.ca/agriculture-life-environment-sciences/news/ales-news-stories-archive/2017/november/new-trap-for-mountain-pine-beetles-could-help-weaken-their-spread.html
https://montreal.ctvnews.ca/forest-fire-centre-declares-2023-already-worst-year-ever-for-canadian-wildfires-1.6456879 
https://www.youtube.com/watch?v=LWCoGOG6-qQ&ab_channel=AssociatedPress 
https://www.reuters.com/graphics/CANADA-WILDFIRE/HISTORIC/znvnzebmavl/ 
https://www.youtube.com/watch?v=nq8uzf4CLhU&ab_channel=InsideEdition 
https://www.npr.org/2023/07/21/1188618934/canada-wildfires-answers 
https://www.wnep.com/article/news/local/luzerne-county/wildfire-shuts-down-route-11-in-luzerne-county-larksville-carey-avenue-bridge-to-east-main-street-wnep/523-3c1ab415-4249-4995-a33d-6d2eedb9edc0 
https://www.reuters.com/business/environment/canadian-wildfires-shutter-sawmills-drive-up-lumber-prices-2023-06-12/ 
https://www.noovo.info/nouvelle/le-tourisme-estival-est-affecte-par-les-feux-de-foret.html 
https://www.gov.mb.ca/health/publichealth/environmentalhealth/smoke.fr.html 
https://macleans.ca/longforms/burned-out-how-b-c-is-learning-to-live-with-wildfires/ 
https://cen.acs.org/materials/polymers/Researchers-examining-plastics-hazards-human/100/i32 
https://www.chemtube3d.com/n2/ '''.split('\n')

SITES = '''https://www.youtube.com/watch?v=rPwvR_Mvrck&ab_channel=TF1INFO
https://writtenrealms.com/
https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal
https://www.canada.ca/fr/sante-canada/services/publications/vie-saine/comment-preparer-fumee-feux-foret.html
https://www.ualberta.ca/agriculture-life-environment-sciences/news/ales-news-stories-archive/2017/november/new-trap-for-mountain-pine-beetles-could-help-weaken-their-spread.html
https://montreal.ctvnews.ca/forest-fire-centre-declares-2023-already-worst-year-ever-for-canadian-wildfires-1.6456879 
https://www.youtube.com/watch?v=LWCoGOG6-qQ&ab_channel=AssociatedPress '''.split('\n')

SITES = '''https://www.sciencedirect.com/science/article/abs/pii/S0022395616301893?via%3Dihub
https://www.montgomeryadvertiser.com/story/life/2016/04/18/positive-reinforcement-not-bribery/83181196/#:~:text=Positive%20reinforcement%20can%20be%20an,return.%E2%80%9D%20It%20is%20manipulation.
'''.split('\n')

SITES = '''https://www.shutterstock.com/search/best-friends-teen 
https://www.iceshaker.com/en-ca/products/20oz-sport-bottle-green
https://www.pixelsquid.com/png/women-s-sunglasses-closed-pink-2364783717613835403?image=G03 
https://parspng.com/en/images/womens-sports-shoes-png/
https://ca.pinterest.com/pin/123215739794346665/
https://www.vecteezy.com/free-png/kids-dress 
https://pngtree.com/freepng/portrait-of-a-pretty-smiling-teen-girl-with-long-hair-in-interior-with-christmas-decorations_13968622.html
https://www.shutterstock.com/search/boy-girl-crush 
https://stock.adobe.com/images/happy-cute-and-a-teen-girl-in-fashion-casual-and-trendy-clothes-with-a-smile-and-confident-mindset-on-a-png-transparent-and-mockup-or-isolated-background-portrait-of-a-real-teenager-with-attitude/529574170 
https://www.dreamstime.com/photos-images/teen-friends-vertical.html'''.split('\n')


FORMAT = 'MLA 8'

driver = webdriver.Chrome()

driver.get('https://www.mybib.com/')
print(driver.title)

first_x = driver.find_element(By.CLASS_NAME, 'material-icons')
first_x.click()

for site in SITES:
    # driver.implicitly_wait(3)
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'mu-ripple-wrapper'))).click()
    # driver.find_elements(By.CLASS_NAME, 'mu-ripple-wrapper')[4].click()
    # driver.implicitly_wait(5)
    
    search = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'mu-ripple-wrapper'))).click()
    search = driver.find_element(By.CLASS_NAME, 'rounded-l-sm')
    search.send_keys(site)

    for i in driver.find_elements(By.CLASS_NAME, 'material-icons')[::-1]:
        if i.text == 'search':
            search_button = i
            search_button.click()
            break
    # driver.implicitly_wait(5)

    site = driver.find_element(By.CLASS_NAME, 'flex.py-4.px-5.text-left.w-full')
    site.click()
    # driver.implicitly_wait(5)

    for i in range(2):
        no_element = driver.find_elements(By.CLASS_NAME, 'mu-flat-button.mu-flat-button-primary')
        if no_element:
            if len(no_element) != 1:
                print(f'{no_element=}')
            no_element[0].click()
            # driver.implicitly_wait(0.5)
        else:
            # driver.implicitly_wait(2)
            break

    save_button = driver.find_elements(By.CLASS_NAME, "mu-raised-button.mu-raised-button-secondary.mu-raised-button-inverse")[1]
    save_button.click()


# driver.implicitly_wait(1)
for site in driver.find_elements(By.CLASS_NAME, 'bibliography-row'):
    site = site.text
    if not ('\nDate published' in site):
        if '\nWebpage author' in site:
            index = 1
        else:
            index = 2
    site = site.split('\n')[0]
    site = site.replace('“', '"').replace('”', '"')
    index += site.split('"')[1].count(',')
    print(site.split(',')[index])
    
