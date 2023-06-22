from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ConcesionesVigentes(LiveServerTestCase):

    def testFiltros(self):
        driver = webdriver.Chrome()

        driver.get("https://www.concesionesmaritimas.cl/")

        driver.implicitly_wait(int(10))

        #navego por los frames de la pagina para encontrar los selects
        frame = driver.find_element(By.NAME, 'centro_sigmar')
        driver.switch_to.frame(frame)

        iframe =driver.find_element(By.TAG_NAME, 'iframe')  
        driver.switch_to.frame(iframe)

        driver.implicitly_wait(int(10))

        variableRegion = driver.find_element(By.NAME, 'variableRegion')
        variableGobmar = driver.find_element(By.NAME, 'variableGobmar')
        variableCapuerto = driver.find_element(By.NAME, 'variableCapuerto')

        
        driver.implicitly_wait(int(10))

        submit = driver.find_element(By.NAME, 'verlistado')

        #ingreso los filtros para probar la pagina
        variableRegion.send_keys('2')
        variableGobmar.send_keys('12')
        variableCapuerto.send_keys('13')

        #se ejecutan los filtros
        submit.click()

        driver.implicitly_wait(int(10))
        """
        #capturo la tabla con los resultados
        tabla = driver.find_element(By.TAG_NAME, "table")

        filas = tabla.find_elements(By.TAG_NAME, "tr")

        # Recorrer las filas y capturar los datos
        for fila in filas:
            # Obtener todas las celdas de la fila
            celdas = fila.find_elements(By.TAG_NAME, "td")
            
            # Imprimir el contenido de cada celda
            for celda in celdas:
                print(celda.text)

        # Cerrar el navegador
        """
        driver.quit()
