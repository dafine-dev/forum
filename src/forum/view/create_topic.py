from datetime import date
from random import randint
from PySimpleGUI import PySimpleGUI as sg
from forum.view.prompts import prompts
from forum.db.model import Forum, Topic


def publish_topic(topic_info):
    Topic(
        id = randint(1000, 1000000),
        title = topic_info['title'],
        body = topic_info['body'],
        date_publication = date.today(),
        forum = Forum(tag = topic_info['forum_tag'])
    ).insert()
        


def start():

    sg.theme('Reddit')

    layout = [
        [sg.Text(prompts['publishing_forum_tag']), sg.Input(key = 'forum_tag')],
        [sg.Text(prompts['topic_title']), sg.Input(key = 'title')],
        [sg.Text(prompts['topic_body']), sg.Input(key = 'body')],
        [sg.Button(prompts['publish'])]
    ]

    window = sg.Window(prompts['publish'], layout)

    while True:

        events, topic_info = window.read()

        if events == sg.WINDOW_CLOSED: 
            break
        
        elif events == prompts['publish']:
            publish_topic(topic_info)