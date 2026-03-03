# 72-Permutations

A comprehensive Python implementation for generating all permutations of a list or string using recursion and backtracking techniques.

## 📋 Overview

This repository contains a complete educational resource for understanding and implementing permutation generation algorithms. It includes both practical code implementation and theoretical explanations to help you master this fundamental algorithmic technique.

## 🎯 Features

- **Efficient Permutation Generation**: Uses swap-based recursion and backtracking
- **Universal Input Support**: Works with both lists and strings
- **Complete Documentation**: Includes detailed PDF lecture with:
  - Step-by-step algorithmic logic
  - Swap-based approach explanation
  - Backtracking technique breakdown
  - Time and space complexity analysis
  - Code walkthrough with examples

## 🚀 Quick Start

### Prerequisites

- Python 3.x

### Installation

```bash
# Clone the repository
git clone https://github.com/zain-cs/72-Permutations.git

# Navigate to the project directory
cd 72-Permutations
```

### Usage

```python
# Run the permutation script
python "Permutations using Recursion and Backtracking.py"
```

## 📖 Files in This Repository

| File | Description |
|------|-------------|
| `Permutations using Recursion and Backtracking.py` | Python implementation of the permutation algorithm |
| `Permutations using Recursion and Backtracking.pdf` | Comprehensive lecture explaining the concept, logic, and complexity |

## 🔍 Algorithm Explanation

The implementation uses a **swap-based recursive backtracking** approach:

1. **Base Case**: When the current index reaches the end, add the permutation to results
2. **Recursive Case**: For each position, swap elements and recursively generate permutations
3. **Backtracking**: Undo the swap to restore the original state before the next iteration

### Time Complexity
- **O(n!)** - where n is the number of elements
- Generates n! permutations for n distinct elements

### Space Complexity
- **O(n)** - recursion stack depth
- Additional O(n!) for storing all permutations

## 💡 Example

```python
# Input: [1, 2, 3]
# Output: 
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], 
#  [2, 3, 1], [3, 2, 1], [3, 1, 2]]

# Input: "abc"
# Output:
# ["abc", "acb", "bac", "bca", "cab", "cba"]
```

## 🎓 Learning Objectives

By studying this repository, you will:

- Understand the fundamentals of recursive algorithms
- Master the backtracking technique
- Learn swap-based permutation generation
- Analyze time and space complexity
- Apply these concepts to solve permutation problems

## 📚 Additional Resources

For a deeper understanding:
- Review the included PDF lecture for detailed explanations
- Study the code comments for implementation insights
- Experiment with different inputs to observe behavior

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest enhancements
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Zain**
- GitHub: [@zain-cs](https://github.com/zain-cs)

## 🌟 Show Your Support

If you find this project helpful, please give it a ⭐️!

---

**Perfect for**: Students learning algorithms, interview preparation, computer science educators, and anyone looking to master permutation generation techniques.
