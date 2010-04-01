#!/usr/bin/env python

__title__ = 'Download all the Tweets For a Twitter Username'
__version__ = 0.11
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/48/download_tweets"
__copyright__ = "(C) 2010 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

"""
This program lets you post status updates to twitter. That's pretty much it for now.
"""

import json
import urllib

def get_tweets():
    print 'Enter your username (e.g. Lucers) below.'
    username = raw_input('Username: ')
    # initialize tweets page number
    page = 0 
    # initialize flag to continue loading pages
    more = True 
    # initialize the tweet keys we want to keep
    keys = 'created_at text'.split(' ')
    # initialize filename
    filename = 'Tweets_%s.txt' % (username)
    # write column headings
    tweetfile = open(filename, 'w')
    tweetfile.write('Tweet\tPosted\n')
    tweetfile.close()
    while more == True and username != '':
        # initialize output array
        simple_tweets = [] 
        # increment page number
        page += 1
        print 'Fetching page %s...' % (page)
        url = 'http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&page=%s' % (username, page)
        #TODO: investigate adding a &count=3200 parameter to the URL
        output = urllib.urlopen(url)
        contents = output.read()
        tweets = json.loads(contents)
        if len(tweets) == 0: 
            more = False
        else:
            for tweet in tweets:
                this_tweetlist = [tweet[key] for key in keys]
                # print str(this_tweetlist)
                this_tweet = '%s\n' % ('\t'.join(this_tweetlist))
                this_tweet = this_tweet.encode('utf-8', 'replace')
                tweetfile = open(filename, 'a')
                tweetfile.write(this_tweet)
                tweetfile.close()
    tweetfile = open(filename, 'r')
    lines = tweetfile.read().split('\n')
    tweetfile.close()
    print 'Download complete with %s tweets archived. All your tweets are in tab-delimited format in %s.' % (len(lines), filename)

if __name__ == '__main__':
    get_tweets()
    
