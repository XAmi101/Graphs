import random

class User:
    def __init__(self, name):
        self.name = name

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # Use add_user num_users times

        # Create friendships (bidirectional friendship)
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")

        # Create/Generate all friendship combos empty list
        possible_friendships = []

        # Avoid duplicates by making sure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))
        print("   - Possiible friendships  ")
        print(possible_friendships)
        print("  -  ")
        # Shuffle all possible friendships
        random.shuffle(possible_friendships)

        # Create for firstX pairs is total //2(how many calls ) 1:51
        for i in range(num_users * avg_friendships// 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])



        # Create friendships
        	       
        # * Hint 1: To create N random friendships, 
        # you could create a list with all possible friendship combinations, 
        # shuffle the list, then grab the first N elements from the list. 
        # You will need to `import random` to get shuffle.
        # * Hint 2: `add_friendship(1, 2)` is the same as `add_friendship(2, 1)`. 
        # You should avoid calling one after the other since it will do nothing but print a warning. 
        # You can avoid this by only creating friendships where user1 < user2. (friend 1 is lower than friend 2)
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # Create a Queue and enqueue(add) starting vertex       
        qq = Queue()
        # Put the starting point in that
        qq.enqueue([user_id])
        # Make a set to keep track of visited vertices 
        vvisited = set()
            # # Track the path, Farthest distance from the input individual.
            # longest_path = [starting_vertex]
        # While the queue/stack isnt empty
        while qq.size() > 0:
            #dequeue the first item
            path = qq.dequeue()
            # Grab the last vertex from the PATH, returns -1 if there is no grandparent
            newuser_last_vertex = path[-1]
            
            # If not visited
            if newuser_last_vertex not in vvisited:
                # DO THE THING!! (search stop when you find something)
                print(newuser_last_vertex)
                # mark as visited
                vvisited.add(newuser_last_vertex)
                # For each edge in the item add a path to its neighbor to the end of the queue
                for next_vert_neighbor in self.friendships(newuser_last_vertex):
                    # Copy the path
                    new_path = list(path)
                    # Append the neighbor to the new path
                    new_path.append(next_vert_neighbor)
                    # Add that edge to the queue/stack
                    qq.enqueue(new_path)
                    # Enqueue the new path to the back of the queue
     

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

