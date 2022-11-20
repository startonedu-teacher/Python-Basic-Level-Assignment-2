from read import *

file = open("the boy who lived.txt", "r")

count = read_book(file)

file.close()

print("The book contains {} potters in it.".format(count))