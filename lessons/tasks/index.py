# zadacha counting valleys
# sample inputs
steps = 100
path = "DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD" #i

#our veriables
count = 0
dolina = 0

for x in path:
    if x == "U":
        count += 1
        if count == 0:
            dolina += 1
    if x == "D":
        count -= 1

print("Ответ: путник прошел", dolina, 'долины')
