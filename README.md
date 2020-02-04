<h1>API IRIS SCRAPING</h1>

<p>Rodar o conteiner</p>

# sudo docker run -it -v ~/Workspace://Workspace --rm -p 5000:5000 --name tensorflow-flask lexcrt/debian:flask-tensorflow /bin/bash 

<p>Exportar variavel</p>

# export FLASK_APP=hello.py

<p>Subir o serve</p>

# flask run --host="0.0.0.0"