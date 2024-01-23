names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

updated_estimated_costs = [estimated_costs*11/10 for estimated_costs in estimated_insurance_costs]

# Add your code here
total_cost = 0

while total_cost <= len(actual_insurance_costs):
  total_cost = sum(actual_insurance_costs)

print("Total cost: " + str(total_cost))

average_cost = total_cost/len(actual_insurance_costs)
print("The average insurance cost is: " + str(average_cost))
print(" ----- ")

for i in range(len(names)):
  name = names[i]
  insurance_costs = actual_insurance_costs[i]
  cost_difference = insurance_costs - average_cost

  print("The insurance cost for " + name + " is " + str(insurance_costs) + " dollars.")

  if insurance_costs > average_cost:
    print("The insurance cost for " + name + " is above average by " + str(cost_difference))
    print(" ----- ")
  elif insurance_costs < average_cost:
    print("The insurance cost for " + name + " is below average by " + str(cost_difference))
    print(" ----- ")
  else:
    print("The insurance cost for " + name + " is equal to average by " + str(cost_difference))
    print(" ----- ")
print("Estimated insurance costs are 10% higher than originally thought. The updated costs are as follows: " + str(updated_estimated_costs))
