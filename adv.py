from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# keep track of reversal
# reversal_path = []


def traverse_map(starting_room, visited=None):
    if visited is None:
        visited = {}
    starting_room = player.current_room.id
    print('PLAYER ROOM ID', player.current_room.id)
    visited[starting_room] = player.current_room.get_exits()
    print('VISITED', visited)
    # iterate through exits
    while len(visited) < len(world.rooms):
        for room_exit in player.current_room.get_exits():
            # if exit has not been visited, travel to that exit
            player.travel(room_exit)
            if player.current_room.id not in traversal_path:
                traversal_path.append(
                    (player.current_room.id, player.current_room.get_exits()))
            if player.current_room.id not in visited:
                new_path = traverse_map(player.current_room.id, visited)
                if new_path:
                    return new_path
            if player.current_room.id in visited:
                player.travel(reverse[room_exit])
        print('TRAVERSAL PATH', traversal_path)
        return traversal_path


# check to see if we are at a dead end
# if we are move in the reverse direction until we get to a room that is not visited
# figure out how to update traversal path

print(traverse_map(0))
# traversal_path = traverse_map(player.current_room.id)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
