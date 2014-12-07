#!/usr/bin/env python
import subprocess
import argparse


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",  "--develop_server",  help="django default develop server", action='store_true')
    parser.add_argument("-u",  "--uwsgi_server",  help="uwsgi server", action='store_true')

    args = parser.parse_args()
    if args.develop_server:
        script("python manage.py runserver")
    elif args.uwsgi_server:
        #script("uwsgi --socket=/tmp/pyapp.socket --chdir /home/jwang/website --module django_wsgi --chmod-socket=666")
        # sample sudo uwsgi -b 25000 --chdir=/www/python/apps/pyapp --module=wsgi:application --env DJANGO_SETTINGS_MODULE=settings --socket=/tmp/pyapp.socket --cheaper=8 --processes=16  --harakiri=10  --max-requests=5000  --vacuum --master --pidfile=/tmp/pyapp-master.pid --uid=220 --gid=499
        # http://stackoverflow.com/questions/14962289/bad-django-uwsgi-performance
        script("sudo uwsgi --daemonize /home/jwang/website_logs/uwsgi.log "
                      " --socket=/tmp/pyapp.socket "
                      " --chdir /home/jwang/website "
                      " --module django_wsgi "
                      " --chmod-socket=666")
    else:
        parser.print_help()




#    parser.add_argument("-r",  "--run",  help="run local server", action='store_true')
#    if args.message:
#        print "start script"
#        ## TODO,  to be added here
#        print "end script"
#    elif args.run:
#    else:
#        parser.print_help()
