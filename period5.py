resturants = ["In N out","Mcdonalds", "Chickfila", "Jack and the Box", "Taco bell"]

new_res = input("What restuant would you like to rank into your list?")

def rank_resturants(new_res, resturants):
    
    for i in range(len(resturants)):

        rank = input("do you like A)" + new_res + "more or B)" + resturants(i) + "more? A/B")

        if rank == "A":
            resturants.insert(i, new_res)
            break
        elif rank == "B":
            continue

    return resturants

print("Your new ranking of resturants is", rank_resturants(new_res, resturants))
