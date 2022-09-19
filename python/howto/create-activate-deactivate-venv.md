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