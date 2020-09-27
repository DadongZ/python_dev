import tweepy

auth = tweepy.OAuthHandler('bmlY8yjoGGw0TCt8wKAiqmVL6', 'GhPvwn7pAt7WWk8UvgnoRPc8Raa8IOnmimyVn1C4p7JhfojW0R')
auth.set_access_token('2293604888-jLqO0brGra39s4NKnlYTiYMk5pzUeLBj3eFmdSH', 'qvv8CreTjq6VftmP1wqkzr2nJWsR1w4cLgEHpJqF0BASO')

api = tweepy.API(auth)
user = api.me()

def showTwitterContent(top=10):
    """display the twiter on specified number of twitts

    Args:
        top (int, optional): [description]. Defaults to 10.
    """ 
    content=[(status.user.screen_name, status.text) for status in tweepy.Cursor(api.home_timeline).items(limit=top)]
    print(*content, sep="\n")

#showTwitterContent(10)

def limit_handler(cursor):
    """pause 1 second while reach the limit
    
    Args:
        cursor (tweepy object)
    """
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    
for followers in tweepy.Cursor(api.followers).items():
    fl=[]
    fl.append({followers.name, followers.screen_name})
    print(*fl, sep="\n")