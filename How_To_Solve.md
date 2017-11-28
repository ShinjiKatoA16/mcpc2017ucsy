# Explanation of each Problems

## Rehearsal Problem-A: Query Langueage Interpreter

This is a relatively easy problem. Save database information and scan that according to query.

If the data is small enough, it's OK to scan every database for each query. But it's better to search with **KEY** if database is big. In Python *Dictionary* is suitable for such purpose. In general, binary-search is fast method for fixed data, and hash list is flexible for data modification.


## Rehearsal Problem-B: Find A Word

1. Make a Dictionary, of which value is a List of coordinate for each alphabet. `'B': [(1,1), (2,7), (5,1)]`
1. For each query search the List in 8 direction

Instead of checking boundary, I added space before/after/top/bottom of the matrix.

```
def find_word(word, char_dict):
    ''' 
    Input: word, dictionary
    Output: None if not found
            List of coordinate of the word if word is found
    '''

    direction = ((1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1))

    first_char = word[0]
    if first_char not in char_dict:
        return None

    for row, col in char_dict[first_char]:
        for dir in direction:
            r_temp, c_temp = row, col
            pos_list = list()
            for c in word:
                if matrix[r_temp][c_temp] != c:
                    break
                pos_list.append((r_temp, c_temp))
                if len(pos_list) == len(word): # found the word
                    return pos_list
                r_temp += dir[0]
                c_temp += dir[1]

    return None
```

## Rehearsal Problem-C: Secret Chamber at Mount Rushmore

If there are pair of (a b), (a c), (b d), character 'a' can be tranlated to either 'a', 'b', 'c', 'd'. In order to handle this, translation table need to be extended repeatedly (without endless loop).
Again, dictionary is a good choice in Python for the translation table. Key: Character to be converted, Value: List of Distination Charater(s).
In case of the 1st sample input, there are 9 pair of characters. (c t), (i r), (k p), (o c), (r o), (t e), (t f), (u h), (w p).

Following Dictionary will be created:

- Key 'c': Value ['t', 'e', 'f']
- Key 't': Value ['e', 'f']
- Key 'i': Value ['r', 'o', 'c', 't', 'e', 'f']
- Key 'r': Value ['o', 'c', 't', 'e', 'f']
- Key 'o': Value ['c', 't', 'e', 'f']
- Key 'k': Value ['p']
- Key 'u': Value ['h']
- Key 'w': Value ['p']


## Rehearsal Problem-D: Ceiling Function

This is a typical binary-tree data. In binary tree, each node has 2 childs. After creating binary tree, count the number of shape.


## Rehearsal Problem-E: Stacking Plates

If there a **N** stacks originally, **N-1** movement is required at minimum.
Each *split* operation(**S**) create another stack. Total number of movement is
$ 2S+(N-1) $

If the boundary of each piece exists in original stack, it can be used, otherwise it needs to be counted as **S**.

1. Create final stack
1. Check each boundary if it does not exist in original stacks, increment number of *Split* 

**Reverse thinking** is important technique to solve some problems. Problem-J (Green Frog and Ordering) of ICPC 2016 is also this category.

