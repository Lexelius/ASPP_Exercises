#!/usr/bin/env python
import time
t0 = time.time()
tN = 500
print('Heeeeeelllooooooo')
for i in range(tN):
	print(time.time()-t0)
	time.sleep(2)

print('Doooneeee!!')
