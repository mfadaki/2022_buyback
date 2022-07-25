def mu(SL):
    return mu_l + (1+alpha*(SL-SL0)*100)*mu_nl


def sigma(SL):
    return (sigma_l**2 + (1+beta**2 * alpha * (SL-SL0)*100) * sigma_nl**2)**0.5


def b(SL):
    return mu_l / mu(SL)


def integrand(u, k):
    return (u-k)*spt.norm.pdf(x=u, loc=0, scale=1)


def G_u_k(k):
    return si.quad(integrand, k, np.inf, args=(k,))[0]


def SL_(k, *args):
    SL = args[0]
    return SL - (b(SL)*(1-(G_u_k(k)*sigma(SL)/mu(SL))) + (1-b(SL)) * (mu(SL) / (mu(SL) + G_u_k(k) * sigma(SL))))


def Z(SL, k):
    return mu(SL) + k * sigma(SL)


def int1(x, SL, k):
    return (x-Z(SL, k))*spt.norm.pdf(x=x, loc=mu(SL), scale=sigma(SL))


def int1_(SL, k):
    return si.quad(int1, Z(SL, k), np.inf, args=(SL, k))[0]


def int2(x, SL, k):
    return (Z(SL, k)-x)*spt.norm.pdf(x=x, loc=mu(SL), scale=sigma(SL))


def int2_(SL, k):
    return si.quad(int2, 0, Z(SL, k), args=(SL, k))[0]


def profit_r(SL, k):
    return p_r * (mu(SL) - (1-b(SL)) * int1_(SL, k)) - b(SL)*c_b*int1_(SL, k) - c_h * int2_(SL, k)

