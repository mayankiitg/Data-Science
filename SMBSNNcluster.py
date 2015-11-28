import os,sys,math

fname="sample2.txt"
fp=open(fname,'r')
cont=fp.read()
# data contain all raw data set in list format
data=[]
for row in cont.split('\n'):
	b=[]
	for c in row.split(','):
		b.append(float(c.strip()))	
	data.append(b)

print data
########################### FUNCTION
def dist(a,b):
	d=0
	for i in range(0,len(a)):
		d+=(a[i]-b[i])*(a[i]-b[i])
	return math.sqrt(d)

###########################

########################### GLOBAL VARS AND PARAMETERS
n=len(data)
k=7				# k nearest neighbours
ke=3			# thresold for shared neighbours																											
labletable=[]	#contain k nearest neighbours's label
###########################			

# label table formation ---

# dp1 -> datapoint1 dp2->datapoint2 l1->temporary list of nearest neighbours 
# l_dist-> temp list for nearest neighbours distances																																
for idx1,dp1 in enumerate(data):
	l1=[]			# for one data point
	l_dist=[]		#store distances
	l1.append(idx1)
	l_dist.append(0)
	for idx2,dp2 in enumerate(data):
		if not idx1==idx2:
			d=dist(dp1,dp2)
			temp=0
			if(len(l1)<k+1):
				for i in range(0,len(l1)):
					if(l_dist[i]>d):
						l1.insert(i,idx2)
						l_dist.insert(i,d)
						temp=1
						break
				if temp==0:
					l1.append(idx2)
					l_dist.append(d)
			elif(l_dist[k]>d):
				for i in range(0,len(l1)):
					if(l_dist[i]>d):
						l1.insert(i,idx2)
						l_dist.insert(i,d)
						l1.pop()
						l_dist.pop()
						temp=1
						break
				if temp==0:
					l1.pop()
					l_dist.pop()
					l1.append(idx2)
					l_dist.append(d)
	# print "data point ",idx1
	# print l1
	# print l_dist
	labletable.append(l1)

# print "labletable: \n"

# for row in labletable:
# 	print row

# step 3 of algo in paper
# cluster formation

for dp1 in labletable:
	for dp2 in labletable:
		count=0
		if not dp1[0]==dp2[0]:
			if (dp1[0] in dp2) and (dp2[0] in dp1):
				for elem in dp1:
					if elem in dp2:
						count+=1
				if count>=ke:
					if(dp2[0]>dp1[0]):
						find=dp2[0]
						repl=dp1[0]
					else:
						find=dp1[0]
						repl=dp2[0]
					for dp in labletable:
						for idx,d1 in enumerate(dp):
							if(d1==find):
								dp[idx]=repl

# print "labletable: \n"
# for row in labletable:
# 	print row

# find cluster and print

cluster={}
for idx,dp in enumerate(labletable):
	if not dp[0] in cluster.keys():
		cluster[dp[0]]=[]
	cluster[dp[0]].append(idx)
	

for key in cluster.keys():
	print key,cluster[key]
