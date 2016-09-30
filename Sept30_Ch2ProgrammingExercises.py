
#1
Name = raw_input("Please enter your first and last name: ")
Address = raw_input("Please enter your address, including address, city, state and ZIP: ")
Telephone = raw_input("Please enter your telephone number: ")
Major = raw_input("What is your college major? ")
print Name,Address,Telephone,Major

#2. Sale Prediction
sales = input("What is your total sales?: ")
profit = sales*0.23
print format(profit, '.2f')

#3. Land Calculation
sqft = input("Please enter the total area of the tract of land in feet squared: ")
acres = sqft/43560
print format(acres, '.2f')

#4. Total Purchase
item1 = input("Please enter the price of item 1: ")
item2 = input("Please enter the price of item 2: ")
item3 = input("Please enter the price of item 3: ")
item4 = input("Please enter the price of item 4: ")
item5 = input("Please enter the price of item 5: ")
subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * 0.07
total = subtotal + tax
print"Subtotal: ", subtotal
print "Tax: ", tax
print "Total: ", total

#5. Distance Traveled
speed = 70
time = input("How long is the car traveling?: ")
distance = time * speed
print distance

#6. Sales Tax
purchase = input("Please enter the purchase price: ")

st_tax = purchase * 0.05
co_tax = purchase * 0.025
total = purchase + st_tax + co_tax
print"Subtotal: ", purchase
print "State Tax: ", st_tax
print "County Tax: ", co_tax
print "Total Sales Tax: ", st_tax+co_tax
print "Total: ", total

#7. Miles Per Gallon
miles = input("How many miles have you driven? ")
gallons = input("How many gallons of gas have you used? ")
mpg = miles/gallons
print "You MPG is: ", mpg

#8. Tip, Tax & Total
purchase = input("Please enter the cost of your meal: ")

tip = purchase * 0.18
tax = purchase * 0.07

print"Subtotal: $", format(purchase, '.2f')
print "Tip: $", format(tip, '.2f')
print "Tax: $", format(tax, '.2f')

#9. Celcius to Farenheit Temperature Converter
cel = input("Please enter the temperature in degrees Celcius: ")
far = (9/5) * cel + 32
print far, "degrees"

#10. Ingredient Adjuster
cookies = input("How many cookies would you like to make? ")
sugar = (1.5/48)*cookies
butter = (1.0/48)*cookies
flour = (2.75/48)*cookies
print "You will need: "
print sugar, "cups of sugar"
print butter,"cups of butter"
print flour, "cups of flour"

#11. Male and Female Percentages
males = input("How many males are in the classroom? ")
females = input("How many females are in the classroom? ")
total = float(males) + float(females)
per_male = males/total
per_female = females/total
print format(per_male, '.00%'),"of the class are males."
print format(per_female, '.0%'), "of the class are females."

#12. Stock Transaction Program
stock_price = 2000 * 40
com1 = stock_price * 0.03
sale_price = 2000 * 42.75
com2 = sale_price * 0.03
profit = sale_price - stock_price - com1 - com2
print "$",format(profit, ".2f")
