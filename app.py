
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


#Entrar site https://pje-consulta-publica.tjmg.jus.br/

servico = Service (ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
driver.get('https://pje-consulta-publica.tjmg.jus.br/')
sleep(30)

numero_oab =  133864 
#digitar oab
campo_oab = driver.find_element(By.XPATH,"//input[@id='fPP:Decoration:numeroOAB']")
campo_oab.send_keys(numero_oab)

#selecionar estado 

dropdown_estados = driver.find_element(By.XPATH, "//select[@id='fPP:Decoration:estadoComboOAB']")
opcoes_estados = Select(dropdown_estados)
opcoes_estados.select_by_visible_text('SP')

#clicar e pesquisar

botao_pesquisar = driver.find_element(By.XPATH, "//input[@id='fPP:searchProcessos']")
botao_pesquisar.click()
sleep(10)


#entrar em processos 
processos = driver.find_elements(By.XPATH,"//b[@class='btn-block']")

for processo in processos: 
    processo.click()
    sleep(10)
    janelas = driver.window_handles #codigos janelas 
    driver.switch_to.window(janelas[-1])
    driver.set_window_size(1920,1080) #tamanho da janela no navegador 

    numero_de_processo = driver.find_element(By.XPATH,"//div[@class='col-sm-12 ']")
    numero_de_processo = numero_de_processo[0]
    numero_de_processo = numero_de_processo.text


    data_distribuicao = driver.find_element(By.XPATH, "//div[@class='value col-sm-12 ']")
    data_distribuicao = data_distribuicao[1]
    data_distribuicao = data_distribuicao.text
    sleep(5000)



