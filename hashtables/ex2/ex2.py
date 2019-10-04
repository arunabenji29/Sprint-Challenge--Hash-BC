#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
        # print(f'source: {i.source}')
        # print(f'destination: {i.destination}')
        hash_table_insert(hashtable,i.source,i.destination)

    count=0
    prev= "NONE"
    while count<length:
        
        route[count]= hash_table_retrieve(hashtable,prev)
        prev = route[count]
        count += 1
        

    return route
