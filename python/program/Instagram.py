import instaloader as ls

obj=ls.Instaloader()

user=input("Enter user name : ")

obj.download_profile(user, profile_pic_only=True)