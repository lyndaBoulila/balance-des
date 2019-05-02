import tweepy


def auth():
    """
    se connecte à l'api twitter
    """
    # Clés de votre application
    # Clés de votre application
    consumer_key = "IiYtUT1y2TYJoL9jRq8bCyTVg"
    consumer_secret = "7Q6WChQa9qUytPnJ2W7gRImn1b6TSL7efu4E2gD4cC5vwghEGk"

    # le access_token est le token de l'application twitter que nous avons créée précédement
    access_token = "1101572978863734785-oCb7l65x5GF0biwgaDB3LyRCcM89A7"
    access_token_secret = "S8XBMeLJrzyRJ9lQZbTtLT4J31FAzUaFUnSi5sF0f9JfS"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api, auth

