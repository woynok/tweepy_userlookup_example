import yaml
import tweepy
with open('secret/secrets.yaml', 'r') as f:
    bearer_token = yaml.safe_load(f)['twitterAPI']['Bearer_Token']
    
client = tweepy.Client(bearer_token)
