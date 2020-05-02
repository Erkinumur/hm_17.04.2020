def countingValleys(n, s):
    level = 0
    level_down = False
    res = 0
    for i in list(s):
        if i == 'U':
            level += 1
        else:
            level -= 1
        
        if level < 0:
            level_down = True

        if level == 0 and level_down:
            res += 1
            level_down = False
            
    return res