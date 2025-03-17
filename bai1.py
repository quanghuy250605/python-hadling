#doc n ki tu trong file 
with open("new.txt","r") as f:
    print(f.read(7))
#tao file moi
#with open("new.txt","x")as f:
#    f.write("this is  a new file")
#ghi them vao cuoi tep
with open("new.txt","a") as f:
    f.write("\nhello world")
#xoa noi dung cu ghi noi dung moi cua tep
with open("newfile.txt","w") as f:
    f.write("hello worlddddddddddd\n")
#doc toan bo file
with open("newfile.txt","a") as f:
    f.write("aaa\nbbb\nccc")
with open("newfile.txt","r") as f:
    print(f.read())
with open("newfile.txt","r") as f:
    line = f.readline()
    print(line)
#xoa file
import os
if os.path.exists("note2.txt"):
    os.remove("note2.txt")
else:
    print("file ko ton tai")
#xoa file
#os.remove("note.txt")
#kiem tra
if os.path.exists("note.txt"):
    print("file co ton tai")
else:
    print("file ko ton tai")





