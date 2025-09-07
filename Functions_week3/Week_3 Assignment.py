#Question 1
#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    #check if discount is 20% or higher
    if discount_percent >=20:
        #Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        #Calculate the final price after discount
        final_price = price - discount_amount
        return final_price
    else:
        #If discount is less than 20% return the original price
        return price

print(calculate_discount(1000, 10)) 