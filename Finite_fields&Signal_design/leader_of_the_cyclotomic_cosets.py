def cyclotomic_cosets(p, n):
	# p = int(input('域的特征：'))
	# n = int(input('域关于特征的幂次：'))
	residue_list = []
	leader_list = []
	cyclotomic_list = []
	mod_number = (p ** n) - 1
	for j in range(1, mod_number):
		residue_list.append(j)
	i = 0
	leader_list.append(i)
	cyclotomic_list.append([i])
	while len(residue_list) != 0:
		i += 1
		k = i * p
		cyclotomic_list.append([])
		cyclotomic_list[-1].append(i)
		leader_list.append(i)
		residue_list.remove(i)
		while i != k:
			cyclotomic_list[-1].append(k)
			residue_list.remove(k)
			k = (k * p) % mod_number
		while (i + 1) not in residue_list and len(residue_list) != 0:
			i = i + 1
	return (cyclotomic_list,leader_list)


def cyclotomic_cosets_mod_N(p, a):
	# p = int(input('域的特征：'))
	# n = int(input('域关于特征的幂次：'))
	residue_list = []
	leader_list = []
	cyclotomic_list = []
	mod_number = a
	for k in range(1, a):
		residue_list.append(k)
	i = 0
	leader_list.append(i)
	cyclotomic_list.append([i])
	while len(residue_list) != 0:
		i += 1
		k = i * p
		cyclotomic_list.append([])
		cyclotomic_list[-1].append(i)
		leader_list.append(i)
		residue_list.remove(i)
		while i != k:
			cyclotomic_list[-1].append(k)
			residue_list.remove(k)
			k = (k * p) % mod_number
		while (i + 1) not in residue_list and len(residue_list) != 0:
			i = i + 1
	return (cyclotomic_list, leader_list)


cyc1, lea1 = cyclotomic_cosets(2, 4)
for a in range(len(cyc1)):
	print(cyc1[a], end='\n')
print(lea1)
