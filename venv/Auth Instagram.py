
import requests

BASE_URL ='https://api.instagram.com/v1/'
APP_ACCESS_TOKEN ='6015895265.bf2309d.04ea1ac0cb2d44a18f63a5e198a6a200'


def get_own_post():
   # request_url =(BASE_URL + 'users/self/media/recent/?access_token=6015895265.bf2309d.04ea1ac0cb2d44a18f63a5e198a6a200')
   # print('Requesting data from %s') %(request_url)
   request_url ='https://api.instagram.com/v1/tags/paris?access_token=6015895265.bf2309d.04ea1ac0cb2d44a18f63a5e198a6a200'
   recent_post = requests.get(request_url)#.json()
   print (recent_post)

get_own_post()
