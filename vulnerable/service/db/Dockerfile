FROM mariadb:11.4

HEALTHCHECK --start-period=10s --interval=10s --timeout=5s --retries=3 \
    CMD [ "healthcheck.sh", "--connect", "--innodb_initialized" ]

COPY vulnerable.sql /docker-entrypoint-initdb.d/
