def sol(n):
    steps, x, y, z = 0, 0, 0, 0
    Triple_step(n, x, y, z)


# 这个答案是错误的！ 因为是顺序敏感，而不是仅仅计算组合的数量。你还需要把组合内部打乱顺序的那些组合计算出来才行
def Triple_step(n, x, y, z):
    steps = 0
    for x in range(0, n // 1 + 1):
        for y in range(0, n // 2 + 1):
            for z in range(0, n // 3 + 1):
                if 1 * x + 2 * y + 3 * z == n:
                    print((x, y, z))
                    steps += 1
                z += 1
            y += 1
        x += 1

    return steps


# 我还是比较推崇这个方法
def triple_step(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)


# print(triple_step(5))

# 用缓存优化
def triple_step2(n, hdict):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n not in hdict:
        hdict[n] = triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)
    return hdict[n]


hd = dict()
print(triple_step2(9, hd))


# 这个方法不好理解，是书上的答案。不用看了
def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n - 1) + countWays(n - 2) + countWays(n - 3)


print(countWays(9))
