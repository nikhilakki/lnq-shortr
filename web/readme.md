<!--
 Copyright (c) 2022 Nikhil Akki
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

## How to run?

#### Development - 
1. Create .env file at `web/web/.env` in the following format - 
    ```
    DEBUG=True
    SECRET_KEY=supersecretcode
    URL_DOMAIN=http://localhost:5000
    ```
1. Run following cmds -
    ```bash
    poetry install
    poetry run python manage.py migrate # creates db connection & applies changes
    poetry run python manage.py runserver # dev runserver on local    
    ```