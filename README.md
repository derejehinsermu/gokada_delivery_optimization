# Optimizing Delivery Driver Locations: A Causal Inference Approach

## Overview:

Gokada, Nigeria’s largest last-mile delivery service, has successfully completed over a million deliveries in Lagos with a fleet of more than 1200 riders. However, as the service expands, Gokada faces the challenge of sub-optimal placement of pilots (drivers) and clients, leading to a high number of unfulfilled delivery requests. To address this issue, Gokada has enlisted the help of 10 Academy trainees to analyze data, understand the primary causes of unfulfilled requests, and recommend optimal driver locations to increase the fraction of completed orders.


## Getting Started

These instructions will guide you through the process of setting up and running the prompt generation

### Prerequisites

1. Python 3.x and pip (Usually bundled with Python installation)

2. Git installed on your machine.

3. Virtualenv. You can install it using pip:
    ```sh
    pip install virtualenv

### Steps

1. **Clone the Repository**
    ```sh
     git@github.com:derejehinsermu/gokada_delivery_optimization.git
    ```
2. **Create and Activate a Virtual Environment**
    Navigate to the root directory of the project and create a virtual environment named 'venv', then activate it:
    ```sh
    cd gokada_delivery_optimization.git
    python -m venv venv  | virtualenv venv
    source venv/bin/activate
    ```
3. **Install Requirements**
    While inside the virtual environment, install the project requirements:
    ```sh
    pip install -r requirements.txt
    ```
