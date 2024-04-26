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

ENV REPO_CODEHOME="/${REPO_NAME}"
ENV PYTHONPATH="${REPO_CODEHOME}:${PYTHONPATH}"

VOLUME ["/root/opt"]

# Copy the codebase
COPY ./${REPO_NAME} ${REPO_CODEHOME}

WORKDIR ${REPO_CODEHOME}
# Install the requirements
RUN pip install --no-cache-dir -r ${REPO_CODEHOME}/requirements.txt
RUN echo "${REPO_NAME} -> ${REPO_CODEHOME} : Completed copy and installed requirements"

# register command 'll' into bash
RUN echo "alias ll='ls --color=auto -alF'" >> ~/.bashrc
# RUN ~/.bashrc

ENV APP_HOST=127.0.0.1
ENV APP_PORT=8501

EXPOSE ${APP_PORT}

# run streamlit app service
WORKDIR ${REPO_CODEHOME}
CMD streamlit run ${APP_NAME}/home.py --server.port ${APP_PORT} --server.address ${APP_HOST}
#CMD tail -f /dev/null
