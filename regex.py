from compreasset import new_server
from previousserver import old_server
faulty_assets=[]
for i in new_server:
	if i in old_server and old_server[i]>new_server[i]:
		print i,"old_server data:",old_server[i],"new_server data:",new_server[i]
		faulty_assets.append(i)



print faulty_assets