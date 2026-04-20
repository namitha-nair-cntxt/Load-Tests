# Load Testing for APIs using Locust

This contains load test scripts for different APIs .
It helps simulate multiple users, validate API responses, and measure performance under load.


## Project Structure

```bash
.
├── locustfile.py
└── README.md
-------------------------------------------------------------------------------------------------
**Prerequisites**

Make sure you have the following installed:
Python
pip
Locust

Install Locust using: pip install locust

-------------------------------------------------------------------------------------------------

**How to Run**

Run the following command from the project directory:
locust

Then open Locust UI in your browser: http://localhost:8089

Enter:
   1. Number of users
   2. Spawn rate
   3. Host if not already defined in script

Start the test and monitor the results in the Locust dashboard.

-------------------------------------------------------------------------------------------------
