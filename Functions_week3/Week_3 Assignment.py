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

#Question2
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
#Prompt the user to enter the original price
#We use the input() function to take input from the user and convert it to a float using float() function
price = float(input("Enter the original price of the item: "))
#Promt the user to enter the discount percentage
discount_percent = float(input("Enter the discount percentage: "))
#Call the calculate_discount funtion to get the final price
final_price = calculate_discount(price, discount_percent)
#Print the final price
print(f"The final price after applying the discount is: {final_price:.2f}")
