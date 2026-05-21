# Restful-Booker API Automation

A Python-based regression automation framework for the Restful-Booker API. This repository combines a modular Pytest suite, JSON schema checks, Allure reporting, and Jenkins CI integration to support reliable API validation.

## What this project contains

- API automation tests written in Python using `pytest`
- Data-driven and contract validation using `jsonschema`
- Postman collection and Newman artifact support in `Postman/`
- Jenkins pipeline definition in `Jenkinsfile`

## Project structure

```text
restful-booker-api-automation/
├── Jenkinsfile
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── Tests/
│   ├── conftest.py
│   ├── test_01_smoke.py
│   ├── test_03_crud_operations.py
│   ├── test_04_integration.py
│   ├── test_05_booking_negative.py
│   └── test_06_schemas.py
├── Postman/
│   ├── Restful_Booker.postman_collection.json
│   └── postman_report.html
├── Utils/
│   ├── payloads.py
│   └── schemas.py
├── docs/                             # QA artifacts and strategy files (Word / Excel)
│   ├── Test Plan_Restful Booker.docx
│   ├── Test Summary Report_Restful Booker.docx
│   └── TestCases_Restful Booker.xlsx
```
## Prerequisites

- Python 3.12+ installed
- `pip` package manager available
- Java Runtime Environment (JRE) for Allure local report generation
- Jenkins server with Allure plugin if using CI

## Install dependencies

From the project root:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS / Linux:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run tests locally

Run the full test suite:

```bash
python -m pytest
```

Run the smoke tests only:

```bash
python -m pytest -m smoke
```

Run the integration tests only:

```bash
python -m pytest -m integration
```

Run with verbose output:

```bash
python -m pytest -v -s
```

## Generate Allure report

Run tests and save results:

```bash
pytest Tests --alluredir=allure-results
```

Serve the Allure report locally:

```bash
allure serve allure-results
```

## Jenkins integration

This repository includes `Jenkinsfile` at the root. The pipeline is configured for Windows agents and performs these stages:

1. Checkout repository code from SCM
2. Create a Python virtual environment in `.venv`
3. Install dependencies from `requirements.txt`
4. Run tests with Allure result generation in `allure-results/`
5. Publish Allure reports using the Jenkins Allure plugin
6. Archive `allure-results/` and `allure-report/`

### Jenkins configuration notes

- Create a Jenkins Pipeline job and point it to this repository
- Set the job to use the root `Jenkinsfile`
- Confirm the Jenkins agent has Python installed and `pip` available
- Install the Allure Jenkins plugin and configure an Allure tool named `allure`
- Update `PYTHON_PATH` in `Jenkinsfile` if the agent uses a different Python install path

### Sample Jenkins agent commands

Windows batch execution (from `Jenkinsfile`):

```bat
"%PYTHON_PATH%" -m venv .venv
call .venv\Scripts\activate.bat
"%PYTHON_PATH%" -m pip install --upgrade pip
pip install -r requirements.txt
pytest Tests --alluredir=allure-results
```

If using Linux or macOS agents, replace Windows batch commands with Bash commands:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest Tests --alluredir=allure-results
```

## Dependencies

This project installs the following Python packages:

- `requests`
- `pytest`
- `jsonschema`
- `allure-pytest`
- `pytest-order`

## Notes

- `allure-report/` is generated output and can be regenerated from `allure-results/`
- Keep `allure-results/` clean between runs if you need fresh report data
- Use `pytest -m <marker>` to execute targeted suites by marker

## Useful commands

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
source .venv/bin/activate         # macOS / Linux
pip install -r requirements.txt
python -m pytest
allure serve allure-results
```

- 🧪 [View Live Interactive Postman Report](https://amrutha-tester.github.io/restful-booker-api-automation/Postman/postman_report.html)
