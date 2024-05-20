python -m PyInstaller login.py

*PREPARAÇÃO DO AMBIENTE VIRTUAL*

python3 -m venv gui_venv

pip freeze > requirements.txt

gui_venv\Scripts\Activate  

pip install -r requirements.txt
