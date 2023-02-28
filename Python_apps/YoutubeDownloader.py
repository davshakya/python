import pytube
def youtube_downloder():
    print("******** Welcome to 'e-lalita Youtube Downloader' ********")
    link = input("Enter url of your youtube video link : ")
    res = input("Choose any one resolution from 360p, 480p, 720p & 1080p: ")
    ytube = pytube.YouTube(link)
    print("Title:", ytube.title)
    print("Author:", ytube.author)
    print("Published date:", ytube.publish_date.strftime("%Y-%m-%d"))
    print("Number of views:", ytube.views)
    print("Length of video:", ytube.length, "seconds")
    ytube.streams.get_by_resolution(res).download()
    print("Video successfullly downloaded from", link)

while True:
    try:
        youtube_downloder()
    except:
        print("Something is wrong with YOURinput data, please try again")
    finally:
        print("Thanks for choosing this application.")
    Exit_Key = input("\nPress x for exit or Press Enter for conitnue..: ")
    if Exit_Key == "x":
        break
    else:
        youtube_downloder
