# Welcome to our trial

Please ensure you follow all the steps before submitting it for review.

# Trial tasks
Our trial is straightforward and simple. Please fork this repository and build the following app in the forked repository. When you are done, create a pull targeting our `truflation/trial` repo.

## App hard requirements:
1. get a Lithium data feed from [Yahoo.com](https://finance.yahoo.com/quote/LITH-USD/)
2. push the data into any database of your choice hosted by a third party, where the schema has the following attributes `id, date_value, value, created_at`
3. expose https endpoint with a simple JSON feed from the database to demo the app

## Review Score Criteria
1. simplicity of the code for the reviewer
2. the naming of the commits (follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/))
3. clear communication with our team

## Questions? 
If you have any questions, please feel free to ask them in [truflation/trial/discussions](https://github.com/truflation/trial/discussions)  
DO NOT ask your question by any other channel.

## Description of Project
1. I build project using poetry (Python project management tool)
2. I fetched Lithium Data feed (LTH-USD) using yfinance python framework
3. I pushed data feed into sql database with history table name through "/add_feed" API after fetching Lithium Data feed 
   Data gets to be saved on "symbols.db"

    - I used SQLALCHEMY python framework to manage sql database
    - I managed API using FASTAPI python framework.
    - I used BackgroundTask for asynchronous process.         
        In FastAPI, BackgroundTask is a class that allows you to add background tasks to be executed after a response is sent to the client. Background tasks are useful for performing asynchronous tasks without blocking the main application response. They are often used for tasks that are not critical for the immediate response
4. Can get data feed saved on database using "/feed" API 

## How to run this project
1. Install required dependencies

2. poetry install 

3. poetry run start 

    http://127.0.0.1:8000 server running

    http://127.0.0.1:8000/add_feed : open database and fetch data and save

    http://127.0.0.1:8000/feed : Fetch Lithum Historical Feed Data
    