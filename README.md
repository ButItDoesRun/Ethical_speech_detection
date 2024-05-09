# Ethical_speech_detection
A case study on Perspective API

OBS!
If you are not one of the authors of this project you cannot run the code. This is due to use of the API 'Perpective API', which requires authorized accesss. To create your own project follow the guide on Perpective API's webpage: https://developers.perspectiveapi.com/s/docs?language=en_US 

To run the code:
Go into your terminal and run this command for activating the virtualenv:
--> .venv\Scripts\activate
You also have to configure the 'run'-button in Visual Studio Code from 'Run Code' to 'Run Python file' to actually run the code in the virtual environment. You do this by clicking on the small arrow next to the run-button and choosing 'Run Python file'. 



Overview of API installation (commands were run in project terminal):
Prerequisite: an API key generated from your Google Cloud Console

1. install the package for creating a virtual environment:
--> pip install virtualenv

2. Create a new virtual environment:
--> py -m venv .venv

3. Activate the environment:
--> .venv\Scripts\activate

4. Install the package for google api client:
--> .venv\Scripts\pip.exe install google-api-python-client

NOTE: if you get an error about updating the pip version then use the below command to resolve it:
--> python.exe -m pip install –-upgrade pip

Dependencies:
numpy
pandas

