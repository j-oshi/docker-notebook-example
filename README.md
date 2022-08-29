# docker-jupyter-notebook
Docker image for a Jupyter Notebook <br >

## File structure
<pre>
Project:
    data:
        data generated goes to this folder
    nodebooks:
        __init__.py
        jupyter notebooks goes to this folder
    src:
        custom python modules goes to this folder
    .gitignore
    docker-compose.yml
        Dockerfile
        README.md
        requirements.txt
        setup.py
</pre>
## Setting up
### Run in venv
> python -m venv `environment name` <br >
> `environment name`\Scripts\activate <br >
> pip install --upgrade pip 
> pip install --upgrade setuptools
> pip install -r requirements.txt
> jupyter notebook
or
> jupyter notebook --port 9999

### Run in dockers
Launch docker on computer.<br >
Clone image from repository and cd into image folder. Open terminal add run the following commands below: 
 > docker-compose build --no-cache --pull <br >
 > docker-compose up -d --build <br >

#### Run
 > docker-compose start <br >
 > docker-compose stop <br >
#### Access
The default access point in browser is <br >
http://localhost:7777 <br >

#### Run example
Run jupyter notebook to generate data and table

#### To set and run with dockers
cd into folder <br >

