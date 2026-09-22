# 🧠 Core Python – Deep Understanding Notebook

---

# 1️⃣ Python Foundations (Mental Model First)

## 🔹 How Python Works Internally
- Source Code → Bytecode → Python Virtual Machine (PVM)
- Interpreted but compiled to bytecode first
- Dynamically typed but strongly typed
- Everything in Python is an object

### Task
- Explain in your own words how Python executes a `.py` file.

---

# 2️⃣ Variables & Memory Model

## 🔹 Object Model
- Variables are references, not containers
- `id()` → memory identity
- `type()` → object type
- Immutable vs Mutable

### Concepts to Master
- Integer caching
- String interning
- Reference counting
- Garbage collection

### Practice
```python
a = 10
b = 10
print(id(a), id(b))
```
Explain why IDs are same.

---

# 3️⃣ Data Types (Deep Level)

## 🔹 Numbers
- int (arbitrary precision)
- float (IEEE 754)
- complex

## 🔹 Strings
- Immutable
- Slicing creates new object
- Interning concept

## 🔹 Lists
- Dynamic arrays
- Over-allocation strategy
- Amortized O(1) append

## 🔹 Tuples
- Immutable
- Faster than list (why?)

## 🔹 Sets
- Hash-based
- No duplicates

## 🔹 Dictionaries
- Hash table implementation
- O(1) average lookup
- Collision handling

### Task
Compare list vs tuple vs set vs dict in terms of:
- Mutability
- Internal structure
- Time complexity

---

# 4️⃣ Control Flow (With Precision)

- if / elif / else
- match-case (Python 3.10+)
- for vs while
- break / continue / pass

### Advanced
- for-else meaning
- while-else meaning

---

# 5️⃣ Functions (Core Depth)

## 🔹 Function Objects
- First-class citizens
- Stored in variables

## 🔹 Parameters
- Positional
- Keyword
- Default
- *args
- **kwargs

## 🔹 Important Concepts
- Recursion
- Lambda
- Closures
- LEGB rule
- Decorators (basics)

### Practice
Write:
- A recursive factorial
- A closure example
- A simple decorator

---

# 6️⃣ OOP in Python (Serious Understanding)

## 🔹 Class Structure
- __init__
- self
- Instance vs class variables

## 🔹 Pillars
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

## 🔹 Advanced
- Dunder methods
- __str__ vs __repr__
- Method Resolution Order (MRO)
- Multiple inheritance

### Task
Create:
- Base class Animal
- Child class Dog
- Override method

---

# 7️⃣ Error Handling

- try
- except
- else
- finally
- raise
- Custom exceptions

---

# 8️⃣ File Handling

- Read / Write
- with statement
- Text vs Binary

---

# 9️⃣ Modules & Packages

- import styles
- __name__ == "__main__"
- Virtual environments (concept)

---

# 🔟 Iterators & Generators (Critical for ML Engineers)

## 🔹 Iterables vs Iterators
- __iter__
- __next__

## 🔹 Generators
- yield
- Generator expressions
- Memory efficiency

---

# 1️⃣1️⃣ Comprehensions & Advanced Pythonic Patterns

- List comprehension
- Dict comprehension
- Set comprehension
- Nested comprehensions

---

# 1️⃣2️⃣ Time & Space Complexity in Python Context

Know complexity of:
- list append
- list insert
- dict lookup
- set operations
- slicing

---

# 1️⃣3️⃣ Python Internals (Advanced Depth)

- Mutable default argument issue
- Shallow vs Deep copy
- is vs ==
- GIL (conceptual understanding)

---

# 1️⃣4️⃣ Mini Projects for Mastery

1. Build your own:
   - Stack class
   - Queue class
2. Implement:
   - LRU Cache (basic)
3. Build a:
   - CLI-based To-Do app

---

# 📌 Final Mastery Checklist

You understand Python deeply if you can explain:

- Why lists are mutable but strings are not
- How dictionary hashing works
- What happens when function is called
- How memory is managed
- Why Python is slower than C

---

# 🚀 Study Strategy

Daily:
- 1 concept
- 5 coding problems
- 1 internal explanation in notebook

Weekly:
- Build 1 small project

---

This notebook is structured for deep conceptual clarity — not surface-level syntax memorization.

