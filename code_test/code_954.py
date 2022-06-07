def profit_amount(actual_cost,sale_amount): 
 """
 Write a function that gives profit amount if the given amount has profit else return none.
 """
 if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    return amount
 else:
    return None
