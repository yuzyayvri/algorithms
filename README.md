# Yuzy's Algorithms Collection v0.5.0
A collection of my algorithm implementations for learning and reference. Learned and written personally. This is sort of a journey showcasing my improvement in Python.
Also— these algorithms are libraries and are reusable.

Note: There is more information about the algorithms in their docstrings, so check that out if you want to learn more. This documentation only provides a brief and very oversimplified rundown!
## Implemented Algorithms

### Sorting
- **Bubble Sort** - An extremely basic algorithm. Sorts by comparing adjacent elements— though I personally don't recommend this.
- **Selection Sort** - A very simple sorting algorithm. Sorts by finding the minimum element and swaps it with the current one.
- **Merge Sort** - A simple divide-and-conquer sorting algorithm. Sorts by recursively splitting the list in half down to one element, then merges those sublists back together in sorted order.

### Searching
- **Linear Search** - A really, really simple searching algorithm. Searches by looping through an array and checking if the element matches the target.
- **Binary Search** - An efficient and easy searching algorithm. Searches by cutting the search space in the array in half until it finds the target.

## Usage
Import and use my algorithms directly:
```python
from merge_sort import merge_sort
result = merge_sort([4, 2, 1, 5, 3])
```
For more detailed information, there are docstrings included in each algorithm file.

## Coming Soon
- Depth-First Search
- Breadth-First Search
- Insertion Sort
- And many, many more!

*Python 3.11.9*
