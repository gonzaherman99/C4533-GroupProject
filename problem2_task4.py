def dp_problem2_n2k(A, k):
    """
    Dynamic Programming solution for Problem 2 
    Time Complexity: O(m * n^(2k))

    Approach:
        - Find all profitable pairs for each stock
        - Sort pairs by profit
        - Select up to k pairs with no overlapping days
    
    Assume:
        - A[i][j] gives the price of stock i on day j
        - Returns up to k transactions
        - No overlapping days between transactions
    """
    m, n = len(A), len(A[0])
    transactions = []

    # Collect all profitable transactions
    all_profits = []
    # Iterate through all stocks
    for i in range(m):
        for buy in range(n):
            for sell in range(buy + 1, n):
                # Calculate profit
                profit = A[i][sell] - A[i][buy]
                if profit > 0:
                    all_profits.append((profit, i, buy, sell))

    # Sort by descending profit
    all_profits.sort(reverse=True)
    # Set instead of List for better time complexity in checking used days
    used_days = set()
    count = 0
    for profit, i, buy, sell in all_profits:
        # Makes sure no days overlap with previous transactions
        if all(day not in used_days for day in range(buy, sell + 1)):
            # Convert to 1-based index and add to transactions
            transactions.append((i + 1, buy + 1, sell + 1))
            used_days.update(range(buy, sell + 1))
            count += 1
            if count == k:
                break

    if not transactions:
        return []
    else:
        return transactions

if __name__ == "__main__":
    A = [
        [7, 1, 5, 3, 6],
        [2, 9, 3, 7, 9],
        [5, 8, 9, 1, 6],
        [9, 3, 4, 8, 7]
    ]
    k = 3

    result = dp_problem2_n2k(A, k)
    print("Transactions:", result)