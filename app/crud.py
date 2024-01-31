from sqlalchemy.orm import Session
import models
from datetime import date


def get_price_by_date(db: Session, target_date: date):
    return db.query(models.ClosePrice).filter(models.ClosePrice.date_value == target_date).first()


def get_price_from_date(db: Session, target_date: date):
    return db.query(models.ClosePrice).filter(models.ClosePrice.date_value >= target_date).all()


def get_prices(db: Session):
    return db.query(models.ClosePrice).all()


def get_latest_price(db: Session):
    return db.query(models.ClosePrice).order_by(models.ClosePrice.id.desc()).first()

