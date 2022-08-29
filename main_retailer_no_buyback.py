from inputs.inputs import *  # This line should be included to the functions.py as well. Otherwise, the variables and parameters of main document are not loaded to the functions.
from functions.functions import *

profit_opt = 0
k_opt = 0
iteration = 0

k_arr = []
prof_arr = []
SL_arr = []
results_dict = {}

SL_range = np.arange(SL0, 1, 0.01).tolist()

for SL in SL_range:
    mu_SL = mu(SL)
    sigma_SL = sigma(SL)
    print("mu=", mu_SL)
    print("sigma=", sigma_SL)
    k = so.fsolve(SL_, 0, args=(SL))[0]
    prof = profit_r(SL, k)
    print("SL", SL)
    print("k=", k)
    print("profit_r=", prof)
    print("----------")

    k_arr.append(k)
    prof_arr.append(prof)
    SL_arr.append(SL)

    if prof > profit_opt:
        profit_opt = prof
        k_opt = k
        SL_opt = SL

    # Save the result of current iteration to a temporary jason
    result_iteration = {
        "mu_sl": mu(SL),
        "sigma_SL": sigma(SL),
        "SL": SL,
        "k": k,
        "profit_r": prof,
    }

    # Include the result of current iteration (result_iteration) to results final dictionary
    results_dict[iteration] = result_iteration
    iteration = iteration+1
    pprint(results_dict)

print(profit_opt)
print(k_opt)
print(SL_opt)

# Save Dictionary to JSON
with open("results.json", "w") as write_file:
    json.dump(results_dict, write_file, cls=NumpyArrayEncoder)

# Load JSON to a Dictionary
with open("results.json", "r") as read_file:
    results_json = json.load(read_file)

# convert the Results JSON to Excel and Save it
json_to_excel(results_json)

# Convert the second indent of json to a list
x_arr = [val['SL'] for key, val in results_json.items()]
y_arr = [val['profit_r'] for key, val in results_json.items()]

# Plot one graph
plt.plot(x_arr, y_arr)
plt.show()

# Plot two graphs
x1_arr = [val['k'] for key, val in results_json.items()]
figure, axis = plt.subplots(2)
axis[0].plot(x_arr, y_arr)
axis[1].plot(x1_arr, y_arr)
plt.show()
###