FROM python:3.10-slim

MAINTAINER Nils Ost

ENV HOME /app

WORKDIR $HOME

RUN apt update \
 && apt install -y --no-install-recommends iputils-ping

ADD requirements.txt $HOME/
RUN pip3 install -r $HOME/requirements.txt

ADD helpers.py $HOME/
ADD collectors.py $HOME/
ADD main.py $HOME/

EXPOSE 8080/tcp

ENTRYPOINT ["python3"]
CMD ["main.py"]
