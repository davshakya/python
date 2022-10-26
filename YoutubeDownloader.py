import pytube
print("******** Welcome to e-lalita Youtube Downloader ********")
def youtube_downloder():
        link = input("Enter any youtube link : ")
        res=input("Choose any one resolution from 144p, 360p, 720p & 1080p: ")
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
        print("Something is wrong with input data, please try with another resolution or URL")
    finally:
        print("Thanks for choosing this application")  
    Exit_Key=input("\nPress x for exit or Press Enter for conitnue..: ")
    if Exit_Key=="x":
        break
    else:
        youtube_downloder


