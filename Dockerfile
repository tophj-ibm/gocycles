# Usage:
#
# # Assemble the full dev environment. This is slow the first time.
# docker build -t gocycles .
#
#

FROM ubuntu:16.04
RUN apt-get update && apt-get install -y -q python-all python-pip vim
ADD ./webapp/requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
ADD ./webapp /opt/webapp
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["python" , "app.py"]
