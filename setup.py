import os
c = input("Choose your environment: [0] pip / [1] pip3 : ")

if c == "0":
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("pip install fade")
elif c == "1":
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("pip install fade")
print("Done.")
