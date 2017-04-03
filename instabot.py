import requests

APP_ACCESS_TOKEN = '3659496219.f4a9425.994f4f785e1542d4b933f2e19eb922d2'
BASE_URL = 'https://api.instagram.com/v1/'

def self_info():
    #request_url = BASE_URL + '/users/self/?access_token=' + APP_ACCESS_TOKEN
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'REQUESTING URL FOR DATA: ' + request_url
    my_info = requests.get(request_url).json()
    print 'MY INFO IS: \n'
    print my_info['data']['bio']
    print my_info['data']['website']
    print my_info['data']['full_name']

self_info()

print '\r\n'

def get_user_by_username(insta_usernname):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_usernname, APP_ACCESS_TOKEN)
    print  'REQUESTING URL FOR DATA : ' + request_url

    search_results = requests.get(request_url).json()

    print search_results

get_user_by_username('devgan.shweta')