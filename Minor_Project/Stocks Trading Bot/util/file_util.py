import json

def open_file(filename):
    """This function is to open the file and return json object """
    file=f"database\\{filename}"
    fhandle=open(file,encoding="UTF-8")
    data=json.load(fhandle)
    return data

def write(filename,data):
    """This function is to write to the file """
    file=f"database\\{filename}"
    with open(file,"w",encoding="UTF-8") as outfile:
        json.dump(data,outfile,indent=4)

def append(filename,entry):
    """This function is to make changes in the values """
    file=f"database\\{filename}"
    with open(file,"r+",encoding="UTF-8") as outfile:
        file_data=json.load(outfile)
        file_data["users"].append(entry)
        outfile.seek(0)
        json.dump(file_data,outfile,indent=4)
