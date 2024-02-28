# Fingerprint Scanner Application

## Overview
The Fingerprint Scanner Application is a Python-based desktop application designed to facilitate employee attendance tracking through fingerprint recognition technology. This application integrates with a fingerprint scanner device to capture and process biometric data for verification purposes.

## Features
- Employee Attendance Tracking: Automatically logs employee presence based on fingerprint recognition.
- Integrated Database Management: Stores employee data securely and efficiently.
- User Interface: A graphical interface for easy interaction with the system.
- Testing and Verification: Built-in functionality for testing and verifying the accuracy of the fingerprint recognition system.

## Getting Started

### Prerequisites
Ensure that you have the following software installed on your system:
- Python  3.x
- PIP package manager
- Relevant Python libraries listed in requirements.txt

### Installation
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the application with `python main.py`.

## Usage
After starting the application, use the following steps to capture and verify fingerprints:
1. Select an employee ID from the dropdown menu.
2. Click the "Capture Fingerprint" button to start the fingerprint capture process.
3. Follow the on-screen instructions to complete the fingerprint capture.
4. Once captured, the fingerprint image will be displayed on the screen.
5. To verify the fingerprint against a database of registered employees, click the "Verify Fingerprint" button.

## Tests
To ensure the reliability of the application, we have included tests within the project. These tests cover the core functionalities of the application, including fingerprint capture and verification. To run the tests, execute the following command:

'''
bash python -m unittest discover

'''

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For further inquiries or support, please contact the maintainer at [engthanoon1@gmail.com].

