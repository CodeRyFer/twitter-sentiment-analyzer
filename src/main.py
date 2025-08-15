import tweepy
from textblob import TextBlob

consumer_key = 'rczZDXlAKoWfepiJIjAiB6sLx'
consumer_secret = '4GdjNhUYyBdyIipIgkFJxcFMK1GC05cebYO17nHQnkViUKEFcJ'

access_token = '1535726073987616768-m8O6o9ffOXnQM6y5Oem9z4j8nFM7a2'
access_secret = 'f5PL9W6dR3Mjyo3fHkybNTTq9GsSvMsBPiXhUno7bLfTk'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)