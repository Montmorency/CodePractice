class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return ' '.join(map(str, [name, score]))
    def comparator(b, a):
        if a.score < b.score:
            return -1
        elif a.score > b.score:
            return 1
        elif a.score == b.score:
            if len(a.name) == len(b.name):
                for i,j in zip(a.name,b.name):
                    if i < j:
                        return 1
                    elif i > j:
                        return -1
                return 0
            elif len(a.name) < len(b.name):
                for i,j in zip(a.name, b.name):
                    if i < j:
                        return 1
                    elif i > j:
                        return -1
                return 1 
            elif len(a.name) > len(b.name):
                for i,j in zip(a.name, b.name):
                    if i < j:
                        return 1
                    elif i > j:
                        return -1
                return -1 
