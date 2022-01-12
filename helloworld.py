import tweepy, time, sys, random

argfile = str(sys.argv[1])

CONSUMER_KEY= 'UHAqu3DdWAy0K7lELWP4Yo94e'
CONSUMER_SECRET= 'qJporIhW4egHkgdpi1MrjJavXNdJtv6MOMcWdCmbMr1gYy9yv0'
ACCESS_KEY= '1480468985762041861-mp3NU8KChhWgEh4PtTfkxGwGag4YnA'
ACCESS_SECRET= '0P46ldcQxeSH6ZA2ZJp55mkDC9U5cWK02JMapnyFRLJVT'
BEAR_KEY= 'AAAAAAAAAAAAAAAAAAAAAHDRXwEAAAAAD1%2FVM8cRjEyjcckrpD3FZMilcjQ%3Dw8OxqjsXs5zglrQfRktfRzyyCjN07QTTHq7HJYXNnCmxRnw5Rx'

client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET,
                       bearer_token = BEAR_KEY)

filename=open(argfile,'r')
f=filename.readlines()
random.shuffle(f)
filename.close()

for line in f:
    client.create_tweet(text=line.rstrip())
    time.sleep(20)
    print("Success at posting tweet")