import json


with open("followers_and_following/followers_1.json", 'r') as followers_file:
    followers_data = json.load(followers_file)

with open("followers_and_following/following.json", 'r') as following_file:
    following_data = json.load(following_file)

following = [i['string_list_data'][0]['value'] for i in following_data['relationships_following']]
followers = [i['string_list_data'][0]['value'] for i in followers_data]


not_in_followers =[]
for i in following:
    if i in followers:
        pass
    else:
        not_in_followers.append(i)

print(not_in_followers)
