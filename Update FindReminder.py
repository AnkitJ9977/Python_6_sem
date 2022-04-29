@@ -1,6 +1,4 @@
a = int(input())
tests = []
for i in range(a):
    tests.append([int(i) for i in input().split()])
for i in tests:
    print(i[0]%i[1]
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(A%B)
