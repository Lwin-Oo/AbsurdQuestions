Blocks = [

	{
	 "gym": False,
	 "school": True,
	 "store": False,
	},
	 
	{
	 "gym": True,
	 "school": False,
	 "store": True,
	},

	{
	 "gym": True,
	 "school": True,
	 "store": False,
	},

	{
	 "gym": False,
	 "school": True,
	 "store": False,
	},
	
	{
	 "gym": False,
	 "school": True,
	 "store": True,
	},

]

with open('data.txt', 'w') as file:
    for block in Blocks:
        file.write(str(block) + '\n')