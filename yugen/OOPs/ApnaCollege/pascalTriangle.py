def generate(numRows: int):
        p_l = []
        for i in range(numRows):
            if i == 0:
                p_l = [[1]]
            else:
                p = []
                for j in range(i+1):
                    if j in (0, i):
                        p.append(1)
                    else:
                        p.append(p_l[i-1][j-1] + p_l[i-1][j])
                p_l.append(p)
        return p_l

print(generate(5))