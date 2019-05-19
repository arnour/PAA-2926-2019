from paa191t1.pph import pph_med2

a0 = 100
b0 = 10

# a = [2, 1, 3, 5, 16]
# b = [5, 3, 9, 16, 16]

a = [2, 1, 3, 6, 5]
b = [5, 3, 8, 6, 16]
       
K = [0, 1, 2, 3, 4]
ab = [a[i]/b[i] for i in K]
print(K)
print(a)
print(b)
print(ab)
print(sorted(ab))

I1 = pph_med2(a0, b0, a, b, K)

print('I1', I1)