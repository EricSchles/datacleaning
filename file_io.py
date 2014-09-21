thing = open("thing.txt","w") #writing to a file - will erase contents from the file if it exists!!! use with caution!!!
thing_two = open("thing.txt","r") #reading from a file
thing_three = open("thing.txt","wb") #writing to a file as binary - used for writing to pdfs and things like this
thing_four = open("thing.txt","rb") #reading from a binary file
thing_five = open("thing.txt","a+") #adds to a file

thing.close()
thing_two.close()
thing_three.close()
thing_four.close()
thing_five.close()

with open("thing.txt","w") as f:
    f.write("hello world")
    print f

print f
