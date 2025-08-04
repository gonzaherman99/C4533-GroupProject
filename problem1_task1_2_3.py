def brute_force_p1(A):
	"""
	Brute force solution for single transaction
	Time Complexity: O(m * n^2)

	Approach:
		- Iterate through all stocks
		- For each stock, check all possible buy-sell day combinations
		- Track the transaction with maximum profit
	Assume:
		- Matrix A contains valid numerical data
		- Days are in chronological order (columns 0 to n-1)
	"""
	m, n = len(A), len(A[0])
	best_profit = 0
	best_stock, best_buy, best_sell = -1, -1, -1
    	
	# Iterate through all stocks
	for i in range(m):
		# Check all possible buy days
		for buy in range(n):
			# Check all possible sell days AFTER buy day
			for sell in range(buy + 1, n):
				# Calculate potential profit
				profit = A[i][sell] - A[i][buy]
				
				# Update best transaction if better profit is found	
				if profit > best_profit:
					best_profit = profit
					best_stock, best_buy, best_sell = i, buy, sell

	# Return (0, 0, 0, 0) if there are no profitable transactions
	if best_profit <= 0:
		return (0, 0, 0, 0)
	
	# Convert to 1-based index and return
	return (best_stock + 1, best_buy + 1, best_sell + 1, best_profit)

def greedy_p1(A):
	"""
	Greedy solution for single transaction
	Time Complexity: O(m * n)

	Approach:
		- For each stock, track minimum price encountered
		- Calculate potential profit using current day's price
		- Update global maximum profit when better solution found
	Assume:
		- Prices are non-negative
		- At least one day of data exists
	"""
	m, n = len(A), len(A[0])
	best_profit = 0
	best_stock, best_buy, best_sell = -1, -1, -1
    
	# Process each stock separately
	for i in range(m):
		min_price = A[i][0]  # Initialize minimum price
		min_index = 0        # Day of minimum price
        
		# Iterate through each day
		for j in range(1, n):
			# Update minimum price if lower price found
			if A[i][j] < min_price:
				min_price = A[i][j]
				min_index = j

			# Calculate potential profit
			profit = A[i][j] - min_price

			# Update global best if better profit
			if profit > best_profit:
				best_profit = profit
				best_stock = i
				best_buy = min_index
				best_sell = j
    
	# Return (0, 0, 0, 0) if there are no profitable transactions
	if best_profit <= 0:
		return (0, 0, 0, 0)
    
	# Convert to 1-based index and return
	return (best_stock + 1, best_buy + 1, best_sell + 1, best_profit)

def dp_p1(A):
    """
    Dynamic programming solution for single transaction
    Time Complexity: O(m * n)

	Approach:
		- Maintain running minimum price for each stock
		- Calculate max profit as current price minus minimum
		- Update global optimum when better solution found
	Assume:
		- Prices change daily
		- No missing data points
    """
    m, n = len(A), len(A[0])
    best_profit = 0
    best_stock, best_buy, best_sell = -1, -1, -1
    
    for i in range(m):
        min_price = A[i][0]  # Initialize min price to day 0
        min_index = 0        # Day of min price
        max_profit = 0       # Best profit for current stock
        buy_index, sell_index = 0, 0  # Transaction days for stock

		# Process each day
        for j in range(1, n):
			# Update minimum price if found better buy point
            if A[i][j] < min_price:
                min_price = A[i][j]
                min_index = j

			# Calculate current profit
            profit = A[i][j] - min_price

			# Update best transaction for current stock
            if profit > max_profit:
                max_profit = profit
                buy_index = min_index
                sell_index = j

		# Update global best transaction
        if max_profit > best_profit:
            best_profit = max_profit
            best_stock = i
            best_buy = buy_index
            best_sell = sell_index

	# Return (0, 0, 0, 0) if there are no profitable transactions
    if best_profit <= 0:
        return (0, 0, 0, 0)
	
	# Convert to 1-based indexing
    return (best_stock + 1, best_buy + 1, best_sell + 1, best_profit)