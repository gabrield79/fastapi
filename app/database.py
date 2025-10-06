from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Reemplaza estos datos con los de tu servidor PhpMyAdmin
DATABASE_URL = "mysql+pymysql://usuario:contraseña@IP_o_dominio/nombre_basedatos"

# Ejemplo:
# DATABASE_URL = "mysql+pymysql://root:12345@192.168.1.100/mi_base"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
