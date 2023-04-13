medicalData = """Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Replacing '#' instances for '$'.
medicalDataUpdate = medicalData.replace("#", "$")
#print(medicalDataUpdate)

# Calculating the number of Medical Records
numRecord = 0
for i in medicalDataUpdate:
  if i == '$':
    numRecord += 1
# Cleaning the data
medicalDataSplit = medicalDataUpdate.split(';')

medicalRecords = []
for record in medicalDataSplit:
    medicalRecords.append(record.split(','))

medicalRecordsClean = []

for record in medicalRecords:
  recordClean = []
  for item in record:
    recordClean.append(item.strip())
  medicalRecordsClean.append(recordClean)

#Separating into differente list

names = []
ages = []
bmis = []
insuranceCosts = []

for record in medicalRecordsClean:
    record[0] = record[0].upper()
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insuranceCosts.append(record[3])

print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: "  + str(bmis))
print("Insurance Costs: " + str(insuranceCosts))

#Calculating Average BMI and Average Insurance Cost
totalBMI = 0
for bmi in bmis:
  totalBMI += float(bmi)

averageBMI = (totalBMI / len(bmis))

print(f"Average BMI: {averageBMI: .3f}")

avgInsurance = 0
for avg in insuranceCosts:
    avgReplace = avg.replace("$","")
    avgInsurance += float(avgReplace)
    avgInsurance = avgInsurance / len(insuranceCosts)

print(f"Average Insurance Cost: {avgInsurance}") 

#Finishing steps
count = 0
for info in names:
  print(f"{names[count]} is {ages[count]} years old with a BMI of {bmis[count]} and an insurance cost of {insuranceCosts[count]}.")
  count += 1