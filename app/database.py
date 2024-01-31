from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote


user = "freedb_escandar"
password = quote("%Z@v7tzjzd!NS!P")
host = "sql.freedb.tech"
port = 3306
database = "freedb_price_data"
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
