#!/bin/python3

import datetime
import os 
def do_magic():
    now = datetime.datetime.now()
    return "Hello my friend {0}".format(now)

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [do_magic().encode()]

if __name__ == "__main__":
    if 'REQUEST_URI' is os.environ:
        print("Content-type: text/html\n\n")
    print(do_magic())
