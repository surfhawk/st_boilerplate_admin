# Base image
FROM python:3.11-slim
MAINTAINER Daniel Park <surfhawk@naver.com>

# Install Git and cron
RUN apt-get update && apt-get install -y git cron openssh-server vim
RUN apt-get install -y libssl-dev sqlite3 libsqlite3-dev mariadb-client # default-mysql-client

RUN pip install --upgrade pip

# Arguments
ARG REPO_NAME
ARG APP_NAME
ARG APP_HOST
ARG APP_PORT

ENV REPO_CODEHOME="/${REPO_NAME}"
ENV PYTHONPATH="${REPO_CODEHOME}:${PYTHONPATH}"

VOLUME ["/root/opt"]

# Copy the codebase
COPY ./${REPO_NAME} ${REPO_CODEHOME}

# Install the requirements
WORKDIR ${REPO_CODEHOME}

RUN pip install --no-cache-dir -r ${REPO_CODEHOME}/requirements.txt
RUN echo "${REPO_NAME} -> ${REPO_CODEHOME} : Completed copy and installed requirements"
RUN echo APP_NAME is "${APP_NAME}"

# register command 'll' into bash
RUN echo "alias ll='ls --color=auto -alF'" >> ~/.bashrc
# RUN ~/.bashrc

ENV APP_NAME=${APP_NAME}
ENV APP_HOST=${APP_HOST}
ENV APP_PORT=${APP_PORT}

EXPOSE ${APP_PORT}

# run streamlit app service
WORKDIR ${REPO_CODEHOME}/${APP_NAME}

RUN echo streamlit run home.py --server.port {APP_PORT} --server.address {APP_HOST}
CMD streamlit run home.py --server.port ${APP_PORT} --server.address ${APP_HOST}
# CMD tail -f /dev/null
