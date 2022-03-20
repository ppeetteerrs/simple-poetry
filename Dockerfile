FROM ppeetteerrs/python:latest

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY requirements_dev.txt /tmp/
RUN pip install --requirement /tmp/requirements_dev.txt

CMD ["zsh"]