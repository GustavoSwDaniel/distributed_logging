FROM python:3.8-alpine3.19

WORKDIR /usr/simulate_services

COPY ./simulated_services .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "__init__.py" ]