##########################
###pip install instabot###
##########################
from instabot import Bot
bot=Bot()
bot.login(username=input("Enter your username, Email or Phone Number : "), password=input("Enter your password : "))
bot.upload_photo(input("Enter the link of photo you want to upload : "),caption=input("Enter caotion : "))
bot.logout
#################################################################
#### Coded by Shivam kumar (https://www.github.com/Shiva-slbs)###
#################################################################