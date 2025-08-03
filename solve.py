import json

def solve():
    grid = []
    loc = []
    words = []
    length = 0

    with open('assets/grid.json','r',encoding='utf-8') as f:
        data = json.load(f)

    val = -1
    for d in data["rec_boxes"]:
        if d[0] > val:
            val = d[0]
            length += 1
        else:
            break

    temp = []
    for d in data["rec_texts"]:
        if d == '_':
            d = 'I'
        if d == '0':
            d = 'O'
        d = d.upper()
        temp.append(d)
        if len(temp) == length:
            grid.append(temp)
            temp = []

    temp = []
    for d in data["rec_boxes"]:
        temp.append(d)
        if len(temp) == length:
            loc.append(temp)
            temp = []

    with open('assets/words.json','r',encoding='utf-8') as f:
        data = json.load(f)

    for d in data["rec_texts"]:
        d.replace('_','I')
        words.append(d)

    width = len(grid)
    dir = [[1,0],[0,1],[0,-1],[-1,0],[1,-1],[1,1],[-1,1],[-1,-1]]
    answers = []

    for word in words:
        flag = 0
        for x in range(width):
            for y in range(length):
                cnt = -1
                for d in dir:
                    i = x
                    j = y
                    cnt += 1
                    pos = 0
                    while 0 <= i < width and 0 <= j < length and pos < len(word) and word[pos] == grid[i][j]:
                        i += d[0]
                        j += d[1]
                        pos += 1
                    if pos == len(word):
                        answers.append([loc[x][y],loc[i-d[0]][j-d[1]],cnt])
                        flag = 1
                        break
                if flag:
                    break
            if flag:
                break
                
    print(answers)
    return answers