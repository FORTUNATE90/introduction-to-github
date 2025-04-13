import time, random, matplotlib.pyplot as plt

# Cube root finder with steps and timing
def cube_root(n): s,t,a=0,time.time(),abs(n); l,h=0,a; neg=n<0
 while l<=h: s+=1; m=(l+h)//2; c=m**3; 
 if c==a: r=m;break
 elif c<a: l=m+1
 else: h=m-1
 else: r=h
 return (-r if neg else r),s,time.time()-t

# Primality check with step count
def is_prime(n): s=1
 if n<2: return 0,s
 if n==2: return 1,s
 if n%2==0: return 0,s+1
 for i in range(3,int(n**0.5)+1,2): s+=1
 if n%i==0: return 0,s
 return 1,s

# Graphing utility
def plot_graph(x, y1, y2, title1, title2, xlabel):
 plt.figure(figsize=(10,4))
 plt.subplot(1,2,1); plt.plot(x,y1,'o-'); plt.title(title1); plt.xlabel(xlabel); plt.ylabel("Steps")
 plt.subplot(1,2,2); plt.plot(x,y2,'o-r'); plt.title(title2); plt.xlabel(xlabel); plt.ylabel("Time (s)")
 plt.tight_layout(); plt.show()

# Cube root test
digits = range(1,10); steps,times = [],[]
for d in digits:
 _,s,t = cube_root(10**d-1)
 steps.append(s); times.append(t)
plot_graph(digits, steps, times, "Cube Root Steps", "Cube Root Time", "Digits")

# Prime test
print("Sum of primes 3–1000:", sum(i for i in range(3,1001) if is_prime(i)[0]))
steps,times=[],[]
for d in range(1,7):
 n=10**d+1; t0=time.time(); _,s=is_prime(n)
 steps.append(s); times.append(time.time()-t0)
plot_graph(range(1,7), steps, times, "Primality Steps", "Primality Time", "Digits")

# Optimal egg drop calculation (DP method)
def egg_drop(e,f):
 dp=[[0]*(f+1) for _ in range(e+1)]; t=0
 while dp[e][t]<f:
  t+=1
  for k in range(1,e+1): dp[k][t]=dp[k][t-1]+dp[k-1][t-1]+1
 return t

# Simulate egg drop with plotting
def simulate_egg(f=102,e=7,c=None):
 c=c or random.randint(1,f); print("Critical Floor:",c)
 l,h,r,s=1,f,[],e
 while l<=h and s:
  m=(l+h)//2; broke=m>c; r.append((m,broke))
  if broke: s-=1; h=m-1
  else: l=m+1
 return r,c

def plot_drops(r,cf):
 f=[x for x,_ in r]; col=['r' if b else 'g' for _,b in r]
 plt.figure(figsize=(5,7))
 plt.barh(f,[1]*len(f),color=col); plt.axhline(y=cf,color='blue',ls='--',label='Critical')
 plt.xlabel("Result"); plt.ylabel("Floors"); plt.gca().invert_yaxis(); plt.legend(); plt.title("Egg Drop"); plt.show()

print("Min drops (7 eggs, 102 floors):", egg_drop(7,102))
res, cf = simulate_egg()
plot_drops(res, cf)
