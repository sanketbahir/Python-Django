# #file handling: very important for we applaction
# #open() function --> open(filename,mode)
# #create_file.read_tile

# #r : open existing file for read read opration
# #read(): read the content of the filne 

# read_file = open('inner5.py','r')
# print(read_file.read())


# read_file = open('inner5.py','r')
# print(read_file.read())


# i = open('inner5.py','r')
# print(i.readline())
# print(i.readline())
# print(i.readline())
 
# for x in i:
#     print(x)


#x - creating the file
#w - opens a file  for writing , creating file if the file exists


i = open('file.txt','a')
i.write('\n pyrhon django')
i.close()
read_file = open('file.txt','r')
print(read_file.read())