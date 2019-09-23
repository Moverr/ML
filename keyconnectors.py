users = [
    {"id":0},
    {"id":1},
    {"id":2},
    {"id":3},
    {"id":4},
    {"id":5},
    {"id":6},
    {"id":7},
    {"id":8},
    {"id":9}
    
]

friendship_pairs = [
    (0,1),
    (0,2),
    (1,2),
    (1,3),
    (2,3),
    (3,4),
    (4,5),
    (5,6),
    (5,7),
    (6,8),
    (7,8),
    (8,9)
]

friendships = {user["id"]:[] for user in users}

print(friendships)
for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

#print(friendship_pairs)
#print(friendships)

def number_of_friends(user):
    """ how manu friends does _user_ nave ? """
    user_id = user["id"]
    firend_ids = friendships[user_id]
    return len(firend_ids)

total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)

num_users = len(users)
print(num_users)

num_friends_by_id = [(user["id"],number_of_friends(user)) for user in users ]

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],reverse=True
)

print(num_friends_by_id)

# Suggest Friends of a Friend  Connection
def foaf_ids_bad(user):
    return[foaf_id 
                for friend_id in friendships[user["id"]]
                for foaf_id in friendships[friend_id]]


print(users[0])
foaf = foaf_ids_bad(users[0])
# print(foaf)

foaf = foaf_ids_bad(users[1])
# print(foaf)

foaf = foaf_ids_bad(users[2])
# print(foaf)


interests = [
    (0,"Hadoop"),
    (0,"Big Data"),
    (0,"HBase"),
    (0,"Java"),
    (0,"Spark"),
    (0,"Storm"),
    (0,"Cassandra"),
    (1,"NoSQL"),
    (1,"MogoDB"),
    (1,"Cassandra"),
    (1,"HBase"),
    (1,"Postgres"),
    (2,"Python"),
    (2,"scikit-learn"),
    (2,"scipy"),
    (2,"numpy"),
    (2,"statsmodels"),
    (2,"pandas"),
    
    (3,"R"),
    (3,"Python"),
    (3,"statistics"),
    (3,"probability"),
   
    (4,"machine learning"),
    (4,"regression"),
    (4,"decision trees"),
    (4,"libsvm"),
   
    (5,"Python"),
    (5,"R"),
    (5,"Java"),
    (5,"C++"),
    (5,"Haskell"),
    (5,"programming languages"),

    (6,"probability"),
    (6,"mathematics"),
    (6,"theory"),

    (7,"machine learning"),
    (7,"scikit-learn"),
    (7,"Mahout"),
    (7,"neural networks"),

    (8,"neural networks"),
    (8,"deep learning"),
    (8,"Big Data"),
    (8,"artificial intelligence"),

    (9,"Hadoop"),
    (9,"Java"),
    (9,"MapReduce"),
    (9,"Big Data")    
     
]
 
#print(users)
print("Data scientiss who like :")
def data_scientists_who_like(target_interest):
    return [user_id for user_id, user_interest in interests
            if user_interest == target_interest]

# creating a loop and returning it 

# print(data_scientists_who_like("Big Data"))


from collections import defaultdict

# user ids by interest 
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

print(user_ids_by_interest)


# interest by user id 
interests_by_user_id = defaultdict(list)
for user_id,interest in interests:
    interests_by_user_id[user_id].append(interest)

print("-------------------------------------------------------------------------")
print(interests_by_user_id)