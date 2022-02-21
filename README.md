
# jsonplaceholder

This project includes tests of jsonplace holder fake APIs.

Python with BBD approach used to develop API testing.


## Run Locally

Install Python3 to your local machine

```bash
  https://www.python.org/downloads/
```

Clone the project

```bash
  https://github.com/oonursrc/testjsonplaceholder.git
```

Go to the project directory

```bash
  cd testjsonplaceholder
```

Create python virtual env

```bash
  python3 -m venv venv
```

Activate virtual env

```bash
  . venv/bin/activate
```

Install required packages

```bash
  pip install -r requirements.txt
```


## Running Tests

To run tests, run the following command

```bash
  python3 -m pytest tests/step_defs/steps.py --junitxml=test-reports/report.xml
```


## CircleCI

To run tests on CircleCI, run the following link

[CircleCI Page](https://app.circleci.com/pipelines/github/oonursrc/testjsonplaceholder?branch=main)
## FAQ

If you have Python SSL issue, please follow the link below

[Link](https://github.com/actions/setup-python/issues/93/)
