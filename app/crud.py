from sqlalchemy.orm import Session
from . import models, schemas

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    nuevo_usuario = models.Usuario(nombre=usuario.nombre, email=usuario.email)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def obtener_usuarios(db: Session):
    return db.query(models.Usuario).all()
