# Bibliotecas ##################################################
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

from worker_config import *


# Config #######################################################
def config(path=path,file=file,url=url,browser=browser,verbose=verbose):

    print("--------------------------------------------")
    options = ""
    if (verbose == "no"):
        options = Options()
        options.add_argument('--headless')

    if (url==""):
        url = input("Link: ")
    else:
        print("Using url config...")

    if not path:
        path = os.getcwd() 
        path += "/"
    
    if (file==""):
        file = path + input("Nome do arquivo: ")
    else:
        file = path + file
        print("Using file config...")

    global wb 
    wb = ""
    if (browser == "Firefox"):
        if (options==""):
            wb = webdriver.Firefox()
        else:
            wb = webdriver.Firefox(options=options)

    else:
        if (options==""):
            wb = webdriver.Chrome()
        else:
            wb = webdriver.Chrome(options=options)

    print("--------------------------------------------")
    return [url,file]


# Worker #######################################################
def waiting_warning():
    print()
    print("Wating server...")

def get_url(url):
    wb.get(url)
    sleep(5)

# Verifica se deu erro ou nao
def verify_request():
    try:
        all_text = wb.find_elements(By.TAG_NAME,'p')
        for i in all_text:
            if "Houve um erro" in i.text or "Ocorreu um problema" in i.text:
                return False
    except:
        return True

# Faz o request
def send_request(file, id=1):
    #  FirstRequest
    if (id == 1):
        field_input = wb.find_element(By.ID, 'id_data')
        field_input.send_keys(file)
        button_submit = wb.find_element(By.CLASS_NAME,'button')

    else:
        wb.back()
        wb.back()
        button_submit = wb.find_element(By.CLASS_NAME,'button')

    sleep(2)
    button_submit.click()
    sleep(70)

# Realiza o tratamento dos requests
def make_request(file):
    waiting_warning()
    send_request(file)

    while (verify_request() == False):
        waiting_warning()
        send_request(file,id=2)

def print_response(): 
    print()
    print("Server connected!")
    print()
    print("Getting request's response...")

    elements = wb.find_elements(By.CLASS_NAME,"subtask-head")
    for i in elements:
        i.click()
    sleep(2)

    print()
    print("--------------------------------------------")
    elements = wb.find_elements(By.ID,"submission_list")
    for i in elements:
        print(i.text)
    print("--------------------------------------------")
    print()

    elements = wb.find_elements(By.CLASS_NAME,"score_details")
    for i in elements:
        print(i.text)

def main(path=path,file=file,url=url,browser=browser,verbose=verbose):
    data = config(path=path,file=file,url=url,browser=browser,verbose=verbose)
    url,file = data[0],data[1]

    get_url(url)
    make_request(file)
    print_response()
    
