# Personal Project - Real-Time Data Visualization

## Introduction

Welcome to my personal project! In this endeavor, I have built a simple web-based dashboard to visualize real-time process data. The main goal is to demonstrate my proficiency in Python and showcase my skills in developing data visualization applications.

## Technical Details

Within this directory, you'll find a `Dockerfile` that defines the image for running the code. The source code is installed into a Python 3.10 virtual environment as a package using pip, along with any specified dependencies listed in the `requirements.txt` file.

To serve the web-based dashboard locally, I have configured Docker to start the container and execute the `run-app` command, which serves the dashboard on http://localhost:8888/.

### The Database

The data used for visualization is stored in a PostgreSQL database, which is also configured in `compose.yaml`. To access the database, you'll need the following environment variables:
- `POSTGRES_HOST`: Provides the host
- `POSTGRES_PORT`: Provides the port
- `POSTGRES_USER`: Provides the user
- `POSTGRES_PASSWORD`: Provides the password
- `POSTGRES_DB`: Provides the database

An example configuration can be found in `local.env`. Please avoid hardcoding these credentials as they are subject to change.

### The Data

The database contains information about various process parameters. Here are some examples of the data stored in the tables:

| Table                    | Name             | Units   |
|--------------------------|------------------|---------|
| CM_HAM_DO_AI1/Temp_value | Temperature      | Celsius |
| CM_HAM_PH_AI1/pH_value   | pH               | n/a     |
| CM_PID_DO/Process_DO     | Distilled Oxygen | %       |
| CM_PRESSURE/Output       | Pressure         | psi     |

## How to Test the Code

To test the code, follow these steps:

1. Run `docker compose up`.
2. Open your browser and navigate to http://localhost:8888/.
3. You should now be able to view the dashboard.
