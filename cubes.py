n = 200
results=set()
separator=', '
trivial=[1,8,27,64]
for i in range(-n,n):
  for j in range(-n,n):
    for k in range(-n,n):
      val = i*i*i + j*j*j + k*k*k 
      if val not in trivial and val < n and val > 0:
        factors = sorted([i,j,k])
        factorsStr = [str(x) for x in factors]
        results.add(str(val) + "=" + separator.join(factorsStr))

print(sorted(results))
print(len(results))
