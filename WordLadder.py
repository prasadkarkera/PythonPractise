# http://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/

from collections import deque

dictionary = ['poin', 'plia', 'poon', 'plee', 'same', 'poie', 'plie', 'plea', 'ploa', 'pooa']


def get_neighbours(start, visited):
    neighbours = []
    for word in dictionary:
        if not visited.get(word):
            number_of_different_letters = 0
            for i in range(len(start)):
                if start[i] != word[i]:
                    number_of_different_letters = number_of_different_letters + 1

                if number_of_different_letters > 1:
                    break

            if number_of_different_letters <= 1:
                neighbours.append(word)

    return neighbours


queue = deque()


def shortest_distance(start, end):

    queue.append((start, 0))

    visited = {}
    while len(queue) > 0:
        word, distance = queue.popleft()
        print(word)
        if end == word:
            return distance

        neighbours = get_neighbours(word, visited)

        for neighbour in neighbours:
            queue.append((neighbour, distance + 1))
            visited[neighbour] = 1

    return -1


start = 'toon'
end = 'plea'

print(shortest_distance(start, end))
