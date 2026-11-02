import pyshorteners
apt
#ask for link
long_link=input("Paste the link you want to shorten: ")

#shorten the link
def main(link):
    s=pyshorteners.Shortener()
    short_link=s.tinyurl.short(long_link)
    return print("Your shortened link is: ", short_link)


if __name__=="__main__":
    main()