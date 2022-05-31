#age: age of the individual in years /sex: 0 for female, 1 for male/ bmi: individual’s body mass index / num_of_children: number of children the individual has / smoker: 0 for a non-smoker, 1 for a smoker

# Create calculate_insurance_cost() function below: 

def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)
# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)
# This is going to be my own insurance cost
rafael_insurance_cost = calculate_insurance_cost("Rafael", 17, 1, 24.5, 0, 0)
