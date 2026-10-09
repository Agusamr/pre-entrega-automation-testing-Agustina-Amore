from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_exitoso():

    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    wait = WebDriverWait(driver,10)

    try:


# Navegar a la página de login
        driver.get("https://www.saucedemo.com/")
        
        usuario = wait.until(EC.presence_of_element_located((By.ID,"user-name")))
        contrasena = wait.until(EC.presence_of_element_located((By.ID,"password")))
        boton_login = wait.until(EC.element_to_be_clickable((By.ID,"login-button")))



    #primero localizo los elementos de la web para interactuar con ellos...
       #usuario = driver.find_element(By.ID,"user-name")
        #contrasena = driver.find_element(By.ID,"password")
        #boton_login = driver.find_element(By.ID,"login-button")"""
        
    #completar el form
        usuario.send_keys("standard_user")
        contrasena.send_keys("secret_sauce")
    #hacer login
        boton_login .click()
        
        titulo = driver.find_element(By.CLASS_NAME,"app_logo")
        
        #validar la URL despues del login
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert titulo.text == "Swag Labs"

        
    finally:
        driver.quit()
