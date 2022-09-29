
xfile = open('swigy_order_details.text')
for cheese in xfile:
    if cheese.startswith("2 Maharaja"):
        continue
    print(cheese)

print(len("A\nB"))
