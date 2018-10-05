from typing import List


def is_subset_of(strings: List[str]) -> bool:
    """Challenge
    Write a function that satisfies the following rules:

        - Return true if the string in the first element of the list
          contains all of the letters of the string in the second
          element of the list.

    examples
    >>> is_subset_of(["hello", "Hello"])
    True

    because all of the letters in the second string are present in the first, ignoring case.

    >>> is_subset_of(["hello", "hey"])
    False

    because the string "hello" does not contain a "y".

    >>> is_subset_of(["Alien", "line"])
    True

    because all of the letters in "line" are present in "Alien"."""

    s1, s2 = list(map(str.casefold, strings))
    return (set(s2) - set(s1)) == set()
