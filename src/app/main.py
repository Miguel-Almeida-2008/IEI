import pyshorteners
import os

#create function
def main():
   
   
    s=pyshorteners.Shortener()
    while True:
        #ask if user wants to shorten the link or make it longer instead
        choice=input("Type 0 if you want to shorten your link\nType 1 if you want to lengthen it instead\n---> ")
            

        if choice=="0":
            #ask for link
            link=input("Paste the link you want to shorten: ")
            short_link=s.tinyurl.short(link)
            print("Your shortened link is: ", short_link)
            break
        elif choice=="1":
            #ask for link
            link=input("Paste the link you want to lengthen: ")
            long_link=s.tinyurl.expand(link)
            print("Your lengthened link is: ", long_link)
            break
        else:
            print("Your choice is invalid. Please try again and type either 0 or 1.")


if __name__=="__main__":
    main()