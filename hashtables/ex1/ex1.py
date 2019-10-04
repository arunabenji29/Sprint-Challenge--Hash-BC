#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    answer = []
    retrieve = ht.storage
    for weight in weights:
        hash_table_insert(ht,weight,weight)

    if length > 1:


        for i in range(len(retrieve)):
            first_el = None
            second_el = None
            first_i = None
            second_i = None
            retrieve_first = None
            retrieve_second = None

            if retrieve[i] is not None:
                first_el = retrieve[i].key
                second_el = limit - first_el
                retrieve_first = hash_table_retrieve(ht,first_el)
                retrieve_second = hash_table_retrieve(ht,second_el)

            if retrieve_first is not None and retrieve_second is not None and retrieve_first + retrieve_second == limit :
                
                if retrieve_first == retrieve_second :
                    result = [i for i, e in enumerate(weights) if e == retrieve_first]
                    if result[0] >= result[1]:
                        answer.append(result[0])
                        answer.append(result[1])
                    else:
                        answer.append(result[1])
                        answer.append(result[0])
                    return answer

                first_i = weights.index(retrieve_first)
                second_i = weights.index(retrieve_second)

                if first_i >= second_i:
                    answer.append(first_i)
                    answer.append(second_i)
                else:                    
                    answer.append(second_i)
                    answer.append(first_i)
                return answer
            
    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
