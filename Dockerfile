# set base image (host OS)
FROM python:3.12

# set the working directory in the container
WORKDIR /app

COPY . .

RUN pip install -e ".[testing]"

EXPOSE 6543

CMD [ "pserve", "development.ini" ]