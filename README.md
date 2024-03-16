# pyTranslate
An extremely simple quick cross-platform translation tool. It is written in a simple main.py file. This script can be bound to a keyboard shortcut and integrates with any screenshot tool and text editor.

## Use
To use this tool, you simply need to have [Python](https://www.python.org/downloads/) installed. It is also recommended to use a virual environment to install dependencies which can be done using the following command.
```console
python3 -m venv venv-name
```
Next, activate the environment using the following command. On Linux,
```console
source venv-name/bin/activate
```
On Windows (one of these),
```console
venv-name\Scripts\activate
venv-name\Scripts\activate.bat
venv-name\Scripts\Activate.ps1
```
Install all dependencies from the requirements.txt file by using the following commands. On Linux,
```console
pip3 install -r requirements.txt
```
On Windows,
```console
pip install -r requirements.txt
```
Now simply run the main.py file using Python,
On Linux,
```console
python3 main.py
```
On Windows,
```console
python main.py
```

## Configuration
In main.py file, under the "Config" comment, certain variables are declared that can be changed and configured according to different systems/usecases.
- DIR_PATH : The directory path to where the image/screenshot is going to be saved
- IMG_NAME : Image name in the DIR_PATH with file extension
- TRANSLATE_FROM : Translate language source. It can be set to "auto" for auto-detection
- TRANSLATE_TO : Language to translate the image text
- SAVE_TO : The save path for the text file. By default, it is under the "translated" directory
- OPEN_WITH : The application used to auto-launch the translated text file using subprocess function
