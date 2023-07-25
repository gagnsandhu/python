# import requests

# result=requests.get("https://pythonhow.com/media/data/universe.txt")
# # print(result.text)
# print(result.text.count('a'))

# import screeninfo
# print(type(screeninfo.get_monitors()))
# l=(screeninfo.get_monitors())
# print(l[0].width)

# import pyglet

# pyglet.options['debug_gl'] = True
# print(pyglet.app("hello world"))


# with open("countries_missing.txt",'r') as file:
#     content=file.readlines()

# content=[i.rstrip('\n') for i in content]
# content.append("Portugal")
# content.append("Germany")
# content.append("Spain")
# content.sort()

# with open("countries_missing.txt",'w') as file:

#     for i in content:
#         file.write(i+"\n")  



# import pandas as pd

# data=pd.read_csv("countries_by_area.txt")

# # print(type(data["country"]))
# data["density"]=data["population_2013"]/data["area_sqkm"]
# data=data.sort_values(by="density",ascending=False)

# print(data)


# import sqlite3
# conn=sqlite3.connect("database.db")
# cur=conn.cursor()
# cur.execute("SELECT * FROM countries")
# rows=cur.fetchall()
# conn.close()

# for i in rows:
#     print(i)

# import os

# curr=os.system('echo %CD%')
# print(os.system('dir '+str(curr)))


# with open("urls.txt",'r') as file:
#     content=file.readlines()

# with open("data.txt","w") as file:
#     for line in content:
#         line1=line.replace('s','')
#         # print(line)
#         line2=line1[:5]+"/"+line1[5:]
#         # print(line)

#         file.write(line2+"\n")

# with open("urls.txt",'r') as file:
#     conte=file.readlines()

# print(conte)

# value=input("Enter values: ")
# l=value.split(',')
# with open("values.txt",'w') as file:
#     for i in l:
#         file.write(i+"\n")


# import pyglet

# window = pyglet.window.Window()

# label = pyglet.text.Label('Hello, world',
#                           font_name='Times New Roman',
#                           font_size=36,
#                           x=window.width//2, y=window.height//2,
#                           anchor_x='center', anchor_y='center')
# @window.event
# def on_draw():
#     window.clear()
#     label.draw()

# pyglet.app.run()
import pytest

print(dir(pytest))
