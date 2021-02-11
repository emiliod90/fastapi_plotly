#python -m uvicorn asgi:app --host 0.0.0.0 --port 3000 --reload
#gunicorn --bind=0.0.0.0 --timeout 600 wsgi:app
gunicorn --bind=0.0.0.0 --timeout 600 asgi:app -w 2 -k uvicorn.workers.UvicornWorker
