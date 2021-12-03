
iAINTAINER AVDHUT_ULHARE 
RUN  apt-get update 
RUN apt-get install mysql-server  -y 
RUN apt-get update 
RUN service mysql start 

RUN mkdir /data/db
ADD new.sql /data/db
EXPOSE 2800
ENTRYPOINT usr/bin/mysql




