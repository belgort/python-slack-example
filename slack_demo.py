# CTEC 121 / Intro to Programming and Problem Solving
# Lab - Using the Slack API
# by Bruce Elgort, 2016

# pip install slackclient to install SlackClient library
from slackclient import SlackClient
import json

def test_slack(sc):
    # use for debugging
    print("Testing API")
    print(80 * "=")
    print (sc.api_call("api.test"))

def get_channel_info(sc,channel):
    # get info about the channel
    print("Getting Channel Info")
    print(80 * "=")
    print (sc.api_call("channels.info", channel=channel))

def get_list_of_channels(sc):
    print("Getting List of Channels")
    print(80 * "=")
    # get list of channels
    channels = sc.api_call("channels.list")
    channels = json.dumps(channels)
    channels = json.loads(str(channels))
    return channels

def display_channels(channels):
    print("Display Channels")
    print(80 * "=")
    for i in channels['channels']:
        print("Channel:",i['name'])

def post_message(sc,text,channel,icon_url,username):
    print("Posting Message to Slack")
    print(80 * "=")
    # post a message into the #general channel
    print (sc.api_call("chat.postMessage",channel=channel,text=text,username=username,icon_url=icon_url,unfurl_links="true"))

def get_users(sc):
    print("Get Users")
    print(80 * "=")
    #call the users.list api call and get list of users
    users = (sc.api_call("users.list"))
    users = json.dumps(users)
    users = json.loads(str(users))
    return users

def display_users(sc,users):
    print("User List")
    print(80 * "=")
    # display active users
    for i in users['members']:
        # don't display slackbot
        if i['profile']['real_name'] != "slackbot":
            # don't display deleted users
            if not i['deleted']:
                # display real name
                print (i['profile']['real_name'])    
def main():
    # define variables
    token = "your token"
    channel = "a channel id"
    username = "Username to use display for message function"
    icon_url = "icon url for message function"
    # connect to Slack
    sc = SlackClient(token)
    # test slack
    test_slack(sc)
    # get channel info
    get_channel_info(sc,channel)
    # get list of channels
    channels = get_list_of_channels(sc)
    # display channels
    display_channels(channels)
    # post message
    post_message(sc,"Visit http://slack.com",channel,icon_url,username)
    # get users
    users = get_users(sc)
    # display users
    display_users(sc,users)
    
main()




