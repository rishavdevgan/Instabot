import requests

APP_ACCESS_TOKEN = '3659496219.f4a9425.994f4f785e1542d4b933f2e19eb922d2'
BASE_URL = 'https://api.instagram.com/v1/'

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'REQUESTING URL FOR DATA: ' + request_url
    my_info = requests.get(request_url).json()
    print 'MY INFO IS: \n'
    print my_info

self_info()

print '\r\n'

insta_username = raw_input("What username do you want me to take requests for Sir ??\n")

print "What do you wish to do from the following tasks:\n" \
      "1. Get the user's Instagram ID\n" \
      "2. Get the user's recent posts\n" \
      "3. Like the posts"

make_a_choice = raw_input("Select from the above options\n")
print "You have selected %s option" %(make_a_choice)



def get_user_id_by_username(insta_username):

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, APP_ACCESS_TOKEN)
    print  'REQUESTING URL FOR DATA : ' + request_url

    search_results = requests.get(request_url).json()

    if search_results['meta']['code'] == 200:
        if len(search_results['data']):
            print search_results['data'][0]['id']
            return search_results['data'][0]['id']
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 was received!'

    return None



def get_users_recent_posts(insta_username):
    insta_user_id = get_user_id_by_username(insta_username)
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (insta_user_id, APP_ACCESS_TOKEN)

    print 'REQUESTING URL FOR DATA : ' + request_url

    recent_posts = requests.get(request_url).json()

    if recent_posts['meta']['code'] == 200:
        if len(recent_posts['data']):

                print recent_posts['data'][0]['id']
                return recent_posts['data'][0]['id']

        else:
            print 'No recent post by this user!'
    else:
        print 'Status code other than 200 was received!'



def like_post_for_user(insta_username):
    post_id = get_users_recent_posts(insta_username)
    payload = {'access_token': APP_ACCESS_TOKEN}
    request_url = (BASE_URL + 'media/%s/likes') % (post_id)

    response_to_like = requests.post(request_url, payload).json()

    print response_to_like

    if response_to_like['meta']['code'] == 200:
        print 'Liked Successfully'
    else:
        print 'Please try again!'



if make_a_choice == "1":
    print get_user_id_by_username(insta_username)

elif make_a_choice == "2":
    get_users_recent_posts(insta_username)

elif make_a_choice == "3":
    like_post_for_user(insta_username)

else:
    print "Select a suitable option.....................!!!!!!!!"




