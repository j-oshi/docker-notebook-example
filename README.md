# docker-jupyter-notebook
Docker image for a Jupyter Notebook <br >

## File structure
<pre>
Project:
    data:
        data generated goes into this folder
    nodebooks:
        jupyter notebooks goes into this folder
    src:
        __init__.py
        custom python modules goes into this folder
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
> pip install --upgrade pip <br > 
> pip install --upgrade setuptools <br >
> python manage_pip install|uninstall packages
<!-- > pip install -r requirements.txt <br > -->
> jupyter notebook <br >
or <br >
> jupyter notebook --port 9999

### Run in dockers
Launch docker on computer.<br >
Clone image from repository and cd into image folder. Open terminal add run the following commands below: 
### Build image and run
 > docker-compose build --no-cache --pull <br >
 > docker-compose up -d --build <br >

#### To start and stop container
 > docker-compose start <br >
 > docker-compose stop <br >
#### Access
The default access point in browser is <br >
http://localhost:7777 <br >

#### Run example
Run jupyter notebook to generate data and table

#### To set and run with dockers
cd into folder <br >

#### Run managa_pip
The use of `pip freeze > -l > requirements.txt` to update the packages in requirements.txt has led to installation failure in some cases. <br >

The `pip freeze` command was found to appended incompatible packages from local environments that caused conflict in a different installation setting. Run the command below to install or uninstall packages and avoid installation failure. <br >

> python manage_pip install|uninstall packages

Running this script rather than use pip to install or uninstall packages will prevent the issue with pip freeze > -l > requirments.txt appending all packages from a local environment. <br >

When pip freeze command is used to update requirements file, there ia a likely probability of installation failure with a system with different python environment configuration. Pip freeze writes local environment packages with versions that might conflict with new environment packages. Running manage_pip appends or removes just the requested packages with exact version. <br >
> python manage_pip install|uninstall packages

