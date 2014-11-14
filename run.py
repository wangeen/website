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
        script("uwsgi --http :8000 --chdir /root/website --module django_wsgi")
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
