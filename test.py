item_name = "Paneer Tikka Wrap"
quantity =3
unit_price = 149.0
is_first_order = True
# Subtotal
subtotal = quantity*unit_price
# Discount Tier
if subtotal >= 500:
  tier = "Gold"
  discount_rate = 0.15
elif subtotal >= 300:
  tier = "Silver"
  discount_rate = 0.10
else:
  tier = "Bronze"
  discount_rate = 0.05

  # first _order bonus
  if is_first_order and subtotal >= 300:
    discount_rate = discount_rate + 0.05
  # Delivery Fee
  if subtotal >= 300:
    delivery_fee = 0.0
  else:
    delivery_fee = 40.0
  #Final bill
  discount_amount = subtotal * discount_rate
  final_total = subtotal - discount_amount + delivery_fee
  print("item:",item_name)
  print("quantity:",quantity)
  print("unit price:",unit_price)
  print("subtotal:",subtotal)
  print("discount rate:",discount_rate)
  print("delivery fee:",delivery_fee)
  print("final total:",round(final_total,2))