
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
from time import sleep

#Entrar site https://pje-consulta-publica.tjmg.jus.br/
#entrar no site -  Qual é o principal objetivo da tecnologia blockchain? * 
#digitar numero oab e selecionar e estado 
# clicar em pesquisar 
# entrar em cada um dos processos 

#extrarir o numero de processos e data de distrubuição 
#extrar e guardar todas últimas movimentações 
#guardar tudo no exel, separados pro processo 



numero_oab=133864


#Entrar site https://pje-consulta-publica.tjmg.jus.br/

servico = Service (ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
driver.get('https://pje-consulta-publica.tjmg.jus.br/')
sleep(100)


#digitar oab
campo_oab = driver.find_element(By.XPATH, "input [@id='fPP:Decoration:numeroOAB']")
campo_oab.send_keys(numero_oab)

#selecionar estado 

dropdown_estados = driver.find_element(By.XPATH, "//select[@id='fPP:Decoration:estadoComboOAB']")
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text('SP')

#clicar e pesquisar

botao_pesquisar = driver.find_element(By.XPATH, '//input[@id="fPP:searchProcessos"]')
botao_pesquisar.click()
sleep(10)
