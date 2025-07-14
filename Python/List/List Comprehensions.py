if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    may_list = []
    may_list2 = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                may_list.append([i,j,k])
    print(may_list)
    max = len(may_list) - 1
    for item in may_list:
        print(sum(item))
        if sum(item) != n:
            may_list2.append(item)

    print(may_list2)