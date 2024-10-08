import subprocess
import re

result = subprocess.run("Ping 127.0.0.1", stdout=subprocess.PIPE,text=True)


print(result.stdout)


pattern = r"Sent = ([0-9]+), Received = (\d+)"

ans = re.findall(pattern,result.stdout)

print(ans)

print("Sent : ", ans[0][0], " Recieved : " , ans[0][1])


ans = re.search(pattern,result.stdout)

print(ans)

print("Sent : ", ans.group(1), " Recieved : " , ans.group(2))