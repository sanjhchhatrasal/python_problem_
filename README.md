---

## Problem Statement:

**Title**: Sort an Array by Frequency

**Description**:  
Given an array of integers, where some elements may be duplicated, the task is to sort the array based on the frequency of each element. The element with the highest frequency should appear first, followed by the element with the next highest frequency, and so on. If two elements have the same frequency, they should appear in the order they first appeared in the array.

**Example**:
- **Input**: 
  - `N = 8`
  - `array[] = {1, 2, 3, 2, 4, 3, 1, 2}`
- **Output**: 
  - `2 2 2 1 1 3 3 4`
- **Explanation**: 
  - The number `2` appears 3 times, so it is listed first. 
  - The number `1` appears 2 times and is listed next.
  - The number `3` also appears 2 times but after `1`, so it comes after `1` in the output.
  - The number `4` appears only once, so it appears last.

---

## Solution Explanation

### Step-by-Step Breakdown:

1. **Input Handling**:
   - The solution begins by reading the array of integers as input. The user enters the elements in a single line, separated by spaces. The input is then converted into a list of integers.

2. **Frequency Counting**:
   - A dictionary (`dict`) is used to count the frequency of each element in the array. The dictionary's keys are the array elements, and the values are the corresponding frequencies.
   - As we iterate through the array, we check if the element is already in the dictionary. If it is, we increment its frequency; otherwise, we add it to the dictionary with a frequency of 1.

3. **Sorting by Frequency**:
   - After building the frequency dictionary, we sort the dictionary by its values (frequencies) in descending order.
   - To achieve this, the `sorted` function is used with the `key` parameter set to `dict.get`, and `reverse=True` ensures the sort is in descending order of frequency.

4. **Building the Sorted Array**:
   - After sorting, we create a new list (`sortedArray`) where elements are added according to their frequency. For each element in the sorted keys, we extend the list by adding the element repeated according to its frequency.

5. **Output**:
   - Finally, the sorted array is printed as both a string and a list to show the result.

### Code Implementation:

```python
def frequencySorting():
    arr = list(map(int, input("Enter elements: ").split()))
    dict = {}
    for i in arr:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
    sortedArray = []
    for key in sorted(dict, key=dict.get, reverse=True):
        sortedArray.extend([key] * dict[key])
    print("sorted array is: ", " ".join(map(str, sortedArray)))
    print(sortedArray)
```

### Explanation of Key Functions:
- `map(int, input().split())`: Converts input into a list of integers.
- `dict.get`: Retrieves the value associated with a key in the dictionary.
- `sorted`: Sorts elements based on the frequency from the dictionary.

### Sample Run:
```text
Enter elements: 1 2 3 2 4 3 1 2
{1: 2, 2: 3, 3: 2, 4: 1}
sorted array is:  2 2 2 1 1 3 3 4
[2, 2, 2, 1, 1, 3, 3, 4]
```

---
