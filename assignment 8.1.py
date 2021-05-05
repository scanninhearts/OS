import os
def main ():
    directory = input("Enter the directory that you want to save the file:")
    file_name = input("Enter the filename:")
    name = input("Enter your name:")
    address = input("Enter your address:")
    phone_number = input("Enter your phone number:")
    #Looking for the directory
    if os.path.isdir(directory):
        #Opening the file
        writeFile = open(os.path.join(directory, file_name),'W')
        #Writing the data
        writeFile.write (name+','+address+','+phone_number+'\n')
        #Closing the file
        writeFile.close()
        print ("File contents:")
        #Reading the file
        readFile = open(os.path.join(directory, file_name), "r")
        for line in readFile:
            print (line)
        readFile.close ()
    else:
        print ("This directory does not exists.")
main ()