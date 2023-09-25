from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

def LoginSite(driver,user,password):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"session_key")))
        driver.find_element(By.ID,"session_key").send_keys(user)

        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"session_password")))
        driver.find_element(By.ID,"session_password").send_keys(password,Keys.ENTER)

    except:
        raise



def Search(driver,SearchText):
    try:    
        driver.get(f"https://www.linkedin.com/search/results/people/?keywords={SearchText}&origin=CLUSTER_EXPANSION&sid=jWZ")
    
    except:
        raise


def Connect(driver,Window):
    try:
        for Index in range(1,11):

            try:
                WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,f"html/body/div//div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{Index}]/div/div/div//div/button")))
            
            except:
                Window().ConnectionLimit()
                exit()
            
            sleep(1.5)
            Person = driver.find_element(By.XPATH,f"html/body/div//div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul/li[{Index}]/div/div/div//div/button")

            if Person.text == "Conectar":
                Person.click()

                WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]")))
                driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[3]/button[2]").click()
                continue

            else:
                print("Can't connect, going to next person!!")
                continue

    except:
        raise


def ChangeTab(driver,counter):
    try:
        if counter == 100:
            return "Can't click anymore"

        else:
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
            driver.execute_script('document.querySelector(`[aria-label="Avançar"]`).click()')

    except:
        input("deu erro change tab")
        raise