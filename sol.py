# superBido
def d(num):
	sum_it = 0
	for x in range(1,num):
		if num % x == 0:
			sum_it += x 
	return sum_it 
	
def ds_ls_maker(num):
	ls_for_ds = []
	for n in range(1,num):
		ls_for_ds.append(d(n))
	return ls_for_ds

def ls_checker(num):
	ls_for_ds = ds_ls_maker(num)
	count_n = 0
	count_y = 0
	ls_of_ds_real = []
	for n in ls_for_ds:
		for x in ls_for_ds:
			if x != n and d(x) == n and d(n) == x:
				if x not in ls_of_ds_real:
					ls_of_ds_real.append(x)
				break
		count_n += 1
		count_y += 1
	return ls_of_ds_real

def total_ds(num):
	sum_d = 0
	my_ds = ls_checker(num)
	for n in my_ds:
		sum_d += n
	return sum_d

print sum(ls_checker(10000))

