medicalCosts = {}
medicalCosts.update({"Marina" : 6607.0 , "Vinay": 3225.0})
medicalCosts.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina":6420.0})
medicalCosts["Vinnay"] = 3325.0

totalCost = 0
for value in medicalCosts.values():
  totalCost += value

averageCost = totalCost / len(medicalCosts)

print(f"The total Insurance Cost is {totalCost} and the average cost is {averageCost}")
print(" ")

names = ["Marina", "Vinay", "Connie", "Issac", "Valentina"]
ages = [27, 24, 43, 35, 52]
zippedAges = zip(names, ages)
namesToAges = {key:value for key, value in zippedAges}

marinaAge = namesToAges.get("Marina")

medicalRecords = {}

medicalRecords.update({
  "Marina": {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance Cost": 6607.0} ,
 
 "Vinay":{"Age": 24, "Sex": "Male",	"BMI": 26.9, "Children": 0,	"Smoker": "Non-smoker", "Insurance Cost": 3225.0} , 
 
 "Connie": {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance Cost": 8886.0} , 
 
 "Isaac": {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance Cost": 16444.0} , 
 
 "Valentina": {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance Cost": 6420.0}})

ConnieRecord = medicalRecords["Connie"]["Insurance Cost"]
print(f"Connie's insurance cost is {ConnieRecord} dollars.")

medicalRecords.pop("Vinay")

for name, record in medicalRecords.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance Cost"]))
