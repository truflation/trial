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

## Setup
**NOTE:** Need Python 3.10 or later.

1. Install [Poetry](https://python-poetry.org/docs/#installation). Poetry is a package management tool.
2. Create and activate a virtual environment.
3. Run the following line to install all necessary packages:

    ```bash
    poetry install
    ```
4. Run the following command to start the API server:
    ```bash
    poetry run start
    ```
    This will not only start the server, but also setup the SQLite database and it's tables.
5. Go to browser and type the following:
    `127.0.0.1/feed`
    This will get the yahoo feed and store into the database.
6. To view the data from the database, go to `127.0.0.1`