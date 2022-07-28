from inputs.inputs import *  # This line should be included to the functions.py as well. Otherwise, the variables and parameters of main document are not loaded to the functions.
from functions.functions import *

iteration = 0
results_dict = {}
buyback_percent_opt = 0
profit_m_opt = 0
k_opt = 0

buyback_percent_arr = []
prof_m_arr = []

SL_range = np.arange(SL0, 1, 0.01).tolist()
buyback_percent_range = np.arange(0, 1, 0.1).tolist()


for buyback_percent in buyback_percent_range:
    print("buyback_percent=", buyback_percent)
    profit_r_opt = 0
    k_opt = 0
    SL_opt = 0

    for SL in SL_range:
        mu_SL = mu(SL)
        sigma_SL = sigma(SL)
        k = so.fsolve(SL_, 0, args=(SL))[0]
        prof_r = profit_r1(SL, k, buyback_percent)

        if prof_r > profit_r_opt:
            profit_r_opt = prof_r
            k_opt = k
            SL_opt = SL

    prof_m = profit_m(SL_opt, k_opt, buyback_percent)

    if prof_m > profit_m_opt:
        profit_m_opt = prof_m
        profit_r_m_opt = profit_r_opt
        buyback_percent_opt = buyback_percent
        k_opt_m = k_opt
        SL_opt_m = SL

    # Save the result of current iteration to a temporary jason
    result_iteration = {
        "buyback_percent": buyback_percent,
        "profit_r_opt": profit_r_opt,
        "k_opt": k_opt,
        "SL_opt": SL_opt,
        "prof_m": prof_m,
        "profit_r_m_opt": profit_r_m_opt
    }

    # Include the result of current iteration (result_iteration) to results final dictionary
    results_dict[iteration] = result_iteration
    iteration = iteration+1
    pprint(results_dict)

print(profit_m_opt)
print(profit_r_m_opt)
print(buyback_percent_opt)
print(k_opt_m)
print(SL_opt_m)

# Save Dictionary to JSON
with open("results_with_buyback.json", "w") as write_file:
    json.dump(results_dict, write_file, cls=NumpyArrayEncoder)

# Load JSON to a Dictionary
with open("results_with_buyback.json", "r") as read_file:
    results_with_buyback_json = json.load(read_file)

# convert the Results JSON to Excel and Save it
json_to_excel(results_with_buyback_json)

# Convert the second indent of json to a list
x_arr = [val['buyback_percent'] for key, val in results_with_buyback_json.items()]
y_arr = [val['prof_m'] for key, val in results_with_buyback_json.items()]

# Plot one graph
plt.plot(x_arr, y_arr)
plt.savefig('profM_buyback_perc.png')
plt.show()

# Plot two graphs
y1_arr = [val['k'] for key, val in results_with_buyback_json.items()]
figure, axis = plt.subplots(2)
axis[0].plot(x_arr, y_arr)
axis[1].plot(x1_arr, y_arr)
plt.show()
