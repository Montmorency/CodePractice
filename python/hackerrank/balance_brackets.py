def is_matched(expression):
    from collections import deque
    open_b = deque()
    if len(expression)%2 != 0:
        return False
    for s in expression:
        try:
            if s =='}':
                a = open_b.pop()
                if a != '{':
                    return False
            elif s ==')':
                a = open_b.pop()
                if a != '(':
                    return False
            elif s ==']':
                a = open_b.pop()
                if a != '[':
                    return False     
            else:
                open_b.append(s)
        except IndexError:
            return False
    if len(open_b) > 0:    
        return False
    else:
        return True
