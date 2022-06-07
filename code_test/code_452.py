def loss_amount(actual_cost,sale_amount): 
  """
  Write a function that gives loss amount if the given amount has loss else return none.
  """
  if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    return amount
  else:
    return None
