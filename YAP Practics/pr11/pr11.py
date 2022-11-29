import json
import requests 
from tkinter import *

window = Tk()
window.title("Королёв_Никита_УБ-23")
window.geometry('600x300')

name_github = Entry(window, width = 7)
name_github.grid(column = 3, row = 0)
name_github.insert(0, 'origin')

def write_text(filename, text):
    file = open(filename, 'w')
    file.write(text)
    
def click():
    try:
        json = requests.get(f'https://api.github.com/users/{name_github.get()}').json()
    except:
        json = requests.get(f'https://api.github.com/users/origin').json()
    try:
        company = json["company"]
    except:
        company = "None"
    try:
        created_at = json["created_at"]
    except:
        created_at = "None"
    try:
        email = json["email"]
    except:
        email = "None"
    try:
        id = json["id"]
    except:
        id = "None"
    try:
        name = json["name"]
    except:
        name = "None"
    try:
        url = json["url"]
    except:
        url = "None"   
    write_text('pr11\\github_dannie.txt',f"'company': {company}\n'create_at': {created_at}\n'email': {email}\n'id': {id}\n'name': {name}\n'url': {url}")

pusk_program = Button(window, text = 'START',command = click)
pusk_program.grid(column = 2, row = 1)

window.mainloop() 