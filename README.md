<h1>API IRIS SCRAPING</h1>

**Clone os repositorios**

<p>https://bitbucket.org/fmbcruz/iris/src/master/</p>
<p>https://github.com/cristianosantana/TensorFlowKeras.git</p>

**Subir o conteiner**

## sudo docker run -it -v ~/Workspace://Workspace --rm -p 5000:5000 --name tensorflow-flask lexcrt/debian:tensorflow-keras-v1 /bin/bash
## sudo docker run -it -v ~/Workspace://Workspace --rm -p 8080:8080 --name nodejs node:latest /bin/bash

**Exportar variavel app_name.py**

<p>export FLASK_APP=server.py</p>
<p>export LC_ALL=C.UTF-8 && export LANG=C.UTF-8</p>

**Roda o comando**

<p>python3.5 server.py</p>

<p>so roda no fire fox </p>

**Test**

<p>http://localhost:5000/?image_url=https://i.imgur.com/oDf68ZO.jpg</p>
