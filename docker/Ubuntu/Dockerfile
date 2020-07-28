FROM ubuntu:latest

WORKDIR /app
EXPOSE 80
EXPOSE 5000-8888


SHELL [ "/bin/bash","-c" ]


RUN apt update && \
    apt install -y python3-pip python3-dev\
    && cd /usr/local/bin\
    && ln -s /usr/bin/python3 python\
    && pip3 install --upgrade pip\
    && apt-get install -y curl vim less git highlight 


RUN curl --silent --location https://deb.nodesource.com/setup_12.x | bash -
RUN apt update && apt install -y nodejs build-essential && rm -rf /var/lib/apt/lists/*
RUN npm install -g yarn


COPY settings/.bashrc settings/.bash_aliases /settings/
COPY settings/vimrc.local /etc/vim/

CMD ["bash"]
