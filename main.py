from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

##SITES = ('https://google.com', 'https://en.wikipedia.org/wiki/Main_Page', 'https://writtenrealms.com/')

SITES = '''https://www.youtube.com/watch?v=rPwvR_Mvrck&ab_channel=TF1INFO 
https://montreal.ctvnews.ca/forest-fire-centre-declares-2023-already-worst-year-ever-for-canadian-wildfires-1.6456879 
https://www.youtube.com/watch?v=LWCoGOG6-qQ&ab_channel=AssociatedPress 
https://www.reuters.com/graphics/CANADA-WILDFIRE/HISTORIC/znvnzebmavl/ 
https://www.youtube.com/watch?v=nq8uzf4CLhU&ab_channel=InsideEdition 
https://www.npr.org/2023/07/21/1188618934/canada-wildfires-answers 
https://www.wnep.com/article/news/local/luzerne-county/wildfire-shuts-down-route-11-in-luzerne-county-larksville-carey-avenue-bridge-to-east-main-street-wnep/523-3c1ab415-4249-4995-a33d-6d2eedb9edc0 
https://www.reuters.com/business/environment/canadian-wildfires-shutter-sawmills-drive-up-lumber-prices-2023-06-12/ 
https://www.noovo.info/nouvelle/le-tourisme-estival-est-affecte-par-les-feux-de-foret.html 
https://www.gov.mb.ca/health/publichealth/environmentalhealth/smoke.fr.html 
https://www.canada.ca/fr/sante-canada/services/publications/vie-saine/comment-preparer-fumee-feux-foret.html 
https://macleans.ca/longforms/burned-out-how-b-c-is-learning-to-live-with-wildfires/ 
https://www.ualberta.ca/agriculture-life-environment-sciences/news/ales-news-stories-archive/2017/november/new-trap-for-mountain-pine-beetles-could-help-weaken-their-spread.html 
https://cen.acs.org/materials/polymers/Researchers-examining-plastics-hazards-human/100/i32 
https://template-00007.membogo.com/fr/les-animaux-marins 
https://www.icl-group.com/blog/what-is-phosphate/ 
https://www.chemtube3d.com/n2/ '''.split('\n')


SITES = '''https://writtenrealms.com/
https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal
https://www.canada.ca/fr/sante-canada/services/publications/vie-saine/comment-preparer-fumee-feux-foret.html '''.split('\n')

FORMAT = 'MLA 8'

driver = webdriver.Chrome()

driver.get('https://www.mybib.com/')
print(driver.title)

first_x = driver.find_element(By.CLASS_NAME, 'material-icons')
first_x.click()

for site in SITES:
    sleep(0.5)

    driver.find_elements(By.CLASS_NAME, 'mu-ripple-wrapper')[4].click()

    sleep(0.5)

    search = driver.find_element(By.CLASS_NAME, 'rounded-l-sm')
    search.send_keys(site)

##    sleep(1)

    ##search_button = driver.find_elements(By.CLASS_NAME, 'material-icons')[34]
    for i in driver.find_elements(By.CLASS_NAME, 'material-icons')[::-1]:
        if i.text == 'search':
            search_button = i
            search_button.click()
            break

    sleep(2)

    site = driver.find_element(By.CLASS_NAME, 'flex.py-4.px-5.text-left.w-full')
    site.click()

    sleep(1)


    for i in range(2):
        no_element = driver.find_elements(By.CLASS_NAME, 'mu-flat-button.mu-flat-button-primary')
        if no_element:
            if len(no_element) != 1:
                print(f'{no_element=}')
            no_element[0].click()
            sleep(0.5)
        else:
            sleep(1)
            break

    
##    for i in range(2):
##        ripple_elems = driver.find_elements(By.CLASS_NAME, 'mu-ripple-wrapper')
##        if len(ripple_elems) == 17:
##            print(f'Click {i}')
##            ripple_elems[15].click()
##            sleep(0.5)
##        else:
##            break

    save_button = driver.find_elements(By.CLASS_NAME, "mu-raised-button.mu-raised-button-secondary.mu-raised-button-inverse")[1]
    save_button.click()


##a = driver.find_elements(By.CLASS_NAME, 'mu-raised-button.mu-raised-button-secondary.mu-raised-button-inverse')
##driver.find_elements(By.CLASS_NAME, 'mu-flat-button.mu-flat-button-primary')
