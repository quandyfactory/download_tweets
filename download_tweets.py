#!/usr/bin/env python

"""
This program lets you download all the tweets for a given Twitter username.
"""

__title__ = 'Download Tweets'
__version__ = 0.5
__author__ = "Ryan McGreal ryan@quandyfactory.com"
__homepage__ = "http://quandyfactory.com/projects/48/download_tweets"
__copyright__ = "(C) 2010 by Ryan McGreal. Licenced under GNU GPL 2.0\nhttp://www.gnu.org/licenses/old-licenses/gpl-2.0.html"

import datetime
import json
import urllib
import optparse
import sys

def filename_datestamp():
    """Returns the current date/time stamp in string format friendly for filenames"""
    return str(datetime.datetime.now())[:-7].replace(':', '-').replace(' ', '_')

def get_tweets(username, filename):
    if not username:
        print 'Enter your username (e.g. RyanMcGreal) below.'
        username = raw_input('Username: ')
    # initialize tweets page number
    page = 0 
    # initialize flag to continue loading pages
    more = True 
    # initialize the tweet keys we want to keep
    keys = 'created_at text'.split(' ')
    # initialize filename
    if not filename:
        filename = 'Tweets_%s_%s.tsv' % (username, filename_datestamp())
    # write column headings
    tweetfile = open(filename, 'w')
    tweetfile.write('ID\tDate_Posted\tTweet\n')
    tweetfile.close()
    while more == True and username != '':
        # initialize output array
        simple_tweets = [] 
        # increment page number
        page += 1
        print 'Fetching page %s...' % (page)
        url = 'http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&page=%s&count=3200' % (username, page)
        #print 'url = %s' % (url)
        output = urllib.urlopen(url)
        contents = output.read()
        try:
            tweets = json.loads(contents)
        except:
            tweets = []
        if len(tweets) == 0: 
            more = False
        try:
            error = tweets['error']
            print
            print "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
            print "* "
            print "* ERROR: %s" % (error)
            print "* "
            print "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
            print
            more = False
        except:
            for tweet in tweets:
                this_tweet = '%s\t%s\t%s\n' % (tweet['id_str'], tweet['created_at'], tweet['text'])
                this_tweet = this_tweet.encode('utf-8', 'replace')
                tweetfile = open(filename, 'a')
                tweetfile.write(this_tweet)
                tweetfile.close()
    tweetfile = open(filename, 'r')
    lines = tweetfile.read().split('\n')
    tweetfile.close()
    
    print 'Download complete. Archived tweets are in tab-delimited format in %s.' % (filename)

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-u", "--user", dest="username", help="Downloads tweets for USER", metavar="USER")
    parser.add_option('-o', '--output', 
                      dest="output_filename", 
                      help = "Save output to FILE",
                      metavar="FILE",
                      )
    
    options, remainder = parser.parse_args()
    get_tweets(options.username, options.output_filename)
    
