<h1>API IRIS SCRAPING</h1>

<p>Rodar o conteiner</p>

# sudo docker run -it -v ~/Workspace://Workspace --rm -p 5000:5000 --name tensorflow-flask lexcrt/debian:flask-tensorflow /bin/bash 

<p>Exportar variavel app_name.py</p>

# export FLASK_APP=server.py
# export LC_ALL=C.UTF-8 && export LANG=C.UTF-8

# Rode

Run command  `python3.5 server.py`

**Test**

http://localhost:5000/?image_url=https://i.imgur.com/oDf68ZO.jpg