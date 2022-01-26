#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------


print("The Munsters began airing on:", munsters.get("startDate"))

print("The last episode for Munster was on", munsters.get("endDate")) 
print("Characters on the Munsters include:", munsters.get("names"))


names = ['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']

# create a simple for loop
for x in names:   # if a line ends in a colon the next line WILL be indented
    print(x, "is a character on the Munsters")
    # print("---")  # print 3 dashes on the screen each time through the loop

# we don't have to use a simple list to loop
# we could access the nested list within the dictionary->   munsters.get('name')
print("\nDisplays the same data, but by accessing the nested list within our dict\n")
for x in munsters.get("names"):
    print(x, "is a character on the Munsters")

# Add to the munsters
munsters["episodes"] = 70
print(munsters)
