from pytube import YouTube 
link=input("Enter your link : ")
yt=YouTube(link)


print("\nTitle : {} \n".format(yt.title))
print("Number of Vies : {} \n".format(yt.views))
print("length : {} Seconds \n".format(yt.length))
print("Description : {} \n ".format(yt.description))
print("Rating : {} \n".format(yt.rating))
#print("Streams : {} \n".format(yt.streams))
stream=yt.streams
for i in stream:
    print(i)


print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))

#download vidoe
ys=yt.streams.get_by_itag('22')
ys.download()

#download song
song=yt.streams.get_audio_only()
song.download()
print("done...")