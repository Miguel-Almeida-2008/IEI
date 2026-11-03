from pyshorteners import pyshorteners
#ask for link
link=input("Paste the link you want to shorten: ")

#ask if user wants to shorten the link or make it longer instead
choice=int(input("Type 0 if you want to shorten your link\n" "Type 1 if you want to lengthen it instead\n""--->"))

#create function
def main(choice, link):
    s=pyshorteners.Shortener()
    if choice==0:
        short_link=s.tinyurl.short(link)
        return print("Your shortened link is: ", link)
    elif choice==1:
        long_link=s.tinyurl.expand(link)
        return print("Your lengthened link is: ", link)
    else:
        return print("Your choice is invalid. Please try again and type either 0 or 1.")


if __name__=="__main__":
    main()