"""List Practice

Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.

    For example::

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """
    #loop through items in the list
    for item in items:
        #print each item
        print item


def long_words(words):
    """Return words in input list that longer than 4 characters.

    For example::

        >>> long_words(["hello", "a", "b", "hi", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

    (If there are duplicates, show both --- notice "bacon" appears
    twice in output)

    If no words are longer than 4 characters, return an empty list::

        >>> long_words(["all", "are", "tiny"])
        []
    """
    #make an empty list
    longer_words = []
    #loop through the words in the input list
    for word in words:
        #if it has more than 4 letters add it to our longer_words list
        if len(word) > 4:
            longer_words.append(word)
    #return the list of 4+ char words
    return longer_words


def n_long_words(words, n):
    """Return words in list longer than `n` characters.

    For example::

        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "bacon", "bacon"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'bacon', 'bacon']

        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """
    #make an empty list
    long_n_words = []
    #loop through the words
    for word in words:
        #if the length of the word is greater than the submitted amount
        if len(word) > n:
            #add the word to the long_n_words list
            long_n_words.append(word)
    #return the list of long_n_words
    return long_n_words


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `min()`!

    For example::

        >>> smallest_int([-5, 2, -5, 7])
        -5

        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return `None`::

        >>> smallest_int([]) is None
        True
    """
    #sort the list to be in ascending order
    numbers.sort()
    #if no list is given, return None
    if len(numbers) == 0:
        return None
    #otherwise return the first number in the list
    return numbers[0]


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.

    **DO NOT USE** the built-in function `max()`!

    For example::

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None::

        >>> largest_int([]) is None
        True
    """
    #sort the list in descending order
    #looked up how to sort in reverse - https://docs.python.org/2/howto/sorting.html
    numbers.sort(reverse=True)
    #if no list provided - Return None
    if len(numbers) == 0:
        return None
    #otherwise return first number in the list
    return numbers[0]


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.

    For example::

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off
    the half::

        >>> halvesies([1, 5])
        [0.5, 2.5]
    """
    #make an empty list
    halved_numbers = []
    #loop through the numbers in the list
    for num in numbers:
        #divide the number in half - making sure to keep floats
        #could also write as halved_numbers.append(float(num * .5))
        #at least one num has to be a float in the equation to get a float answer
        #float(num/2) doesn't work bc it just makes the resulting int a float
        halved_numbers.append(float(num) / 2)

    return halved_numbers


def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    #make an empty list
    word_lengths = []
    #loop through the words in the list
    for word in words:
        #add their length to the list
        word_lengths.append(len(word))
    #return the list
    return word_lengths


def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.

    For example::

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero::

        >>> sum_numbers([])
        0
    """
    #start with a 0 value - if no numbers given, 0 will be returned
    list_total = 0
    #loop through the list of numbers
    for num in numbers:
        #add each number to the list_total
        list_total += num
    #return the total
    return list_total


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.

    For example::

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in input, the product is zero::

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::

        >>> mult_numbers([])
        1
    """
    #we start with a mult total of 1, bc a 0 would make everything 0
    mult_total = 1
    #loop through the numbers
    for num in numbers:
        #multiply each new number by the existing total
        mult_total = num * mult_total
    #return the total
    return mult_total


def join_strings(words):
    """Return a string of all input strings joined together.

    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.

    For example::

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string::

        >>> join_strings([])
        ''
    """
    #create an empty string
    all_strings = ""
    #loop through the words in the list
    for word in words:
        #add each word to the all_strings string
        all_strings = all_strings + word
    #return the final string
    return all_strings


def average(numbers):
    """Return the average (mean) of the list of numbers given.

    For example::

        >>> average([2, 4])
        3.0

    This should handle cases where the result isn't an integer::

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.

    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """
    #start with a base int of 0
    list_sum = 0
    #go through the numbers in the list
    for num in numbers:
        #add them to the list_sum value
        list_sum += num
    #return the average by dividing the total by the length of the list
    return (float(list_sum)/len(numbers))


def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".

    For example::

        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course::

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """
    #use join to take the list and add a comma and space between each item
    #forming a string
    end_list = ", ".join(words)
    #return the final string
    return end_list


def reverse_list(items):
    """Return the input list, reversed.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    You should do this without changing the original list::

        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """
    #create copy of the items list in reverse using list slicing
    #and stepping backwards
    items_list = items[::-1]
    #return the list
    return items_list


def reverse_list_in_place(items):
    """Reverse the input list `in place`.

    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.

    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.

    For example::

        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]

        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """
    #make a copy of the items list in reverse
    items_copy = items[::-1]
    #loop through the items_copy list using the index position
    for i in range(len(items_copy)):
        #rebind the items values to match the reversed list items_copy
        items[i] = items_copy[i]
    #QUESTION: seems like this would have a scope issue if the list lived outside the function?
    #I didn't think we could modify an external var from inside a function without returning it?
    #seems like it would have to be orig = reverse_list_in_place(orig) to work


def duplicates(items):
    """Return list of words from input list which were duplicates.

    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.

    For example::

        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']

        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]

    You should do this without changing the original list::

        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']

        >>> orig
        ['apple', 'apple', 'berry']
    """
    #get a version without the duplicates
    items_copy = set(items)
    #convert back to a list with only unique items
    items_copy = list(items_copy)
    #make an empty list
    dups_list = []
    #go through the items in the list
    for item in items:
        #if its in the list of unique items - remove it
        #we do this so we only add unique terms once
        if item in items_copy:
            items_copy.remove(item)
        #if it isn't in the unique items list and isn't in the dups_list
        #add to the dups_list
        elif item not in dups_list:
            dups_list.append(item)
    #sort them in ascending order
    dups_list.sort()
    #return the list of duplicates
    return dups_list


def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.

    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.

    **DO NOT** use the `list.index()` method.

    For example::

        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]

    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")

    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::

        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]

    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """
    #make a list to hold the indexes of the letters
    letter_positions = []
    #loop through each word
    for word in words:
        #make a var to increments
        index_position = 0
        #if the letter is in the word
        if letter in word:
            #loop through the letters
            for char in word:
                #if it isn't the letter we want increment up
                if char != letter:
                    index_position += 1
                #otherwise stop the loop
                else:
                    break
        #if it doesn't exist - set position to None
        else:
            index_position = None
        #add the position to the list
        letter_positions.append(index_position)
    #return the final list
    return letter_positions


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")
