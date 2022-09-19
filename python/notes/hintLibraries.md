# PIP

### How import python libraries in VSCode
Create [Project Folder]
Open VSCode
Open Folder in VSCode
Create Main Fyle main.py
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
// capture requirements to install
pip freeze > requirements.txt

// install requirements from requirements.txt
pip install -r requirements.txt

### Create VENV
Create a virtual environment#
To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:
```
macOS/Linux
You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

Windows
You can also use 
py -3 -m venv .venv
python -m venv .venv
```
### TO ACTIVATE VENV
Restart Terminal (optionally)
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.venv\scripts\activate
```
### TO DEACTIVATE VENV
deactivate

#UPGRADE PIP:
pip install -U setuptools
D:\.......\Python\.venv\scripts\python.exe -m pip install --upgrade pip


Better to add venv to workspace like this:
```
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
```

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