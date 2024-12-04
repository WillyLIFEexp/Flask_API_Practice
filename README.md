# Flask API Practice
This is a practice for Flask API

## :hammer_and_pick: Technologies Used
- Programming Languages: Python
- Backend: Flask
- Other Libraries: Pytest

## :gear: Installation
- Python 3.8+
- [Docker](https://docs.docker.com/engine/install/) 

## :closed_book: Project Directory Structure
```bash
project-name/
├── app/ # Application source code 
│ ├── hello.py # Contains API endpoints 
│ └── __init__.py # Initializes the Flask app 
├── tests/ # Unit tests for the application 
│ ├── test_hello.py # Tests for API endpoints 
│ └── __init__.py # Test package initializer 
├── requirements.txt # Python dependencies 
├── Dockerfile # Docker configuration file 
└── README.md # Documentation for the project
```

## :wrench: Setting up

* Clone the Repo
* Build the container using the following command.
    ```
    docker build -t flask_docker .
    ```
* Starting the container with port mapping and let container to run in the background.
    ```
    docker run -d -p 5001:5000 flask_docker
    ```
* Stop the container by using the following command.
    ```
    docker stop <container-id-or-name>
    ```

## :pencil2: Testing
* Enter the container by the following command.
    ```
    docker exec -it <container-id-or-name> bash
    ```
* Running pytest to check for result
    ```
    pytest tests/test_hello.py
    ```

## :tophat: Demonstration
![](https://github.com/WillyLIFEexp/Flask_API_practice/blob/create_flask/imgs/demo_1.gif)
