from PIL import Image
import csv
import requests
import os
import PyPDF2
import re

def image():
    mask=Image.open('mask.png')
    print(mask.size)

    word_matrix=Image.open('word_matrix.png')
    print(word_matrix.size)

    mask.putalpha(200)

    mask=mask.resize((1015,559))
    # print(mask.show())
    # print(mask.size)
    # mask.paste(im=word_matrix,box=(0,0))
    word_matrix.paste(mask,(0,0),mask)

    print(word_matrix.show())


def csvpdf():
    data=open('find_the_link.csv',encoding='utf-8')
    csv_data=csv.reader(data)
    data_line=list(csv_data)
    i=0
    link=''
    for line in data_line:
        link=link+line[i]
        i+=1
    print(link)
    # result=requests.get(link)
    # # print(result.text)
    # url='curl'+' '+link
    # re=os.system(url)
    # print(re)
    fhandle=open('Find_the_Phone_Number.pdf','rb')
    pdf_reader=PyPDF2.PdfReader(fhandle)
    total_pages=(len(pdf_reader.pages))
    for page in range(0,total_pages):
        page_one=pdf_reader.pages[page]
        page_text=page_one.extract_text()
        # print(page_text)
        found=re.search(r'\d{3}\s\d{3}',page_text)
        if found == None:
            continue
        print(found.group())


csvpdf()