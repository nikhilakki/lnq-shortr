<!--
 Copyright (c) 2022 Nikhil Akki
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

# URL Link Shortener app

Source code for [lnqshortr.com](https://lnqshortr.com) backend.

This app is URL-Link shorter service built using Python-FastAPI

### Author - [Nikhil Akki](https://nikhilakki.in)

### License -

**LNQ Shortr** is an open source product licensed under GPLv3.

### Development

Uses the default Django development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:80](http://localhost:80). No mounted folders. To apply changes, the image must be re-built.
