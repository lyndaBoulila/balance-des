#https://github.com/srphcr/python-instagram-ext



from instagram.client import InstagramAPI
access_token = "6015895265.2395b5e.2e9ee8e774ca4d8a9943d568c2a8a4a3"
client_secret = "292206cc19544089b92a93696bc0339b"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)

#api = InstagramAPI(client_id='2395b5e3d1f544fd8ccb99d8c61912bf', client_secret=client_secret)
api.tag('#paris')

# Subscribe to updates for all users authenticated to your app
#api.create_subscription(object='user', aspect='media', callback_url='http://mydomain.com/hook/instagram')

# Subscribe to all media tagged with 'fox'
#api.create_subscription(object='tag', object_id='fox', aspect='media', callback_url='http://mydomain.com/hook/instagram')

# Subscribe to all media in a given location
#api.create_subscription(object='location', object_id='1257285', aspect='media', callback_url='http://mydomain.com/hook/instagram')

# Subscribe to all media in a geographic area
#api.create_subscription(object='geography', lat=35.657872, lng=139.70232, radius=1000, aspect='media', callback_url='http://mydomain.com/hook/instagram')