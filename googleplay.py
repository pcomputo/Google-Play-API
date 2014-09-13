#!/usr/bin/env python

from bs4 import BeautifulSoup
import sys
import urllib
import urllib2
import json

package = ""

#Entry point
def searchApp (pack):
    global package
    package = pack
   
#Creates the soup
def createSoup():
    global package
    url = "https://play.google.com/store/apps/details?id=" + package
    try:
        response = urllib.urlopen( url )
    except urllib.error.HTTPError as e:
        print( "HTTPError with: ", url, "\t", e )
        return None
        
    the_page = response.read()
    soup = BeautifulSoup( the_page )   
    
    return soup

def getAppTitle(display):
    soup = createSoup()
    
    title_div = soup.find( 'div', {'class':'document-title'} )
    title = title_div.find( 'div' ).get_text().strip()
    
    if display:
        print title
        
    return title
     
def getAppUpdateDate(display):
    global package
    soup = createSoup()

    date_published_div = soup.find( 'div', {'itemprop' : 'datePublished'} )
    updated = date_published_div.get_text().strip()
    
    if display:
        print updated
    
    return updated
    
    
def getAppUpdate(display):
    global package
    soup = createSoup()
    
    change = []
    changes_div = soup.find_all( 'div', {'class':'recent-change'}  )
    for changes in changes_div:
        change.append(changes.get_text().strip())
        #print change
        
    if display:
        for log in change:
            print log
        
    return change
    
    
def getAppReviews(display):
    global package
    reviews = []
    i = -1
    cur = 0
    while True:
        i += 1
        url = "https://play.google.com/store/getreviews"
        data = "reviewType=0&pageNum=" + str(i) + "&id=" + package + "&reviewSortOrder=4&xhr=1"
        headers = { "orgin" : "https://play.google.com",
                    "accept-language": "en-US,en;q=0.8",
                    "user-agent": "Mozilla/5.0 (X1; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "accept": "*/*",
                    "referer": "https://play.google.com/store/apps/details?id="+package}
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()[6:]
        js = json.loads(the_page)
        page = js[0][2]
        try:
            if not page:
                raise IndexError
            soup = BeautifulSoup( page )
        except IndexError:
            break

        if not soup: return None
        reviews_div = soup.find_all( 'div', {'class':'single-review'} )
        for review in reviews_div[:10]:
            cur += 1
            if display:
             print str(cur)+')', review.find(class_='author-name').get_text().strip(), review.find(class_='tiny-star').get('aria-label').strip(), 'On', review.find(class_='review-date').get_text().strip()
            
            body = review.find(class_='review-body')
            title = body.find(class_='review-title')
            link = body.find(class_='review-link')
            text = title.get_text().strip()
            if display:
                print 'TITLE:', text and text or '(no title)'
            title.decompose()
            link.decompose()
            text = body.get_text().strip()
            reviews.append(text)

            if display:
                print 'REVIEW:', text and text or '(no content)'
                print
        if cur % 20 != 0:
            break

    print 'TOTAL REVIEWS:', cur
    return reviews


def getAppDetails(display):
    global package
    comment = []
    i = -1
    cur = 0
    while True:
        i += 1
        url = "https://play.google.com/store/getreviews"
        data = "reviewType=0&pageNum=" + str(i) + "&id=" + package + "&reviewSortOrder=4&xhr=1"
        headers = { "orgin" : "https://play.google.com",
                    "accept-language": "en-US,en;q=0.8",
                    "user-agent": "Mozilla/5.0 (X1; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                    "accept": "*/*",
                    "referer": "https://play.google.com/store/apps/details?id="+package}
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()[6:]
        js = json.loads(the_page)
        page = js[0][2]
        try:
            if not page:
                raise IndexError
            soup = BeautifulSoup( page )
        except IndexError:
            break

        if not soup: return None
        reviews_div = soup.find_all( 'div', {'class':'single-review'} )
        for review in reviews_div[:10]:
            reviews = []
            cur += 1
            if display:
             print str(cur)+')', review.find(class_='author-name').get_text().strip(), review.find(class_='tiny-star').get('aria-label').strip(), 'On', review.find(class_='review-date').get_text().strip()
            date = review.find(class_='review-date').get_text().strip()
            rating = review.find(class_='tiny-star').get('aria-label').strip()
            reviews.append(date)
            reviews.append(rating)
            body = review.find(class_='review-body')
            title = body.find(class_='review-title')
            link = body.find(class_='review-link')
            text = title.get_text().strip()
            if display:
                print 'TITLE:', text and text or '(no title)'
            title.decompose()
            link.decompose()
            text = body.get_text().strip()
            reviews.append(text)
            
            
            comment.append(reviews)
            if display:
                print 'REVIEW:', text and text or '(no content)'
                print
        if cur % 20 != 0:
            break

    print 'TOTAL REVIEWS:', cur
    return comment

if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print >> sys.stderr, 'SYNTAX: reviews.py [app-package-name]'
        sys.exit(-1)

    #getAppDetails(args[0],1)
    getAppUpdate(args[0],1)
