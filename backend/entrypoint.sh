set +e 
echo "==> Django setup, executing: makemigrations "
python3 manage.py makemigrations
echo "==> Django setup, executing: migrate pro"
python3 manage.py migrate
echo "==> Django setup, executing: collectstatic"
python3 manage.py collectstatic --settings=pill.settings --no-input 

gunicorn pill.wsgi:application --bind 0.0.0.0:8980