# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:45:49 2018

@author: vineet
"""




import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
##fb_file_path= "facebooklinks.txt"
fb_file_path= "links.txt"
global user_list,users,users_choice
user_list=[]
users=[]
users_choice=[]
##user_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
##users=['Alia','Candy','Vicky','Meera','Veronica','Kabir','Tanmay','Nikhil','Jenny','Vivian','Edward','Harsh','Mark','Donald','Sunny','Henry','Sumit','Rajesh','Nia','Gopi']
##users_choice=[[6,2,4],
##              [1,3,7],
##              [9,4,2],
##              [5,4,1],
##              [5,1,7],
##              [4,6,8],
##              [1,2,7],
##              [9,8,1],
##              [3,7,6],
##              [1,3,7],
##              [9,4,2],
##              [6,2,4],
##              [1,3,7],
##              [9,4,2],
##              [6,2,4],
##              [1,3,7],
##              [9,4,2],
##              [6,2,4],
##              [1,3,7],
##              [9,4,2]              
##    ]
print(len(users_choice))
### Problem 1b
###


#nx.draw(p_graph)
#plt.show()

def create_romeojuliet_graph():
    rj_graph=nx.Graph()

    rj_graph.add_node("Tybalt")
    rj_graph.add_node("Nurse")
    rj_graph.add_node("Juliet")
    rj_graph.add_node("Friar Laurence")
    rj_graph.add_node("Capulet")
    rj_graph.add_node("Benvolio")
    rj_graph.add_node("Romeo")
    rj_graph.add_node("Mercutio")
    rj_graph.add_node("Montague")
    rj_graph.add_node("Paris")
    rj_graph.add_node("Escalus")
    
    rj_graph.add_edge("Juliet","Tybalt")
    rj_graph.add_edge("Nurse","Juliet")
    rj_graph.add_edge("Juliet","Capulet")
    rj_graph.add_edge("Juliet","Romeo")
    rj_graph.add_edge("Juliet","Friar Laurence")
    rj_graph.add_edge("Tybalt", "Capulet")
    rj_graph.add_edge("Romeo","Benvolio")
    rj_graph.add_edge("Romeo","Friar Laurence")
    rj_graph.add_edge("Romeo","Mercutio")
    rj_graph.add_edge("Romeo","Montague")
    rj_graph.add_edge("Benvolio","Montague")
    rj_graph.add_edge("Mercutio", "Escalus")
    rj_graph.add_edge("Montague", "Escalus")
    rj_graph.add_edge("Paris", "Mercutio")
    rj_graph.add_edge("Escalus", "Paris")
    rj_graph.add_edge("Capulet", "Paris")
    rj_graph.add_edge("Capulet","Escalus")
    
    return rj_graph

def friends(graph,user):
    return set(graph.neighbors(user))

#m= friends(p_graph,'A')
#print(m)

def friends_of_friends(graph,user):
    userfriends = friends(graph,user)
    finalfriends = set()
    for names in userfriends:
        
        friends_of_userfriends = friends(graph,names)
        for names2 in friends_of_userfriends:
            if(names2 not in userfriends and names2 != user):
                finalfriends.add(names2)
    return finalfriends

#n = friends_of_friends(p_graph,'A')
#print(n)
  
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
            
#o = common_friends(p_graph,'A','E')
#print(o)
    

#p = set(p_graph.nodes())
#type(p)

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

#q = number_of_common_friends_map(p_graph,'A')
#print(q)
    
import operator
def number_map_sorted_list(friendmap,friendlikes):
    temp_list=sorted(friendmap.items(),key=operator.itemgetter(1),reverse=True)
    friend_list = [items[0] for items in temp_list]
    return friend_list,friendlikes

#r = number_map_sorted_list(q)
#print(r)

def recommend_by_number_of_common_friends(graph,user):
    friendmap = number_of_common_friends_map(graph,user)
    friend_recommend = number_map_sorted_list(friendmap)
    return friend_recommend
    
def draw_facebook_graph(graph):
    nx.draw(graph)
    plt.savefig("fb.pdf")
    plt.show()
def create_facebook_graph(file_path):
    fb_file=open(file_path, "r")
    fb_data_list=fb_file.readlines()
    fb_graph = nx.Graph()
    
    for data in fb_data_list:
        friend_list=data.split()
        friend_one = friend_list[0]
        friend_two = friend_list[1]
        fb_graph.add_node(friend_one)
        fb_graph.add_node(friend_two)
        fb_graph.add_edge(friend_one,friend_two)
    
    print (nx.info(fb_graph))
    ##draw_facebook_graph(fb_graph)
    return fb_graph;


#s = recommend_by_number_of_common_friends(p_graph,'A')
#print(s)
#t = recommend_by_number_of_common_friends(p_graph,'D')
#print(t)
#u = recommend_by_number_of_common_friends(p_graph,'F')
#print(u)

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

def evaluate_recommender(graph):
    result = ["Number of friends in common", "Influence"]
    tot_rank_common=float(0)
    tot_rank_influence=float(0)
    num_inf_trials = float(0)
    num_common_trials = float(0)
    
    for i in range(100):
        friend_1=random.choice(list(graph.node.keys()))
        friend_2=random.choice(list(friends(graph, friend_1)))
        graph.remove_edge(friend_1, friend_2)
        rank_inf, num_inf = influence_rank_calc(graph, friend_1, friend_2)
        tot_rank_influence += rank_inf
        num_inf_trials += num_inf
        rank_common, num_common = common_rank_calc(graph, friend_1, friend_2)
        tot_rank_common += rank_common
        num_common_trials += num_common
        graph.add_edge(friend_1, friend_2)
        
    final_rank_common=tot_rank_common / num_common_trials
    final_rank_influence=tot_rank_influence / num_inf_trials
    
    print("Average rank of influence method: {} \nAverage rank of number of friends in common method: {}".format(final_rank_influence, final_rank_common))
    print("{} method is better".format(result[0] if final_rank_common < final_rank_influence else result[1]))

def influence_rank_calc(graph, friend_1, friend_2):
    f2_friends=recommend_by_influence(graph, friend_2)
    f1_friends=recommend_by_influence(graph, friend_1)
    return average_rank_calc(friend_1, friend_2, f1_friends, f2_friends)

def common_rank_calc(graph, friend_1, friend_2):
    f2_friends=recommend_by_number_of_common_friends(graph, friend_2)
    f1_friends=recommend_by_number_of_common_friends(graph, friend_1)
    return average_rank_calc(friend_1, friend_2, f1_friends, f2_friends)
    
def average_rank_calc(friend_1, friend_2, f1_friends, f2_friends):
    num_trials = float(0)
    average = float(0)
    
    f1_rank = get_friend_rank(f2_friends, friend_1)
    f2_rank = get_friend_rank(f1_friends, friend_2)
   
    if f1_rank > 0.0 and f2_rank > 0.0:      
        average= (f1_rank+f2_rank)/2.0
        num_trials = num_trials+1.0
    return average, num_trials

def get_friend_rank(friends,friend):
    rank = float(0)
    if friend not in friends:
        return rank
    for f in friends:
        rank += 1
        if f==friend:
            break
    return rank

#s = recommend_by_influence(p_graph,'A')
#print(s)

def diff_algo(graph):
    each_name = set(graph.nodes())
    
    unchanged = list()
    changed = list()
    for names in each_name:
        recommend_list = recommend_by_influence(graph,names)
        common_list = recommend_by_number_of_common_friends(graph,names)
        if recommend_list == common_list:
            unchanged.append(names)
        else:
            changed.append(names)
    print("unchanged = ",unchanged)
    print("changed = ",changed)



    
def top_10_common_fb(graph):    
    for m in graph:
        n = int(m)
        if n>1 and n%2 == 0:
            all_rec = recommend_by_number_of_common_friends(graph,m)
            print(all_rec)
            top_10_common_rec = all_rec[0:5]
            print("rec for {0} is {1}".format(n,top_10_common_rec))
            
            
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

def addnewnode(n):
    global user_list,users
    id=len(user_list)
    id+=1
    user_list.append(id)
    users.append(n)
    return id

def create_list():
    global user_list,users,users_choice
    file=open("userlist.txt","r")
    file_lines=file.readlines()
    for data in file_lines:
        data=data.split()
        user_list.append(data[0])
        users.append(data[1])
    print(user_list,users)
    
##def main():
##    # if (len(argv) == 2):
##    #     fb_file_path = sys.argv[1]
##    # else:
##    #     sys.exit("Facebook data file path is required...")
##
##     
##    
####    
####    print("\n********** ROMEO JULIET GRAPH **********\n")
####    rj_graph = create_romeojuliet_graph()
####    print(rj_graph)
####    
####    print("\n********** Comparing the two algorithms on romeo-juliet graph **********\n")
####    diff_algo(rj_graph)
####    print("\n********** Compute the average ranks for the two algorithms on romeo-juliet graph **********\n")
####    #evaluation for romeo juliet data
####    evaluate_recommender(rj_graph)
##    
##    print("\n********** FACEBOOK Graph **************\n")
##    fb_graph = create_facebook_graph(fb_file_path)
##    
##    
##    print("\n********** Recommendation using common friends for some users in FACEBOOK Graph **************\n")
##    
##    ##top_10_common_fb(fb_graph)
##    
##    
##    print("\n********** Recommendation using influence algorithm for some users in FACEBOOK Graph **************\n")
##    
##    top_5_influence(fb_graph)
##    
##    
##    print("\n********** Compute the average rank for the two algorithms on FACEBOOK Graph **********\n")
##    #evaluation for facebook data
##    ##evaluate_recommender(fb_graph)
##    
##    
##    
##    
##    
    
    #this method call wil take long time to execute.
    #draw_facebook_graph(fb_graph)
    
##if __name__ == "__main__":
##    main()
