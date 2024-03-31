#starting celery beat and worker process
celery -A jobWebsite beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A jobWebsite worker -E -l info --logfile=celery.log --detach  #if you plan to detach worker process
celery -A jobWebsite worker -E -l info --logfile=celery.log #if you dont plan to detach worker process

#starting redis
redis-server --daemonize yes
redis-cli ping

Note: 
you are to start the redis daemonize first
then check its running with the ping command ,if it returns pong then you are good to go

Open two separate terminal process and run the above beat and worker process in different terminal
i.e the two celery commands must be running at the same time.

Then login to admin panel and Go to periodic tasks , you should see three periodic tasks who are disabled , enable the one you interested in starting

#note leave the backend cleanup tasks the way it is. Thanks 