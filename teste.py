from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver de inicialização / init driver
driver = webdriver.Chrome()
driver.maximize_window()

# abra a url / open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('One Piece')

# espero 4 segundos / wait for 4 sec  
sleep(4)

# clique em pesquisar / click search
driver.find_element(By.NAME, 'btnK').click()

# espero 4 segundos / wait for 4 sec  
sleep(4)

# verificar / verify
assert 'one+piece' in driver.current_url.lower(), f"Consulta esperada não encontrada em {driver.current_url.lower()}"
print('Teste Concluído com Sucesso')

driver.quit()
