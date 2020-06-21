FROM mysql:8.0.20

# Set debian default locale to ja_JP.UTF-8
RUN apt-get update && \
    apt-get install -y locales && \
    rm -rf /var/lib/apt/lists/* && \
    echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8

ENV MYSQL_ROOT_PASSWORD=reporter

COPY mysql/conf/my.cnf /etc/mysql/conf.d

CMD ["mysqld"]
