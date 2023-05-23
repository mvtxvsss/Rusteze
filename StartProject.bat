python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
Start http://localhost:8000/
python manage.py runserver

