# PIP

### How import python libraries in VSCode
Create [Project Folder]
Open VSCode
Open Folder in VSCode
Create Main File main.py
Open VSCode Terminal
Create Virtual environment
Type in terminal: python -m venv [Path to Project Folder]\.venv

### Pip Install lib
pip install [libname]
pip install matplotlib
Click Run

### Emergency Pip install
```
\.venv\Lib\site-packages\setuptools\command\easy_install.py
\.venv\Scripts\get-pip.py
```
### Save/Install pip Packages To/From list
Capture requirements to install

`pip freeze > requirements.txt`

Install requirements from requirements.txt

`pip install -r requirements.txt`

### Pip List Outdated

`pip list -o`

### Pip Upgrade One Package

`pip install PACKAGENAME -U`

### Pip Upgrade All Packages
Works on Windows. Should be good for others too.
($ is whatever directory you're in, in command prompt. eg. C:/Users/Username>)

do

    $ pip freeze > requirements.txt

open the text file, replace the `==` with `>=` , and execute 


    $ pip install -r requirements.txt --upgrade

If you have a problem with a certain package stalling the upgrade (numpy sometimes), just go to the directory ($), comment out the name (add a # before it) and run the upgrade again. You can later uncomment that section back. This is also great for copying python global environments.

___
**Another way:**

I also like the pip-review method:
    
    py2
    $ pip install pip-review

    $ pip-review --local --interactive

    py3
    $ pip3 install pip-review

    $ py -3 -m pip_review --local --interactive

You can select 'a' to upgrade all packages; if one upgrade fails, run it again and it continues at the next one.



# Jupyter

Disable Jupyter Keymap extension


#########################################################
######## VSCODE ENVIRONMENT##############################
#########################################################
How import python libraries in VSCode

Create [Project Folder]
Open VSCode
Open Folder in VSCode
Create Main Fyle main.py

Open VSCode Terminal
Create Virtual environment
Type in terminal: python -m venv [Path to Project Folder]\.venv
TO ACTIVATE VENV

Restart Terminal (optionally)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate

pip list

pip install [libname]
pip install matplotlib

Click Run

pip uninstall [libname]

TO ACTIVATE VENV

Restart Terminal (optionally)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate
deactivate


UPGRADE PIP:
pip --version
D:\.......\Python\.venv\scripts\python.exe -m pip install --upgrade pip


Better to add venv to workspace like this:

{
	"folders": [
		{
			"path": "Python"
		}
	],
	"settings": {
		"files.autoSave": "onFocusChange",
		"python.pythonPath": ".venv\\Scripts\\python.exe"
	}
}

# Format code
pip install autopep8
pip install pep8
ctrl sh p : >Format document with >python

#########################################################

559

This will work for all Mac, Windows, and Linux systems. To get the list of all pip packages in the requirements.txt file (Note: This will overwrite requirements.txt if exist else will create the new one, also if you don't want to replace old requirements.txt then give different file name in the all following command in place requirements.txt).

pip freeze > requirements.txt
Now to remove one by one

pip uninstall -r requirements.txt
If we want to remove all at once then

pip uninstall -r requirements.txt -y