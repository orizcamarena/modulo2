from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('mysql+pymysql://root:12345678@localhost/Diccionario')

#Crear sesion con el engie de base de datos
Session = sessionmaker(bind=engine)
session = Session()
