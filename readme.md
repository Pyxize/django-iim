## Django IIM App

### Make migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
### Load fixtures
```bash
python manage.py loaddata person.json
python manage.py loaddata category.json
python manage.py loaddata article.json
```
### Display local app
```bash
python3 manage.py runserver
```