FROM ghcr.io/ppeetteerrs/python:3.8

RUN pip install poetry poetry-dynamic-versioning

CMD ["zsh"]