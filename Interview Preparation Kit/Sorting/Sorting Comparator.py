'''https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting'''
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        print("in repr")

    def comparator(a, b):
        if (a.score == b.score):
            a_len = len(a.name)
            b_len = len(b.name)
            min_len = min(a_len, b_len)
            for i in range(0, min_len):
                if (a.name[i] < b.name[i]):
                    return -1
                if (a.name[i] > b.name[i]):
                    return 1
            if (a_len < b_len):
                return -1
            elif (a_len > b_len):
                return 1
            else:
                return 1
        elif (a.score < b.score):
            return 1
        else:
            return -1


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
