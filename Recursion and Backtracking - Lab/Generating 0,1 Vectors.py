def generator(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[idx] = num
        generator(idx + 1, vector)


n = int(input())
vector = [0] * n
generator(0, vector)
