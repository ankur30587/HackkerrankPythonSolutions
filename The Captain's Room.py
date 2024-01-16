def find_captains_room(group_size, room_list):
    room_count = {}
    
    for room in room_list:
        if room in room_count:
            room_count[room] += 1
        else:
            room_count[room] = 1

    for room, count in room_count.items():
        if count == 1:
            return room

if __name__ == "__main__":
    group_size = int(input())
    room_list = list(map(int, input().split()))

    captains_room = find_captains_room(group_size, room_list)
    print(captains_room)
