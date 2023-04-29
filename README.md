# Overview
This repository contains a set of files related to web UI automation testing. The "test plan.txt" file describes the test plan and test cases, while the "bug.doc" file contains a list of bugs that have been identified during testing. The tests folder contains all the test scripts used for testing.

# Files
## test plan.txt
This file contains a detailed description of the test plan and test cases. It outlines the scope, and approach to be taken during testing. It also describes the test environment, test data, and expected results. The test cases are organized according to their respective functional areas and cover both positive and negative scenarios.

## bug.doc
This file contains a list of bugs that have been identified during testing. Each bug is described in detail, including steps to reproduce, actual result and expected result. The list is organized by priority and severity to aid in bug triage and resolution.

## tests folder
This folder contains all the test scripts used for web UI automation testing.

# Usage
To use the files in this repository, simply download or clone the repository to your local machine. The "test plan.txt" file can be used to guide the testing process, while the "bug.doc" file can be used to track and manage bugs.
## Run the test scripts under tests folder
For using pytest command to run the test, you need to install pytest plugin first. You can simply run the following command in your terminal:
```
pip install pytest
```
Once the installation is complete, you can use the pytest command under "tests" folder to run the specified test case:
```
pytest test_B_1.py
```
Or you can execute all the test scripts under "tests" folder by the following command:
```
py.test
```


## Generate the test report
For generate the report, please install pytest-html plugin. 
To install the pytest-html plugin, you can use pip:
```
pip install pytest-html
```
You can run the generate_report.py in in your terminal to run all the test scripts and get the report under tests/report folder. 
```
python generate_report.py
```

# License
This repository is licensed under the GNU GENERAL PUBLIC LICENSE. See the LICENSE file for more information.