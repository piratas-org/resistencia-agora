#!/usr/bin/env bash

PIDFILE={{agora.virtualenv.root}}/agora-celery.pid
ROOTD={{agora.root}}
cd $ROOTD

if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

ps aux | grep "{{agora.virtualenv.root}}/bin/python $ROOTD/manage.py celery worker --pidfile=$PIDFILE -B -S djcelery.schedulers.DatabaseScheduler" | awk '{print $2}' | xargs kill -9

{{agora.virtualenv.root}}/bin/python $ROOTD/manage.py celery worker --pidfile=$PIDFILE -B -S djcelery.schedulers.DatabaseScheduler
