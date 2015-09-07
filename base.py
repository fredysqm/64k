#import redis

digits62 = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 69069
c = 1
m = 4294967296
#x_n = 667668

def a_base62(n):
    out = ''
    while (n != 0):
        out += digits62[n % 62]
        n = n // 62
    return out

def main():
    x_n = 667668
    n = ( (a * x_n) + c ) % m
    i = 1
    while (x_n != n):
        n = ( (a * n) + c ) % m
        i += 1
    print(i)

if __name__ == '__main__':
    main()
