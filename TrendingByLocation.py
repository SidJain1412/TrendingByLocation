def trending():
    #importing tweepy to connect to twitter
    import tweepy
    from tweepy import OAuthHandler
    #from twitter app id
    consumer_key=""
    consumer_secret=""
    access_token=""
    access_secret=""
    #initializing contact point (api variable)
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api=tweepy.API(auth)
    WOEID=2295424
    #Replace with WOEID for whichever city you want
    trends=api.trends_place(WOEID)
    a=trends[0]
    for item in a["trends"]:
        print(item["name"])