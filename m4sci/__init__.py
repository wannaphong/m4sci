def gcd(a,b): # Euclidean Algorithm https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
 if a==0:
  return b
 elif b==0:
  return a
 else:
  q=int(a/b)
  r=a-(b*q)
  return GCD(b,r)
