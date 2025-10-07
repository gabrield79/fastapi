from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, crud, schemas
from .database import engine, SessionLocal

# Iniciar la aplicación
app = FastAPI()

# Crear las tablas si no existen
models.Base.metadata.create_all(bind=engine)

# Ruta de prueba
@app.get("/")
def read_root():
    return {"mensaje": "API FastAPI funcionando correctamente"}

# Dependencia para obtener la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Crear usuario
@app.post("/usuario/", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db=db, usuario=usuario)

# Obtener usuarios
@app.get("/usuario/", response_model=list[schemas.UsuarioOut])
def obtener_usuarios(db: Session = Depends(get_db)):
    return crud.obtener_usuarios(db)
