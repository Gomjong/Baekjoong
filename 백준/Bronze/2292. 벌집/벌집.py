n = int(input())
cnt = 1 # 카운트
move = 1 # 벌집이동

while n>move:
    move=move+cnt*6
    cnt=cnt+1

print(cnt)
    