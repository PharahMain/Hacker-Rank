# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

q = int(input())
eng = set(map(int, input().split(' ')))
p = int(input())
frn = set(map(int, input().split(' ')))

both = set(eng & frn)

print(len(both))