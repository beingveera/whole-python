print({1,2,3,4,5}.intersection({1,3,5}))
print({1,2,3,4}.union({5,6,7,8,3}))
print({1,2,3,4}.difference({0,2,4}))
print({1,2,3,4}-{0,2,4})
print({1,2,3,4}.symmetric_difference({0,2,4}))
print({1,2,3,4}^{0,2,4})
print({1,3,5,4}.issuperset({1,3,4}))
print({1,2,3,5}>={2,3,5})
print({2,3,4}.issubset({1,2,3,4}))
print({2,3,4,5} <= {2,3,4})
print({1,2,3}.isdisjoint({4,5}))
print({1,2,3}.isdisjoint({1,6}))
print(2 in {1,2,3})
print(4 in {1,2,3})
print(4 not in {1,2,3})

s={1,2,3,4}
s.add(5)
print(s)
s.discard(2)
print(s)
s.remove(3)
print(s)
s |= {2,3,4}
print(s)
s |= {10,20,30}
print(s)
s &={1,2,30}
print(s)
s -= {2,4,6}
print(s)
s.update({1,3,5,7})
print(s)
