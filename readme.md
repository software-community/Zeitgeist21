# Official Website of Zeitgeist'21, IIT Ropar

## Development setup
Ensure `python3` and `node` is installed on the machine.

1. Make a new virtual enviornment
```bash
python -m <venv-name> <path>
```
2. Activate the environment
* For Windows Powershell
  ```bash
  <venv-name>/Scripts/activate
  ```
* For Linux
  ```bash
  source ./<venv-name>/bin/activate
  ```
3. Clone the repository
```bash
  git clone <url>
```
4. Navigate to the cloned folder
5. Install all python dependencies
```bash
pip install -r requirements.txt
```
6. Intall all node dependenices
```bash
npm i
```
7. Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
8. Create a superuser
```bash
python manage.py createsuperuser
```

## Development startup
1. Activate the virtual environment
2. Navigate to the git folder
3. Run the development server
```bash
python manage.py runserver
```
4. Run the node command (in another terminal)
```bash
npm run css
```
5. The website will become live at [127.0.0.1:8000](http://127.0.0.1:8000/)
6. To access the admin panel, navigate to [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)