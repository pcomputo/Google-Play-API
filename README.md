Google-Play-API
===============

This is used to get information about various entities like title, category, reviews, ratings, etc of a given app on Google Playstore.

Requirement:
============
1. Python 2.7+
2. BeautifulSoup API -- If running Ubuntu or likes the command is: sudo apt-get install python-bs4

Usage of the API:
=================

Provide the package name of the app to the function searchApp(). This is a compulsary line and beginning of the entry point of the API.
The package name can be found in the Playstore URL of the app. It occurs after the "?id=" parameter.

Every function accepts a boolean parameter for display. If it is set to True then the API prints the entity for which the function was invoked else it just returns the respective entity. 

In the file example.py some functions have been used to provide a brief usage of the API.

To accept the package name of the app and pass it to other functions use:

    googleplay.searchApp(args[0])

To get the Title of the app:

    googleplay.getAppTitle(True)
    
To get the lastest update date:

    googleplay.getAppDeveloper(True)
    
To get the dev link:

    googleplay.getAppDevLink(True)
    
and so on...

The highlight of this API is that all the reviews can be collected. The reviews generally are a large number and only the first 20 reviews are only static. The remaining reviews are loaded by AJAX thus crawling on them becomes difficult. But this API will let you get all the reviews under a given app. :)
