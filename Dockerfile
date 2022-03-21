FROM ghcr.io/ppeetteerrs/python:3.8

RUN pip install "poetry>=1.2.*" poetry-dynamic-versioning

CMD ["zsh"]