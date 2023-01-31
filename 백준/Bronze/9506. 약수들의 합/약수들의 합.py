while True:
    n = int(input())
    soo = []
    if n == -1 :
        break
    for i in range(1, n-1):
        if n % i == 0:
            soo.append(i)
    if sum(soo) == n:
        print(f"{n} = ", ' + '.join(str(i) for i in soo), sep="")
    else:
        print(f"{n} is NOT perfect.")