#python -m uvicorn asgi:app --host 0.0.0.0 --port 3000 --reload
#gunicorn --bind=0.0.0.0 --timeout 600 wsgi:app
#gunicorn --bind=0.0.0.0 --timeout 600 main:app -w 1 -k uvicorn.workers.UvicornWorker
gunicorn --bind=0.0.0.0 --timeout 600 fastapi_plotly.main:app -w 1 -k uvicorn.workers.UvicornWorker