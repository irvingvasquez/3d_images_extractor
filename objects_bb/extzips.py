import os, zipfile, pandas as pd


def extract_zip(dir_name, extension):
    dir = []
    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(dir_name + item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            os.mkdir(file_name[:-4])
            zip_ref.extractall( file_name[:-4]) # extract file to dir
            zip_ref.close() # close file
            dir.append(file_name[:-4])
            os.remove(file_name) # del file
    
    x = pd.DataFrame(data=dir, index=None, columns=None, dtype=None)
    x.to_excel('direcciones.xlsx', index=False)