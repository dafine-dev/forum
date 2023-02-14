from PySimpleGUI import PySimpleGUI as sg
from forum.view.prompts import prompts
from forum.db.model import User


def signup_user(user_info):
    User(**user_info).insert()


def start():

    sg.theme('Reddit')

    layout = [
        [sg.Text(prompts['username']), sg.Input(key = 'username')],
        [sg.Text(prompts['password']), sg.Input(key = 'password', password_char = '*')],
        [sg.Text(prompts['password']), sg.Input(prompts['email'], key = 'email')],
        [sg.Button(prompts['signup'])]
    ]

    window = sg.Window(prompts['signup'], layout)

    while True:

        events, user_info = window.read()

        if events == sg.WINDOW_CLOSED: 
            break
        
        elif events == prompts['signup']:
            signup_user(user_info)