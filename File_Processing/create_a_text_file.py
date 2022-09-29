# Creating a text file using python program

with open("swigy_order_details.text", "w") as order_details:
    # Writing the details on the text file
    order_details.write("2 Large Pizzas from Domino's \n")
    order_details.write("2 Maharaja Burgers from McDonald's")

