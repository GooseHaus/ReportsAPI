# API Report Card Comment Generator

## **How to Run API**

0. If you are reading this file, it is likely you have already git cloned the required files for the API. If not, git clone the forum repository. You will need to have python installed (https://www.python.org/downloads/). Python 3.10.9 recommended. 

1. To use this API, you will need an API key from OpenAI. https://platform.openai.com/account/api-keys Set your API key as openai.api_key on line 7 of app.py as a str (using quotation marks)

2. In your console, terminal, or command prompt, navigate to ReportsAPI directory

3. While in the ReportsAPI directory, create a virtual environment in python; depending on the os and package installed, this command will either be:

        python -m venv venv

    or

        python3 -m venv venv

4. Activate the virtual environement. If you are working with a Windows machine, the command will be:

        venv\Scripts\activate

    or; if you are working on a Mac, the command will be:

        source venv/bin/activate

5. Install required packages in the virtual environment:

        pip install -r requirements.txt

6. Run the application using flask with the command:

        flask run

        *note: f this fails to run because it cannot find openai, it is likely you just need to restart the shell. Close and reopen your command prompt, navigate to the ReportsAPI directory  and re-complete steps 4 and 6 (NOT 5). 

7. Open a browser and navigate to http://127.0.0.1:5000 or http://localhost:5000/


## Usage
This API provides a way to generate report card comments based on student name, student grade, and course description. It uses OpenAI's Completion API to complete a text prompt based on the input data. The API is built with Flask, a lightweight web framework.

Input
The API takes in 3 inputs:

studentName: The name of the student being reported on.
studentGrade: The grade of the student, as an integer.
courseDesc: A description of the course being reported on.
Output
The API generates a report card comment, consisting of three sentences. The first two sentences must each include at least one entry from the list of words: thorough, high degree, extensive, comprehensive, in-depth, admirable, outstanding, tremendous (if the student grade is greater than or equal to 70) or considerable, significant, substantial, noteworthy, strong, ample (if the student grade is between 70 and 79). The third sentence must be a suggestion for how to improve. Most must be kept positive. All three sentences should be reasonably related to the course description. 
