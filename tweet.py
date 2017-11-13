
import requests
import oauth2 as oauth
import os
import urllib
import argparse
import json

# Constants
post_tweet_endpoint = 'https://api.twitter.com/1.1/statuses/update.json'
timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# Fetch environment variables
CONSUMER_KEY = os.environ["TWITTER_CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_SECRET"]
ACCESS_KEY = os.environ["TWITTER_ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# Create client
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

# Pretty prints a json response into individual tweets
def print_response(content):
  for tweet in content:
    print tweet['user']['name'] + '/' + tweet['user']['screen_name'] + tweet['text'] +'\n'

# Creates a HTTP request and posts to the post tweet endpoint
def post_tweet(tweet):
  response, content = client.request(post_tweet_endpoint,
                         method="POST",
                         headers={'Content-type': 'application/x-www-form-urlencoded'},
                         body=urllib.urlencode({'status': tweet}) )
  print response

# Returns the timeline for a user and pretty prints it to the console
def get_timeline():
  response, content = client.request(timeline_endpoint,
    method="GET",
    headers={'Content-type': 'application/json'})
  print_response(json.loads(content))

# Argument parsing logic
parser = argparse.ArgumentParser(description='Tweet from the command line')
parser.add_argument('--tweet', required=False)
parser.add_argument('--list', required=False, default='Yep')

args = parser.parse_args()

if args.tweet:
  post_tweet(args.tweet)
if args.list:
  get_timeline()
