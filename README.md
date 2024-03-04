# CarDataConduit: Digital Product Passports for Sustainable Mobility

## Overview
CarDataConduit is a project aimed at developing a secure, scalable framework for digital product passports.

## Features
- **Digital Product Passport Creation**: Generate secure, verifiable digital passports for vehicles.
- **Attribute-Based Access Control (ABAC)**: Securely manage data access based on user attributes and policies.
- **Environmental Impact Tracking**: Monitor and report on the environmental impact of vehicles, including CO2 emissions and resource usage.
- **Lifecycle Traceability**: Track the entire lifecycle of a vehicle to ensure responsible manufacturing and disposal practices.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Docker
- Python 3.8+
- Flask

### Installation
1. **Clone the repository**
```bash
git clone https://github.com/adityasissodiya/carDataConduit
```

2. **Build the Docker container**
```bash
docker build -t cardataconduit .
```

3. **Run the container**
```bash
docker run -p 5000:5000 cardataconduit
```

### Usage
To interact with the system, use the provided API endpoints:

- **Create Digital Passport**: `POST /api/passport/create`
- **Update Service Record**: `POST /api/service/update`
- **Query Vehicle Data**: `GET /api/vehicle/{id}`

See the API documentation for more details on request and response formats.

### Running Tests
Execute the following command to run the automated test suite:
```bash
python -m unittest discover tests
```

## Built With
- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [RDFLib](https://rdflib.readthedocs.io/) - For managing RDF data
- [Docker](https://www.docker.com/) - Containerization platform
