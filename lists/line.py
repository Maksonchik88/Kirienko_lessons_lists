#Петя перешёл в другую школу.
# На уроке физкультуры ему понадобилось определить своё место в строю.
# Помогите ему это сделать.



line = [int(i) for i in input().split()]
n = int(input())
pos = 0
while pos < len(line) and line[pos] >= n:
    pos += 1
print(pos + 1)