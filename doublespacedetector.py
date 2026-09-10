#write a program to detect double space in a string

print("Write something below")
hekko=input("")

detector=hekko.find("  ")


if detector==-1:
 print("No double Space found. The string is correctly written")

else:
 print("System finds that there is a double space at index",detector,"pls correct it")
