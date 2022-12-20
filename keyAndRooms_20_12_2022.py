from typing import List
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    lock_status = [False for _ in range(len(rooms))]

    next_key = set(rooms[0])
    lock_status[0] = True
    unlock = set([0])
    while len(next_key):
        print(next_key, "===============")
        set_key = set()
        for key in next_key:
            lock_status[key] = True
            set_key.update(rooms[key])
        next_key = set_key
        if unlock == unlock | next_key:
            break
        unlock = unlock | next_key

    return all(lock_status)


print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
