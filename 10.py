#10 Write a program that will take user input of cost price
# and selling price and determines whether its a loss or a profit

cost_price=int(input("Enter Cost Price"))
selling_price=int(input("Enter selling price"))
loss=cost_price-selling_price
profit=selling_price-cost_price
if cost_price>selling_price:
    print(" You are in the loss,",loss,"rs")
elif cost_price==selling_price:
    print("No Lose , No Profit")
else:
    print("You are in profit,",profit,"rs")