<h1>API IRIS SCRAPING</h1>

<p>Rodar o conteiner</p>

# sudo docker run -it -v ~/Workspace://Workspace --rm -p 5000:5000 --name tensorflow-flask lexcrt/debian:flask-tensorflow /bin/bash 

<p>Exportar variavel app_name.py</p>

# export FLASK_APP=api-iris.py
# export LC_ALL=C.UTF-8 && export LANG=C.UTF-8

<p>Subir o serve</p>

# flask run --host="0.0.0.0"