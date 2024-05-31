n, m = map(int, input(). split())
cards = list(map(int, input(). split()))

blackjack = 0
temp = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp = cards[i] + cards[j] + cards[k]
            if temp > m:
                continue
            elif temp > blackjack:
                blackjack = temp
                
print(blackjack)
    
    



