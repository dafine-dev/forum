from datetime import date
from PySimpleGUI import PySimpleGUI as sg
from forum.view.prompts import prompts
from forum.db.model import Forum

def create_forum(forum_info):
    Forum(**forum_info).insert()    


def start():

    sg.theme('Reddit')

    layout = [
        [sg.Text(prompts['forum_tag']), sg.Input(key = 'tag')],
        [sg.Text(prompts['forum_title']), sg.Input(key = 'title')],
        [sg.Text(prompts['forum_description']), sg.Input(key = 'description')],
        [sg.Button(prompts['create_forum'])]
    ]

    window = sg.Window(prompts['create_forum'], layout)

    while True:

        events, forum_info = window.read()

        if events == sg.WINDOW_CLOSED: 
            break
        
        elif events == prompts['create_forum']:
            forum_info['date_creation'] = date.today()
            create_forum(forum_info)