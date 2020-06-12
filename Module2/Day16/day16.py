#A set should be used over a list only if there is no need for the collection to be ordered.
#The program is able to scan the contents of a set substantially faster than the contents of a list.

suspects = {"Verbal", "Keaton", "McManus", "Fenster"}
investigators = set(["Dave Kujan", "Jack Baer", "Jeff Rabin"])
print(suspects)
print(investigators)

# you can change a set
suspects.add("Hockney")
print(suspects)
# iterating through a set with a for loop
for person in suspects:
    print("{} was brought in for a line up.".format(person))
# combining with a union
numbers1 = set([1, 2, 3, 4, 5])
numbers2 = set([6, 7, 8, 9, 10])
print(numbers1.union(numbers2))
# intersection brings items that match between the two sets
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.intersection(evens))
# what is not in the same ( items that don't match)
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.difference(evens))
# useful for removing duplications (difference_update) changes dupplications and removes them from OG Set
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Evens: {}".format(nums))
print("Evens Difference Update: {}".format(nums.difference_update(evens)))
print("Evens: {}".format(nums))
# prints difference between two sets
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.symmetric_difference(evens))
# updates set with unique numbers
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Evens: {}".format(nums))
print("Symmetric Difference Update: {}".format(nums.symmetric_difference_update(evens)))
print("Evens: {}".format(nums))
# remember sets are unsorted -> so use sorted to order them
print(suspects)
print(sorted(suspects))
# remove and discard can delete items, only remoove will show an error message if it is not present
evens = set([0, 2, 4, 6, 8])
evens.discard(0)
evens.remove(2)
print(evens)
# example of error message
evens.discard(0)
evens.remove(2)
print(evens)
# frozen set "While sets are mutable, the frozenset()
# function can be used to create immutable sets.
# None of the update methods will execute on a frozenset()."
suspects = frozenset(["Verbal", "Keaton", "McManus", "Fenster"])
suspects.add("Kaiser Soze")
print(suspects)
# clear
print(nums)
nums.clear()
print(nums)
