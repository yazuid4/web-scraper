import os
import time

res_dir = 'results'
entries = os.listdir(res_dir)

ts = time.time()

for entry in entries:
	file_ts = entry.split('_')[1][:-4]
	delta_ts = ts - int(file_ts)
	
	if delta_ts / 60 > 5:
		os.remove(res_dir+'/'+entry)
