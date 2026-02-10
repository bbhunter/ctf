# misc/endians
flag="氀愀挀琀昀笀㄀开猀甀爀㌀开栀　瀀攀开琀栀㄀猀开搀　攀猀开渀　琀开最㌀琀开氀　猀琀开㄀渀开琀爀愀渀猀氀愀琀椀　渀℀紀"
print("".join([chr(b) for b in flag.encode("UTF-16-LE") if b != 0]))


# $ python endians.py
# lactf{1_sur3_h0pe_th1s_d0es_n0t_g3t_l0st_1n_translati0n!}
# [ 11:20:03 ] bl4de @ ~/hacking/ctf/2026/LACTF_2026 (master)