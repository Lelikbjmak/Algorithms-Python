### Description

[Kata](https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python)

You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people
that like an item. It must return the display text as shown in the examples:

```python
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```

**Note**: For 4 or more names, the number in `"and 2 others"` simply increases.

### Solution

```python
@staticmethod
def likes(names):

    text = ""

    if len(names) == 0:
        text = "no one likes this"
    elif len(names) == 1:
        text = str(names[0]) + " likes this"
    elif 1 < len(names) < 4:
        for name in range(0, len(names) - 1):
            text = text + names[name] + ", "

        text = text[:-2]  # trim last ,
        text = text + " and " + str(names[len(names) - 1]) + " like this"
    else:
        for name in range(0, 2):
            text = text + names[name] + ", "
        text = text[:-2]
        text = text + " and " + str(len(names) - 2) + " others like this"

    return text
```

