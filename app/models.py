from sqlalchemy import Column, Integer, String
from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"  # debe coincidir con tu tabla MySQL

    idusuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45))
    email = Column(String(100), unique=True)
    password = Column(String(255))
    apellido = Column(String(45))
    telefono = Column(String(11))
