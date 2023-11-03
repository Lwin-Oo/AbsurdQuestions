imported_blocks = []

with open('data.txt', 'r') as file:
    for line in file:
        block_dict = eval(line)
        imported_blocks.append(block_dict)

for block in imported_blocks:
    gym_present = block['gym']
    school_present = block['school']
    store_present = block['store'] 

    if gym_present:
        print("Yayy I found a gym :)")
    else:
        print("Oh no, I failed to find a gym :(") 

    if school_present:
        print("Yayy I found a school :)")
    else:
        print("Oh no, I failed to find a school :(")

    if store_present:
        print("Yayy I found a store :)")
    else:
        print("Oh no, I failed to find a store :(") 

    print("-" * 30) 
#Will continue later.....
