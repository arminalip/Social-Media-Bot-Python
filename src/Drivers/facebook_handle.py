"""Module to interact with Facebook."""

import facebook
import json
import os
import pyautogui
import requests
import sys
sys.path.append('/Users/Armin/Desktop/social-media-marketing-bot/src/Secrets')
sys.path.append('/Users/Armin/Desktop/social-media-marketing-bot/src/Images')
sys.path.append('/Users/Armin/Desktop/social-media-marketing-bot/src/PyAutoGUI')


from my_secrets import FACEBOOK_PERMANENT_TOKEN
from my_secrets import FACEBOOK_PASSWORD
from my_secrets import FACEBOOK_USERNAME
from my_secrets import FACEBOOK_LOGIN_URL
from my_secrets import FACEBOOK_BUSINESS_PAGE
from my_secrets import FACEBOOK_POST_BASE_URL

class FacebookBot:
    """Class to handle the Facebook API"""
    def __init__(self):
        """Initialize"""
        os.system('clear')
        print('Initializing the Facebook bot')
    
    def postContent(self, content_image, content_message, content_location, content_hashtags):
        '''Adds a post to Facebook.'''
        fb = facebook.GraphAPI(FACEBOOK_PERMANENT_TOKEN)
        fb_tags = []
        for hashtag in content_hashtags.split(', '):
            hashtag = '#' + hashtag
            fb_tags.append(hashtag)
        fb_tags_str = ' '.join(fb_tags)
        fb_message = f'{content_message}\n\n{fb_tags_str}'
        self.post_location = content_location
        # Post to Facebook
        fb_response = fb.put_photo(open(content_image, 'rb'), caption=fb_message) 
        self.fb_post_id = fb_response['id']
        print(f'Post added to Facebook, ID: {self.fb_post_id}')
