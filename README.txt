Honeycomb
=========

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    cd honeycomb

- Create a Python virtual environment, if not already created.

    python3 -m venv env

- Upgrade packaging tools, if necessary.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini


Running into a Docker Container
-------------------------

- Change directory into your newly created project.

- Run the following command to build the honeycomb image.

    docker build -t "honeycomb:latest" .

- Create a new container based on the honeycomb:latest image.

    docker run -p 6543:6543 --rm honeycomb:latest

- Open your browser and visit: http://127.0.0.1:6543
