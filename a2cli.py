#!/usr/bin/env python3

### simple python script to roughly emulate the Andromeda CLI interface over HTTP ###

import os, sys, requests, json

#TODO interactively get input (passwords)
#TODO load URL from environment variable!
#TODO load environment variables andromeda_*
#TODO changing file name

def exithelp():
    print("usage: a2cli.py url app action [--file name] [--$param data] [--$param@ file]")
    sys.exit(1)

def backend(url, app, action, post={}, files=None):

    params = {'app':app,'action':action}
    resp = requests.post(url,params=params,data=post,files=files)

    if resp.headers.get('content-type') == 'application/json':
        return resp.json()
    else: return resp.content


if __name__ == '__main__':

    args = sys.argv[1:]

    if (len(args) < 3):
        exithelp()

    url = args[0]
    app = args[1]
    action = args[2]

    args = args[3:]
    params = { }
    files = { }

    i = 0    
    while i < len(args):

        key = args[i]; i+=1

        if key[0:2] != "--": exithelp()
        else: key = key[2:]

        if len(args) > i and args[i][0:2] != "--":
            value = args[i]; i+=1
        else: value = "null"

        if key[-1] == '@':
            key = key[:-1]
            value = open(value,'rb').read().strip()

        if key == 'file':
            name = os.path.basename(value)
            files["file"+str(i)] = (name,open(value,'rb'))
        else: params[key] = value

    result = backend(url, app, action, params, files)

    if type(result) is dict:
        result = json.dumps(result, indent=4)

    print(result)