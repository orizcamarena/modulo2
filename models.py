
from sqlalchemy import Column, String, Integer
from db import Base


class Diccionario(Base):
  __tablename__ = 'diccionario'
  
  id = Column(Integer, primary_key=True)
  palabra = Column(String(50), unique=True)
  significado = Column(String(200))

  

  def __repr__(self):
    return f"<Diccionario(palabra='{self.palabra}',\nSignificado='{self.significado}')>" 
  
  