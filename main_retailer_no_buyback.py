from inputs.inputs import *
from functions.functions import *

profit_opt = 0
k_opt = 0

alpha = 0.1
beta = 1

k_arr = []
prof_arr = []
SL_arr = []

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

print(profit_opt)
print(k_opt)
print(SL_opt)
