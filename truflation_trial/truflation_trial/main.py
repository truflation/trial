# from fastapi import (
#     APIRouter,
#     BackgroundTasks,
#     Depends,
#     FastAPI,
# )
# from fastapi.middleware.cors import CORSMiddleware
# import sqlalchemy
# from sqlalchemy.orm import Session
import yfinance as yf
# from typing import List
def start():
    ticker = yf.Ticker("LITH-USD")
    daily = ticker.history()
    print(daily)
    
if __name__ == '__main__': 
    start()