Step1 --> create folder ki class-1-onsite -->.gemini install ke folder me phir open karen ge terminal me hum gemini.md ki file 2 nazar ayen gi .1 gemini.md ki file hum khud create kareng terminal me duri gemini.md ju hum ne gemini install kia hai

GEMINI.md  ---> file

Step2

1.Initialze a project with UV package manager.
2.Make a virtual environment using UV..
3.Also activate the virtual environment.

step Use the UV package manager not the PIP

Step3
Initialize the Project using UV and install fastapi

step uv pip install fastapi  

Step4
In main.py initialize the fastapi server.

step 5 
UV pip install unicorn

step6 google mein likhengy
localhost:8000

For docs: http://localhost:8000/docs



GEMINI CLI
Book Reference:
Book URL:- https://ai-native.panaversity.org/

Sunday Afternoon Repo URL:- https://github.com/jawwad-ali/Sunday-Afternoon-Q4

Basic Commands for GEMINI-CLI
/auth: to authenticate the user
/memory: to show, add, refresh and list memory
/clear: Clear the screen and conversation history
/model: To change the model
Memory or Context
When talking about memory or the context it is a know fact that we are talking about GEMINI.md
memory or context = GEMINI.md

Destinations for Gemini.md
There are 3-5 levels where we can define GEMINI.md file
Root/Home Directory
1.1 C:\Users\Ali.gemini\GEMINI.md - It impacts every project that user GEMINI-CLI. It is mainly used to define the rules that should be applied on every project

1.2 Project Level GEMINI.md - Only impacts the particular project.

1.3 Module Level GEMINI.md - Beneficial to give GEMINI-cli instructions related to a module/feature

Features like Tech Stack, Test cases, Multi lingual etc can be written in project specific GEMINI.md.

FASTAPI
Initialize a Projects through UV
Create/activate a virtual env(optional)
Start making Instances and endpoint (do this by prompt)
To Access FASTAPI ENDPOINTS
http://localhost:8000

For docs: http://localhost:8000/docs

2.1 To request the endpoint expand the Bar
2.2. Click on Try it out
2.3 Click on execute
Start the Server: uv run uvicorn main:app --reload

3.1 main = your Python file name (main.py)
3.2 app = the FastAPI instance variable name
3.3 --reload = auto-restart on code changes
3.4 Uvicorn = The server that actually runs and serves your FastAPI app to users
Deposit Module
Prompt for the deposit module
Create an endpoint for deposit asking users the amount to deposit. Make sure to update the bank_balance after depositing

HOMEWORK
Make an API route with the endpoint /authenticate.

The user should be asked for his/her name and pin_number

Make an endpoint named /bank-transfer

The user should be asked for the receipents_name and the amount to trnasfer

After transfering the amount, the amount should be deducted from the sender and should be added to the receiver's accounts.

After bank-transfer hit the authenticate with route again with the name of the person to whom you have transfered the amount.

After authenticating from the receiver's account you should be able to see the amount added to the person bank_balance"# FastAPI_Deposit-Module_Gemini_CLI" 
# FASTAPI-develop-a-Banking-System
