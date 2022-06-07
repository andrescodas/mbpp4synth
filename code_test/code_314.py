def max_sum_rectangular_grid(grid, n) : 
	"""
	Write a function to find out the maximum sum such that no two chosen numbers are adjacent for the given rectangular grid of dimension 2 x n.
	"""
	incl = max(grid[0][0], grid[1][0]) 
	excl = 0
	for i in range(1, n) : 
		excl_new = max(excl, incl) 
		incl = excl + max(grid[0][i], grid[1][i]) 
		excl = excl_new 
	return max(excl, incl)
