import time
current_time=int(time.time())
gen_num=(current_time%100)+50
if gen_num%2==0:
      gen_num+=10


print(gen_num)
