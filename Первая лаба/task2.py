k = 1024
Kb = k
Mb = k * Kb
disceta = 1.44 * Mb
symvol = 4
stroki = symvol * 25
n_strok = 50 * stroki
kniga = 100 * n_strok
answer = disceta // kniga
print("Количество книг, помещающихся на дискету:", int(answer))
