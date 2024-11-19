totals_list = []
rolls = [1,2,3]
for x in rolls:
    for y in rolls:
        for z in rolls:
            totals_list.append(x+y+z)
totals_list.sort()
print(totals_list)
