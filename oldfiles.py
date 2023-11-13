mport os
import time
day = 86400
hour = 3600
minute = 60
week = 604800
month = 2628000
year = 31536000
inputList = ["minutes","hours",'days',"weeks",'months','years',]
timeList = [minute, hour, day, week, month, year]
loop = 0
while loop == 0:
  answer = input("How old are the files you want to delete? ")
  if answer.isdigit() == False:
    print('Invalid Input')
    continue
  timetype = input('minutes, hours, days, weeks, months, years ').lower()
  if timetype not in inputList:
    print('Invalid Input')
    continue
  for times in inputList:
    if times == timetype:
      position = inputList.index(times)
      timeValue = timeList[position]
  while True:
    confirmation = input(f'so files older than {answer, inputList[position]}, correct?')   
    if confirmation in ["correct","yes","y"]:
        loop = 1
        break
    elif confirmation in ["no","n"]:
      break
    else:
      print("retry")
      continue
  
directory = "files"

#print(os.listdir(directory))
oldFileList = []
files = os.listdir(directory)
oldFileCount = 0
for file in files:
  filePath = os.path.join(directory, file)
  localTime = os.path.getctime(filePath)
  print(file, " : ", os.path.getctime(filePath), " : ", localTime)
  currentTime = time.time()
  # print(localTime)
  # print(currentTime)
  print(timeValue)
  # print(amountSpecified)
  if int(localTime) < (int(currentTime) - (int(timeValue) * int(answer))):
    oldFileList.append(filePath)
    oldFileCount += 1

print(f'found {oldFileCount} old files')
if oldFileCount == 0:
  quit()
print(oldFileList)
delete = input('You want to remove these files?').lower()
if delete == "yes":
  for x in oldFileList:
    print("goodbye",x)
    os.remove(x)
    
else:
  quit()
        #os.remove(file_location)
