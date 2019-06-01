def sum_product(L1, L2):
	sum_product = 0
	while len(L1) and len(L2) > 0:
		sum_product += L1[0]*L2[0]
		L1 = L1[1:]
		L2 = L2[1:]
	return sum_product
