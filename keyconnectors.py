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



#print(users)