"""Bot to post content to social media platforms"""

from time import sleep
import os
import sys
sys.path.append('/Users/Armin/Desktop/social-media-marketing-bot/src/Drivers')
sys.path.append('/Users/Armin/Desktop/social-media-marketing-bot/src/Images')
sys.path.append('/Users/Armin/Desktop/social-media-marketing-bot/src/Secrets')
from gsheets import GSheet
from handle_images import HandleImage
from my_secrets import max_character_limit

# Social media platforms to target
social_media_accounts = ['facebook']

#Launch the bot
if __name__=='__main__':
    print(f'Launchin Social Media Marketing Bot')
    print(f'Version: "Post Bot"')
    gsheet = GSheet()
    gsheet.buildService()
    sleep(2)

    #Handle each social media account
    for social_media_account in social_media_accounts:
        os.system('clear')
        gsheet.getPostContent(social_media_account=social_media_account)
        # Handle the image
        post_image = HandleImage()
        post_image.getImageFromSource(image_link=gsheet.post_details['post_image_link'])
        post_image.resizeImage(social_media_account=social_media_account)
