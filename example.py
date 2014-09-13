#!/usr/bin/env python

import googleplay
import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print >> sys.stderr, 'SYNTAX: example.py [app-package-name]'
        sys.exit(-1)
        
    #To accept the package name of the app and pass it to all other functions
    googleplay.searchApp(args[0])
    
    #get the Title of the app
    googleplay.getAppTitle(1)
    
    #get the lastest update date
    googleplay.getAppDeveloper(1)
    
    #get the dev link
    googleplay.getAppDevLink(1)
    
    #get the lastest update date
    googleplay.getAppUpdateDate(1)
    
    #get the app rating
    googleplay.getAppRating(1)
    
    
