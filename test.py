#!C:/Python/Python38/python
print("Content-Type: text/html")
print()

import cgi
import sys
sys.path.insert(0, 'C:\Python\Python38\Lib')
import operator
import networkx as nx
import matplotlib.pyplot as plt
import random


global user_list,users,users_choice
user_list=[]
users=[]
users_choice=[]
print("<html>\n")
print("<body>\n")
def convert(st):
    li=[]
    for i in st:
        if(i!='[' and i!=']' and i!=','):
            li.append(int(i))
    return li

def create_list():
    global user_list,users,users_choice
    file=open("userlist.txt","r")
    file_lines=file.readlines()
    for data in file_lines:
        data=data.split()
        
        user_list.append(data[0])
        users.append(data[1])
        users_choice.append(convert(data[2]))
    print(user_list,"\n <br />",users,"\n <br />",users_choice,"\n <br />")
    file.close()
def addnewnode(n):
    global user_list,users
    i=len(user_list)
    i+=1
    user_list.append(i)
    users.append(n)
    return i
def addchoices(nd,li):
    global users_choice
    users_choice.append(li)
def friends(graph,user):
    return set(graph.neighbors(user))
def common_friends(graph,user1,user2):
    user1friends = friends(graph,user1)
    user2friends = friends(graph,user2)
    commonfriends = user1friends.intersection(user2friends)
    return commonfriends

def common_likes(graph,user1,user2):
    global users_choice
    global user_list
    common_like_list=[]
    count=0
    user1=user_list.index(user1)
    user2=user_list.index(user2)
    user1L=users_choice[user1]
    user2L=users_choice[user2]
    for i in user1L:
        if(i in user2L):
            count+=1
            common_like_list.append(i)
    if(len(common_like_list)==0):
        return 0,None
    return count,common_like_list
def number_of_common_friends_map(graph,user):
    all_names = set(graph.nodes())
    all_names.remove(user)
    users_friends = friends(graph,user)
    friend_map = {}
    for names in all_names:
        temp_friends = common_friends(graph,user,names)
        num_friends = len(temp_friends)
        if num_friends>0 and names not in users_friends:
            friend_map[names] = num_friends
    return friend_map
def number_map_sorted_list(friendmap,friendlikes):
    temp_list=sorted(friendmap.items(),key=operator.itemgetter(1),reverse=True)
    friend_list = [items[0] for items in temp_list]
    return friend_list,friendlikes
def recommend_by_number_of_common_friends(graph,user):
    friendmap = number_of_common_friends_map(graph,user)
    friend_recommend = number_map_sorted_list(friendmap)
    return friend_recommend
def influence_map(graph,user):
    result=0
    friends_influence = dict()
    friends_likes=dict()
    count=0
    friendmap = number_of_common_friends_map(graph, user)
    for k in friendmap.keys():
        x= common_friends(graph,k,user)
        cnt,z=common_likes(graph,k,user)
        
        if(cnt>count):
            count=cnt
            friends_likes[k]=z;
            result+=1
        for cf in x:
            no_of_friends=len(friends(graph,cf))
            
            result = result + (float(1)/no_of_friends)   
        friends_influence[k] = result
        result = 0
    return friends_influence,friends_likes

def recommend_by_influence(graph, user):
    friendmap,friendlikes= influence_map(graph, user)
    return number_map_sorted_list(friendmap,friendlikes)
def top_5_influence(graph):    
    ##for m in graph:
        m='2'
        n = int(m)
##        if n>1 and n%2 == 0:
        reco,likes = recommend_by_influence (graph, m)[:3]
        reco=reco[:5]
        for l in likes.keys():
            if l not in reco:
                likes.pop(l)
        print (n, reco[:5],likes)
        return reco[:5],likes
    
create_list()
newid=addnewnode("Sonal")
##print(users)
form=cgi.FieldStorage()
a=form.getvalue("a")
b=form.getvalue("b")
c=form.getvalue("c")
d=form.getvalue("d")
e=form.getvalue("e")
f=form.getvalue("f")
g=form.getvalue("g")
h=form.getvalue("h")
i=form.getvalue("i")

li=[a,b,c,d,e,f,g,h,i]
Not_none_values = filter(None.__ne__, li)
li = list(Not_none_values)
lis=[]
for x in li:
    lis.append(int(x))
print(lis)

addchoices(newid,li)


print(lis[0])

print("<\body>\n")
print("<\html>")

