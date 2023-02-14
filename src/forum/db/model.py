from __future__ import annotations
from datetime import date
from forum.utils import UNDEFINED
from forum.db.connection import Connection
from datetime import datetime


class Model:
    _table: str
    _columns: list[str]

    @property
    def _insert_query(self) -> str:
        #default query for insert with table name defined in child classes
        query: str = f'insert into {self._table} ('
        
        #inserting columns names stored in a list in child classes
        query += ''.join(f'{column},' for column in self._columns)[:-1]
        query += ') values ('

        #inserting object values in query
        query += ''.join(f"'{value}'," if isinstance(value, (str, date)) else f"{value}," for value in self.values)[:-1]
        query += ');'

        return query

    @property
    def values(self) -> list[any]: return []


    def insert(self) -> None:
        with Connection() as connection:
            connection.execute(self._insert_query)



class User(Model):
    _table: str = 'User'
    _columns: list[str] = 'username', 'password', 'email'

    def __init__(self, username: str = UNDEFINED, password: str = UNDEFINED, email: str = UNDEFINED) -> None:
        self.username = username
        self.password = password
        self.email = email
    
    @property
    def values(self) -> list[any]: 
        return self.username, self.password, self.email
    

class Forum(Model):
    _table: str = 'Forum'
    _columns: list[str] = 'tag', 'title', 'description', 'date_creation', 'themes', 'creator_username', 'owner_username'

    def __init__(self, 
        tag: str = UNDEFINED, 
        title: str = UNDEFINED, 
        description: str = UNDEFINED, 
        date_creation: datetime = UNDEFINED, 
        themes: str = UNDEFINED,
        creator: User = UNDEFINED,
        owner: User = UNDEFINED,
        members: list[User] = UNDEFINED,
        moderators: list[User] = UNDEFINED) -> None:
        
        self.tag = tag
        self.title = title
        self.description = description
        self.date_creation = date_creation
        self.themes = themes
        self.creator = creator
        self.owner = owner
        self.members = members
        self.moderators = moderators
    
    @property
    def values(self) -> list[any]:
        return self.tag, self.title, self.description, self.date_creation, self.themes, self.creator.username, self.owner.username


class Topic(Model):
    _table: str = 'Topic'
    _columns: list[str] = 'id', 'title', 'body', 'date_publication', 'author_username', 'forum_tag'

    def __init__(self, 
        id: int = UNDEFINED, 
        title: str = UNDEFINED, 
        body: str = UNDEFINED, 
        date_publication: datetime = UNDEFINED,
        author: User = UNDEFINED,
        forum: Forum = UNDEFINED) -> None:        
        self.id = id
        self.title = title
        self.body = body
        self.date_publication = date_publication
        self.author = author
        self.forum = forum

    @property
    def values(self) -> list[any]:
        return self.id, self.title, self.body, self.date_publication, self.author.username, self.forum.tag


class Comment(Model):
    _table: str = 'Comment'
    _columns: list[str] = 'id', 'body', 'author', 'comment_answered_id'
    
    def __init__(self, id: int = UNDEFINED, body: str = UNDEFINED, author: User = UNDEFINED, answer_to: Comment = UNDEFINED) -> None:
        self.id = id
        self.body = body
        self.author = author
        self.answer_to = answer_to
    
    @property
    def values(self) -> list[any]:
        return self.id, self.body, self.author.username, self.answer_to.id