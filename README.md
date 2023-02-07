- Follow these steps to run app.
1. pip3 install -r requirements.txt
2. cd /src
3. python3 manage.py makemigrations
4. python3 manage.py migrate
5. python3 manage.py runserver
6. Start Celery and celery beat: celery -A store_queue_tasks worker -B -l INFO

- Save email url: http://localhost:8000/api/v1/email_store/save_email
- List emails: http://localhost:8000/api/v1/email_store