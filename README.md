# Automated Website Visits

### Overview
Automated visit to website using:
- python script ```main.py``` which runs _Selenium_ on headless Chrome and
- script ```visit-castoma.yml``` that schedules runs of ```main.py``` via _GitHub workflows_

In our implementation we visit [this](https://castoma.streamlit.app/) streamlit app hosted on the Streamlit Community Cloud and activate it if it is found to be in sleep mode.

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**
