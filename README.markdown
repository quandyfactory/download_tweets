##Download Tweets

Download all the Tweets For a Twitter Username

## Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Homepage: [http://quandyfactory.com/projects/48/download_tweets](http://quandyfactory.com/projects/48/download_tweets)
* Repository: [http://github.com/quandyfactory/download_tweets](http://github.com/quandyfactory/download_tweets)

## Licence

Released under the GNU General Public Licence, Version 2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.html](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html)

## This Version

* Version: 0.1

* Release Date: 2010-03-31

## Revision History

### Version: 0.1

* Release Date: 2010-03-31

* Changes:

    * First commit.

## Using Download Tweets
    
It's pretty simple to use. [Download](http://github.com/quandyfactory/download_tweets) download_tweets.py and save it somewhere. Then, just execute it. (*nix uses might have to set execute permissions.)

The script will prompt you to enter the Twitter username you want to download. Then it will download all of that user's tweets and save them in a tab-delimited text file named `Tweets_*Username*.txt`.

## Notes

* The twitter API will only let you download [the most recent 3,200 tweets](http://apiwiki.twitter.com/Things-Every-Developer-Should-Know). (Don't worry - all your tweets are still in their database. They eventually plan to make them all available.)

* The Twitter API also [limits the number of data requests](http://apiwiki.twitter.com/Rate-limiting) to 150 per hour. At 20 tweets per page, that means you're actually limited to 3,000 tweets.

## Planned Features

* See about downloading more than 20 tweets per page to reduce HTTP GET requests per hour.

* Add validation to fail gracefully if the user reaches the 150 requests per hour limit. Right now it throws an error.

