FROM python:3.7-alpine

ARG project_dir=/src

WORKDIR ${project_dir}

COPY ./src ${project_dir}

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD ["python3", "main.py"]
