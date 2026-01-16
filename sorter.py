import os, shutil 

path= r"C:/Users/shampie/Downloads/FileSorter/"

print(os.listdir(path))
print(os.path.exists(path+"csv files") )

folder_names = ["xlsx files","pdf files","png files","docx files"]

for loop in range(0,4) :
    if not os.path.exists(path+folder_names[loop]):
        print(path+folder_names[loop])
        os.makedirs(path+folder_names[loop])
        
        
file_name= os.listdir(path)

for file in file_name :
    if ".pdf" in file and not os.path.exists(path+"pdf files/"+file):
        shutil.move(path+file,path+"pdf files/"+file)
        
    elif ".png" in file and not os.path.exists(path+"png files/"+file):
        shutil.move(path+file,path+"png files/"+file)
        
    elif ".docx" in file and not os.path.exists(path+"docx files/"+file):
        shutil.move(path+file,path+"docx files/"+file)
        
    elif ".xlsx" in file and not os.path.exists(path+"xlsx files/"+file):
        shutil.move(path+file,path+"xlsx files/"+file)
        
