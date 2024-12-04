# Flask_API_practice
This is a practice for Flask API

## :hammer_and_pick: Technologies Used
- Programming Languages: Python
- Backend: Flask
- Other Libraries: Pytest

## :gear: Installation
- Python 3.8+
- Docker 

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

## :pencil2: Testing
* Enter the container by the following command.
    ```
    docker exec -it <container_id or container_name> bash
    ```
* Running pytest to check for result
    ```
    pytest test_hello.py
    ```
## Project Directory Structure
project-name/ 
├── app/ # Application source code 
│ ├── init.py # Initializes the Flask app 
│ ├── routes.py # Contains API endpoints 
│ ├── models.py # Defines database models 
│ └── templates/ # HTML templates for the application 
│ └── index.html # Main HTML file for the app 
├── tests/ # Unit tests for the application 
│ ├── test_routes.py # Tests for API endpoints 
│ ├── test_models.py # Tests for database models 
│ └── init.py # Test package initializer 
├── requirements.txt # Python dependencies 
├── Dockerfile # Docker configuration file 
└── README.md # Documentation for the project