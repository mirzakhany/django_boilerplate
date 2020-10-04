#!/bin/sh

echo "Starting proj microservice"
exec uwsgi --ini uwsgi.ini
