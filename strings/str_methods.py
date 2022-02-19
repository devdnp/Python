# len(length), lower(case), upper(case), title(1st capital), count(individual letter's number of repeating)
# lstrip(), rstrip(). strip(), replace(" ", "", n) --> space removers; n=which number of word we want to replace
# find("word", n) [gives starting position of the word, initiative position]
# .center(len(var)+4, "*") --> it'll add 4 *, 2-2 before after the strinng resp.
# strings are immutable: cannot be changed in original place, but new var can be formed to do so.
name, focus = input("enter your name and letter separated by comma: ").split(",")
print(f"length of your name is: {len(name)}")
print(f"letter count is: {name.lower().count(focus.lower())}")