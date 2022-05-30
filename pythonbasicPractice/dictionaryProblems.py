# what is the output of the following program?
synonyms = {"mountain": "peak", "forest": "jungle"}
print("1.", synonyms["mountain"])
synonyms["terrain"] = "land"
print("2.", synonyms)
synonyms.pop("forest")
print("3.", synonyms)
print("4.", synonyms.get("mountain"))
synonyms.update({"Sea": "water"})
print("5.", synonyms)
x = ("one", "two", "three")
y = "count", "numbers"
xy = dict.fromkeys(x, y)  # dict.format(keys,value)..So basically it returns multiple keys with same value
print("6.", xy)
print("7.", synonyms.popitem())  # so popitem() remove the item which was last inserted.
# The setdefault() method returns the value of a key (if the key is in dictionary).
# If not, it inserts key with a value to the dictionary.
sea = synonyms.setdefault("sea")
print("forest =", sea)  # if a key is present, and it has value or None then applying setdefault by giving
forest = synonyms.setdefault("forest", "jungle")  # default value will not change the Previous value
print("forest =", forest)

