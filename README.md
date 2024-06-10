# NopCommerce Test Automation Framework

## Introduction

Welcome to the NopCommerce Test Automation Framework repository. This project contains automated test scripts for the NopCommerce application, utilizing Selenium WebDriver, Python and PyTest. The framework is designed to ensure the robustness and reliability of the NopCommerce application through comprehensive automated testing.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Automated Tests**: Test cases for the NopCommerce application using different sets of data.
- **Selenium WebDriver**: Utilizes Selenium WebDriver for browser automation.
- **Python**: Test scripts are written in Python for simplicity and readability.
- **Reporting**: Generates detailed test execution reports.
- **Logging**: Captures detailed logs for debugging purposes.

## Setup and Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/SurajBehera23/Nopcommerce.git
   cd Nopcommerce
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests

To run the tests, use the following command:

```sh
pytest
```

This command will execute all the test cases and generate a report.

## Project Structure

```sh
Nopcommerce/
├── base_pages/          # Base page classes for Page Object Model
├── configurations/      # Configuration files and settings
├── logs/                # Log files
├── reports/             # Test reports
├── screenshot/          # Screenshots captured during test execution
├── test_cases/          # Test case scripts
├── test_data/           # Test data files
├── utilities/           # Utility functions and helpers
```

### Folders Description

- **base_pages/**: Contains base classes for Page Object Model, defining common functionalities for web pages.
- **configurations/**: Contains configuration files and settings required for the test execution.
- **logs/**: Contains log files generated during test execution.
- **reports/**: Contains test execution reports.
- **screenshot/**: Contains screenshots captured during test execution, useful for debugging.
- **test_cases/**: Contains the test case scripts.
- **test_data/**: Contains data files used for data-driven testing.
- **utilities/**: Contains utility functions and helper scripts.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with any enhancements or bug fixes. 

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Contact

For any questions or inquiries, please contact:
- **Suraj Behera** - surajbeheraqa@gmail.com
