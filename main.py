#######################
#### Assignment #1 ####
#######################

# Part 1 (5 points)
# DONE: Write an equation that uses multiplication, division, an exponent,
# addition, and subtraction that is equal to 1902.
v = int(1000 + 2**3 * (1000 / 10) + 200 - 49 * 2)

# Part 2 (5 points)
list_of_numbers = [2, 4, 6, 8]

# DONE: Using a for loop, create an identical list to the list above.
identical_list_for = []
for number in list_of_numbers:
    identical_list_for.append(number)

# DONE: now using a while loop, create an identical list to the list above, but
# employ a break statement to exit the loop.
identical_list_while = []
while True:
    if len(identical_list_while) == len(list_of_numbers):
        break
    identical_list_while.append(list_of_numbers[len(identical_list_while)])

# DONE: Do the same thing except with a list comprehension. (HINT: You can use
# the range() function)
identical_list_while = list(range(2, 10, 2))


# Part 3 (5 points)
def fahrenheit_to_celsius(fahrenheit):
    result = fahrenheit

    # DONE: convert the FLOAT fahrenheit to INTEGER celsius (round down)
    result = int((fahrenheit - 32) * 5 / 9)

    return result


# Part 4 (5 points)
string_to_change = "Alice and Bob are super cool people."

# DONE: Define x to be the index of the first occurrence of the letter 'a' in
# the string above.
x = string_to_change.index("a")

# DONE: Define y to be the last 5 characters of the string above.
y = string_to_change[-5:]

# DONE: Define z to be the same string as `string_to_change` but with all the
# spaces removed. (must be done in one line)
z = string_to_change.replace(" ", "")

# DONE: Define k to be the same string as `string_to_change` but with the first
# and last words removed. (must be done in one line)
k = " ".join(string_to_change.split()[1:-1])


# Part 5 (5 points)
def is_prime(n):
    # n is bounded between 1 and 2000
    if n < 1 or n > 2000:
        return False

    # DONE: Determine if n is a prime number. Return True if it is, False if it
    # is not.
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Part 6 (5 points)
def is_palindrome(s):
    # DONE: in one line, determine if the string s is a palindrome. Return True
    # if it is, False if it is not.
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


# Part 7 (5 points)
def sum_of_all_values_in_list(list_of_values):
    result = 0
    # DONE: return the sum of all the values in the list_of_values
    for value in list_of_values:
        result += value

    return result


# Part 8 (5 points)
def all_letters_are_unique(s):
    # DONE: return whether or not all the letters in the string s are unique
    # (case-insensitive). must be done in one line.
    # HINT: use the set() function
    return len(set(s.lower())) == len(s)


# Part 9 (5 points)
def remove_duplicates(s):
    # DONE: similar to the above function, but now we want to return a string
    #  with all the duplicate letters removed. must be done in one line.
    # HINT: use the set() function
    return "".join(set(s))


# Part 10 (5 points)
def sort_list_of_list_of_integers(list_of_list_of_integers):
    # DONE: each item in the list is a list of integers. sort each item by the
    # integer values in ascending order
    # HINT: use the sort() method
    for list_of_integers in list_of_list_of_integers:
        list_of_integers.sort()

    # DONE: in addition, sort the list of lists based off of the first integer
    # in each list. empty list is considered the smallest.
    # HINT: how does the sort() method when sorting a list of lists?
    list_of_integers.sort()


# Part 11 (5 points)
def list_to_counter(list_of_values):
    # DONE: create a dictionary that counts the number of times each value appears
    # in the list_of_values
    # You cannot use the "Counter" class from the "collections" module...
    res = dict()
    for value in list_of_values:
        res[value] = res.get(value, 0) + 1
        # could also do the below:
        # if value in res:
        #     res[value] += 1
        # else:
        #     res[value] = 1
    return res


# Part 12 (5 points)
def sort_list_of_tuples_of_integers(list_of_tuples_of_integers):
    # DONE: same thing as Part 10 but with tuples instead of lists
    # HINT: tuples are immutable, so you can't use the sort() method, but what
    # if you casted stuff?
    for i in range(len(list_of_tuples_of_integers)):
        list_of_tuples_of_integers[i] = tuple(sorted(list_of_tuples_of_integers[i]))

    list_of_tuples_of_integers.sort()


# Part 13 (5 points)
def add_up_lists_together(list_of_list_of_ints):
    # DONE: add up all the lists together into one list
    res = []
    for list_of_ints in list_of_list_of_ints:
        res += list_of_ints

    # DONE: then sort the list in descending order
    # HINT: look at the sort() method documentation
    res.sort(reverse=True)
    return res


# Part 14 (5 points)
def does_each_list_have_a_duplicate(list_of_list_of_ints):
    # DONE: return whether or not each list in the list of lists has a
    # duplicate value
    # HINT: use the set() function
    # return should be a list of booleans with the same length as the list of
    # lists
    res = []
    for list_of_ints in list_of_list_of_ints:
        res.append(len(list_of_ints) != len(set(list_of_ints)))
    return res


# Part 15 (5 points)
def create_a_grid(width, height):
    # DONE: create a grid of width x height with each cell being a tuple of
    # (x, y)
    # where x is the column and y is the row
    # must be done in one line
    return [(x, y) for x in range(width) for y in range(height)]


# Part 16 (5 points)
def is_this_tuple_of_three_integers_increasing(t):
    # DONE: return whether or not the tuple of three integers is increasing
    return t[0] < t[1] < t[2]


# Part 17 (5 points)
def map_dictionary_to_list_of_tuples(d):
    # DONE: map the dictionary to a list of tuples where each tuple is
    # (key, value)
    return d.items()


# Part 18 (5 points)
def change_dictionary_keys_to_uppercase(d):
    # DONE: change the keys of the dictionary to uppercase
    # do not need to modify the original dictionary, can return a new one
    res = dict()
    for key, value in d.items():
        res[key.upper()] = value
    return res


# Part 19 (5 points)
def implement_binary_search(sorted_list, value):
    # DONE: implement the binary search algorithm to find the index of the
    # value in the sorted list
    # return -1 if the value is not in the list
    l = 0
    r = len(sorted_list) - 1
    while l <= r:
        mid = (l + r) // 2
        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] < value:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# Part 20 (5 points)
def generator_of_all_positive_even_numbers():
    # DONE: create a generator that yields all positive even numbers
    # yes, this is an infinite generator
    curr = 2
    while True:
        yield curr
        curr += 2


# Part 21 (5 points)
def generator_of_all_fibonacci_numbers():
    # DONE: create a generator that yields all fibonacci numbers
    fst = 1
    snd = 1
    while True:
        yield fst
        fst, snd = snd, fst
        snd = fst + snd


# Part 22 (5 points)
def divide_every_element_in_list_by_its_neighbor(list_of_ints):
    # DONE: divide element at index i by element at index i+1 for all elements
    # in the list
    # the last element should be divided by the first element
    # return the list of results
    # be careful of division by zero errors
    res = []
    for i in range(len(list_of_ints)):
        if list_of_ints[(i + 1) % len(list_of_ints)] == 0:
            res.append(float("inf"))
        else:
            res.append(list_of_ints[i] / list_of_ints[(i + 1) % len(list_of_ints)])
    return res
