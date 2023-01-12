a, b = map(int, input().split())

sangsoo_a = a % 10 * 100 + a // 10 % 10 * 10 + a // 100 
sangsoo_b = b % 10 * 100 + b // 10 % 10 * 10 + b // 100

if sangsoo_a < sangsoo_b:
    print(sangsoo_b)
else:
    print(sangsoo_a)