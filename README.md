## Structure
FastAPI built similar to the Factory Pattern

Folder structure:


Folder for each CRUD action

Inspired by https://github.com/rednafi/fastapi-nano/tree/master/%7B%7Bcookiecutter.repo%7D%7D/app 
And 
https://github.com/Buuntu/fastapi-react/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D
And 
https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D

startup.sh starts the deployment using gunicorn and uvicorn
see here for more: https://www.uvicorn.org/deployment/#gunicorn
gunicorn references asgi.py:app to instantiate FastAPI
main.py contains the callable function for building app = FastAPI() including all routes

### Dependencies used were:
See [tool.poetry.dependencies] in pyproject.toml for list of prod dependencies

Solved poetry issue using python2.7 by following https://github.com/python-poetry/poetry/issues/3184

### GINO
https://python-gino.org/docs/en/master/index.html


## CI/CD
### Prepare requirements
poetry export -f requirements.txt --output requirements.txt --without-hashes

### prepare in Git
git commit -m "first commit"
git branch -M main

### GitHub 
git remote add origin https://github.com/emiliod90/fastapi_plotly.git
git remote set-url --add --push origin https://github.com/emiliod90/fastapi_plotly.git
### Azure Repos
git remote set-url --add --push origin https://emydesouza@dev.azure.com/emydesouza/FastAPI%20Plotly%20App/_git/FastAPI%20Plotly%20App

git push -u origin --all
git push -u origin main



## Deployment
For azure make sure requirements.txt is in the project root and "startup.sh" is referenced as a Startup Command under Stack Settings in Azure Portal. See here for more: https://docs.microsoft.com/en-us/azure/app-service/configure-language-python 

In development I am using poetry
poetry run uvicorn asgi:app --host 0.0.0.0 --port 3000 --reload
Or
poetry run gunicorn --bind=0.0.0.0 --timeout 600 asgi:app -w 2 -k uvicorn.workers.UvicornWorker

In production Azure uses the startup.sh which runs gunicorn directly with 
gunicorn --bind=0.0.0.0 --timeout 600 asgi:app -w 2 -k uvicorn.workers.UvicornWorker

I chose to use Azure Pipelines
Use this guide https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops#create-an-azure-devops-project-and-connect-to-azure
Add this to the bottom of the azure-pipelines.yml
startUpCommand: 'gunicorn --bind=0.0.0.0 --timeout 600 fastapi_plotly.main:app -w 1 -k uvicorn.workers.UvicornWorker'

To use uvicorn directly, make sure the startup command invokes a python -m command instead of invoking the server directly, e.g.
python -m uvicorn application:app --host 0.0.0.0
see more here https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-app-service-on-linux-04#startup-commands-for-other-frameworks-and-web-servers
https://fastapi.tiangolo.com/deployment/manually/ 


## Notes
This was developed on Vagrant
If trouble with python3.8 set alias in ~/.bashrc
alias python = python3.8
