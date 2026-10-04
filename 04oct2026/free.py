order_amount = 850
has_permium_membership = True

if order_amount >= 1000 or has_permium_membership:
    delivery_charge = "free charge"
else:
    delivery_charge = "standard delivery fee applied"
  
print(f"result: {delivery_charge}")    