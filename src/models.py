import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

#https://app.quickdatabasediagrams.com/#/d/ydPxrW


Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table Follower
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.ID'))
    user_to_id = Column(Integer, ForeignKey('User.ID'))

    #Relationships
    user_from = relationship('User', foreign_keys=[user_from_id], backref='followers')
    user_to = relationship('User', foreign_keys=[user_to_id], backref='following')

class User(Base):
    __tablename__ = 'User'
    #Columns
    ID = Column(Integer, primary_key=True) 
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)

    #Relationships
    followers = relationship('Follower', backref='user_from')
    following = relationship('Follower', backref='user_to')
    posts = relationship('Post', backref='user')
    comments = relationship('Comment', backref='author')

class Comment(Base):
   __tablename__ = "Comment" 
   #Columns
   ID = Column(Integer, primary_key=True)
   comment_text = Column(String)
   author_id = Column(Integer, ForeignKey('User.ID'))
   post_id = Column(Integer, ForeignKey('Post.ID'))

   #Relationships
   author = relationship('User', backref='comments')

class Media(Base):
    __tablename__ = "Media"
    #Columns
    ID = Column(Integer, primary_key=True)
    type = Column(Enum('image', 'video'))
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.ID'))

class Post(Base):
    __tablename__ = "Post"
     #Columns
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.ID'))

    #Relationships
    user = relationship('User', backref='posts')
    comments = relationship('Comment')
    media = relationship('Media')
    


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
