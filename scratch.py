from datetime import datetime

now = datetime.now()

print(now)
print(now.strftime("%I:%M %p"))
print(now.strftime("%H:%M %p"))
print(now.strftime("%A %d %B,%Y"))



print(now.strftime("%B"))
print(now.strftime("%Y"))
print(now.strftime("%I"))
print(now.strftime("%M"))