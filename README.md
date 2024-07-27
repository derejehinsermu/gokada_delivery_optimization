# Logistic Optimization: Delivery Driver Location Optimization with Causal Inference

## Overview

Gokada, Nigeria’s largest last-mile delivery service, has successfully completed over a million deliveries in Lagos with a fleet of more than 1200 riders. However, as the service expands, Gokada faces the challenge of sub-optimal placement of pilots (drivers) and clients, leading to a high number of unfulfilled delivery requests. To address this issue, Gokada has enlisted the help of 10 Academy trainees to analyze data, understand the primary causes of unfulfilled requests, and recommend optimal driver locations to increase the fraction of completed orders.


## Technologies Used

- **Judea Pearl’s Causal Inference Framework**: For answering causal questions and understanding impact.
- **Haversine Formula**: To calculate distances between geographic coordinates.
- **Geodesic Distance**: Provides more accurate distance calculations over long distances.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x and pip (usually bundled with Python installation)
- Git installed on your machine
- Virtualenv (install using pip):
  ```bash
  pip install virtualenv

### Installation

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
## Usage

To run the optimization analysis:

    Prepare the Data
    Follow the data preparation steps outlined in the documentation.

    Run the Analysis
    Execute the provided scripts to perform causal inference and optimization analysis.

    Review Results
    Analyze the output to determine optimal driver locations.
Check out the details of this [project](https://medium.com/@derejehinsermu/optimizing-delivery-driver-locations-a-causal-inference-approach-4956bb469007) in my blog post.

## Contributing

Contributions are welcome! 

For any questions or support, please contact derejehinsermu2@gmail.com.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
    
