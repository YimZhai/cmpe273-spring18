"""
Question:
Pick one IP from each region',' find network latency from via the below code snippet
(ping 3 times)',' and finally sort the average latency by region.
http://ec2-reachability.amazonaws.com/
Expected Output for all 15 regions:
1. us-west-1 [50.18.56.1] - 100ms (Smallest average latency)
2. xx-xxxx-x [xx.xx.xx.xx] - 200ms
3. xx-xxxx-x [xx.xx.xx.xx] - 300ms
...
15. xx-xxxx-x [xx.xx.xx.xx] - 1000ms (Largest average latency)
"""
from __future__ import print_function
import subprocess

hosts = {'us-east-1': '34.192.0.54', 'us-east-2': '13.58.0.253', 
'us-west-1': '13.56.63.251', 'us-west-2': '34.208.63.251', 
'us-gov-west-1': '52.61.0.254', 'ca-central-1': '35.182.0.251', 
'eu-west-1':'34.240.0.253', 'eu-central-1': '18.194.0.252', 'eu-west-2': '35.176.0.252', 
'ap-northeast-1': '13.112.63.251', 'ap-northeast-2': '13.124.63.251', 
'ap-southeast-1': '13.228.0.251', 'ap-southeast-2':'13.54.63.252', 
'ap-south-1':'13.126.0.252', 'sa-east-1':'18.231.0.252'}
result = {}

for region in list(hosts.keys()):
	# region represent all the keys(us-east-1, us-east-2, etc)
	host = hosts[region]
	# host represent all the value match the keys('34.192.0.54'...)
	# print(host)
	ping = subprocess.Popen(
	    ["ping", "-c", "3", host],
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE
	)
	out, error = ping.communicate()
	# print(out)

	avg_value = out.split(b"/")
	# print(avg_value)
	
	result[float(avg_value[4])] = region
	# assign region as value to the key which is the avg time
	# result is like {avg time: region}
	# print(result)

avgs = sorted(result.keys())
# sort the avg time
# print(avgs) 

count = 1
for avg in avgs:
	print('{0} {1} [{2}] {3}ms'.format(str(count), result[avg], hosts[result[avg]], str(avg)))
	# print(hosts[result[avg]])
	# result[avg] return the region & hosts[region] return the ip address
	count += 1


'''
Output:
1 us-west-1 [13.56.63.251] 4.373ms
2 us-west-2 [34.208.63.251] 25.732ms
3 us-gov-west-1 [52.61.0.254] 26.119ms
4 us-east-2 [13.58.0.253] 65.739ms
5 ca-central-1 [35.182.0.251] 79.187ms
6 ap-northeast-1 [13.112.63.251] 104.523ms
7 us-east-1 [34.192.0.54] 137.658ms
8 ap-northeast-2 [13.124.63.251] 187.229ms
9 eu-central-1 [18.194.0.252] 192.521ms
10 eu-west-2 [35.176.0.252] 199.446ms
11 eu-west-1 [34.240.0.253] 210.818ms
12 ap-southeast-2 [13.54.63.252] 224.965ms
13 sa-east-1 [18.231.0.252] 239.829ms
14 ap-southeast-1 [13.228.0.251] 254.816ms
15 ap-south-1 [13.126.0.252] 311.263ms
'''