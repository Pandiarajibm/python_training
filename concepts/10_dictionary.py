"""
Dictionary:
        - We have option to store multiple values like list of employee names
        - We can keep DUPLICATE values
        - Here, MANUALLY we-have-to/we-can provide index to each value. Called KEY/VALUE pair
"""
print("Dictionary PART-1")
print("Store Values")
print("-"*20)
# ----------------

my_dictionary_1 = {0:10, 1:"python", 2:"online"}
# FOR KEYS: We can use any IMMUTABLE VALUE like int, float, string, tuple
# FOR VALUES: We can store any type of values
my_dictionary_2 = {
    "duration": 10,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1, end="\n\n")
print("my_dictionary_2:", my_dictionary_2, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Dictionary PART-2")
print("Access each value using index")
print("-"*20)
# ----------------

my_dictionary = {
    "duration": 10,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n")

print("Course:", my_dictionary["course"])
print("1st char in Course:", my_dictionary["course"][1], end="\n\n")

print("Mode:", my_dictionary["mode"])
print("1st Mode:", my_dictionary["mode"][0], end="\n\n")

print("Trainer:", my_dictionary["trainer"])
print("Trainer fname:", my_dictionary["trainer"]["fname"])
print("2nd char in Trainer fname:", my_dictionary["trainer"]["fname"][1], end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Dictionary PART-3")
print("METHODS present inside dict class")
print("-"*20)
# ----------------

print(dir(my_dictionary))
# OR
print(dir(dict))

print("#"*40, end="\n\n")
#########################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ----------------

my_dictionary = {
    "duration": 10,
    "course": "python",
}
print("my_dictionary:", my_dictionary, end="\n\n")

# ADD/UPDATE: Procedure is same
# 1-way
my_dictionary["mode"] = "offline"
# if key present then update else add new
print("my_dictionary after adding mode:", my_dictionary, end="\n\n")
# my_dictionary = { "duration": 10, "course": "python", "mode": "offline"}

# 2-way
another_dictionary = {"mode": "Online"}
my_dictionary.update(another_dictionary)
# if key present then update else add new
print("my_dictionary after updating mode:", my_dictionary, end="\n\n")
# my_dictionary = { "duration": 10, "course": "python", "mode": "Online"}

# REMOVE
my_dictionary.pop("duration")
print("my_dictionary after removing duration:", my_dictionary, end="\n\n")
# my_dictionary = { "course": "python", "mode": "Online"}

my_dictionary.popitem()
print("my_dictionary after removing last item:", my_dictionary, end="\n\n")
# my_dictionary = { "course": "python"}

print("#"*40, end="\n\n")
#########################