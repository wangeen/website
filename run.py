#!/usr/bin/env python
import subprocess
import argparse


def script(cmd):
    print cmd
    subprocess.call(cmd, shell=True)


if __name__  == "__main__":
    script("python manage.py runserver")




#    parser = argparse.ArgumentParser()
#    parser.add_argument("-m",  "--message",  help="this is sample python script", action='store_true')
#    parser.add_argument("-r",  "--run",  help="run local server", action='store_true')
#    args = parser.parse_args()
#    if args.message:
#        print "start script"
#        ## TODO,  to be added here
#        print "end script"
#    elif args.run:
#    else:
#        parser.print_help()