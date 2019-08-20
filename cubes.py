n = 100
results=set()
separator=', '
for i in range(-n,n):
  for j in range(-n,n):
    for k in range(-n,n):
      val = i*i*i + j*j*j + k*k*k 
      if val!=1 and val < n and val > 0:
        factors = sorted([i,j,k])
        factorsStr = [str(x) for x in factors]
        results.add(str(val) + "=" + separator.join(factorsStr))

print(sorted(results))
