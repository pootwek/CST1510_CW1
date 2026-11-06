# week 7 cheat sheet

## 1. case and spaces

- text comparisons care about capital letters, so `"SRV-01" == "srv-01"` is `False`. use `.lower()` on both sides if you want to compare them without case getting in the way.
- `.lower()` makes every letter lowercase: `"HELLO".lower()` gives `hello`. `.upper()` makes every letter uppercase: `"hello".upper()` gives `HELLO`.
- `.title()` makes each word start with a capital: `"record check".title()` gives `Record Check`.
- these methods make a new string; they don’t change the original one. save the result if you want to keep it, like `clean_name = name.lower()`.
- `.strip()` removes spaces from both ends, `.lstrip()` removes them from the left, and `.rstrip()` removes them from the right. they leave spaces in the middle alone.
- you can chain methods: `"  SRV-01  ".strip().lower()` removes the outside spaces, then makes the text lowercase, giving `srv-01`.

## 2. finding and changing text

- `"error" in line.lower()` checks if the word is there, without case getting in the way. it gives `True` or `False`.
- `line.find("disk")` gives the position where `disk` starts. if it cannot find it, it gives `-1`.
- `.replace("_", "-")` swaps every underscore for a dash.
- `.startswith("ERROR")` and `.endswith(".log")` check the beginning or end. `.count("ERROR")` counts how many times it appears.

## 3. splitting and building a line

- `.split()` with no separator handles uneven spaces: `"a   b".split()` gives `["a", "b"]`.
- `.split(",")` splits at every comma. `.split(",", 1)` only splits at the first comma. that `1` is the max number of splits.
- `" | ".join(parts)` puts the strings in a list together with ` | ` between them. the items need to be strings first.
- an f-string puts values into text, like `f"{name}: {used}/{total}"`. use `:.1f` to show one decimal place.

## 4. cleaning and parsing records

- for a messy line: strip it, split it into pieces, clean the pieces, convert number text, then put the values into a dict.
- `piece.split("=", 1)` splits only at the first equals sign, so another `=` stays in the value.
- `ValueError: too many values to unpack` means the split made more pieces than the variables can hold. use a max split if only the first separator matters.
- `ValueError: could not convert string to float` means the value was not written as a number. check and clean the text before converting it.
