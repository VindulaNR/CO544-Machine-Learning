import numpy as np # import numpy module as np


#df=pd.read_csv('Lab01\sampleDataSet.csv')
#print(df)
#3.f the random walk path
#taken 500 steps and walk between 0 to 10

import random
  
# Probability to move up or down
prob = [0.5, 0.5]  
  
# Get random starting point
start = random.randint(0,10)  
positions = [start]
  
# creating the random points
rr = np.random.random(500)
downp = rr < prob[0]
upp = rr > prob[1]
print(downp)
  
for idownp, iupp in zip(downp, upp):
    down = idownp and positions[-1] > 0
    up = iupp and positions[-1] < 10
    positions.append(positions[-1] - down + up)

print(positions)