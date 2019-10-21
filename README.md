# Jupyter Lab Base

_Barebone install of `jupyterlab`_

Example run:
```sh
docker run --rm -v $HOME/notebooks:/data:rw -p 8999:8080 -e EXTERNAL_PORT=8999 nicklarsennz/jupyter-base:latest
```
_See: [run.sh][run]_

## Extend this image

```Dockerfile
FROM nicklarsennz/jupyter-base:latest

COPY requirements.txt .
RUN pip install --user -r requirements.txt
```

## Environment

| Variable | Default | Purpose |
| --- | --- | --- |
| EXTERNAL_HOST | localhost | Jupyter will print a URL for this host to stdout |
| EXTERNAL_PORT | 8080 | Jupyter will print a URL with this port to stdout |

## Additional Info

- Python 3.7
- Jupyer [Security Disabled][config] **Intended for local use**
- The image runs as user `jupyter`
- Working Directory: `/home/jupyter`
- Notebooks Directory: `/data/` (Mount your notebooks folder here)

[run]: ./run.sh
[config]: ./config.py
