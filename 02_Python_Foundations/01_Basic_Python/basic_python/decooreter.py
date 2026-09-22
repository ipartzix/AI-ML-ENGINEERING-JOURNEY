#Decorater is a function that takes a function; it creates a new function inside its body(wrapper). then it returns the ew function
# You're learning about **decorators** in Python—a very powerful concept used in advanced Python programming. Let's break down your code line by line in a simple and professional way.
#
# ---
#
# ###  Concept: What is a Decorator?
#
# A **decorator** is a function that:
#
# 1. Takes another function as an input.
# 2. Adds some extra behavior to that function (before or after it runs).
# 3. Returns a new function that replaces the original one.
#
# ---
#
# ###  Your Code (with explanation)
#
# ```python
# # Step 1: Define a decorator function that takes another function as input
# def decorator(func):
#     def wrapper():  # Step 2: Define a new function inside (the wrapper)
#         print("this is the 1st line I execute start")  # Extra code before
#         func()  # Original function runs here
#         print("I want to see the line which time print")  # Extra code after
#     return wrapper  # Step 3: Return the new function (wrapper)
# ```
# At this point:
# * `decorator` is the outer function.
# * `wrapper` is the new function that will **wrap around** your original function to add extra functionality.
# ---
# ```python
# # Step 4: Your original function
# def say__hello():
#     print("HelloI!")
# ```
# * This is the original function you want to **decorate** (add extra behavior to).
# ---
# ```python
# # Step 5: Apply the decorator manually
# f = decorator(say__hello)
# f()
# ```
#
# * `decorator(say__hello)` means: pass the function `say__hello` to the decorator.
# * It returns the `wrapper` function.
# * `f()` now runs the `wrapper()` function, not the original directly.
#
# ---
#
# ###  Output When You Run This:
#
# ```
# this is the 1st line I execute start
# HelloI!
# I want to see the line which time prints
# ```
# This happens because:
# 1. First line from `wrapper()`
# 2. Then it calls `say__hello()` → prints "HelloI!"
# 3. Then last line from `wrapper()`
#
# ---
#
# ###  Optional: Using `@` Syntax (Cleaner Way)
#
# Instead of manually writing `f = decorator(say__hello)`, you can write:
#
# ```python
# @decorator
# def say__hello():
#     print("HelloI!")
#
# say__hello()  # Automatically applies the decorator
# ```
#
# This does the **same thing**, but is more Pythonic and easier to read.
#
# ---
# ###  Summary:
#
# | Part            | What it does                                            |
# | --------------- | ------------------------------------------------------- |
# | decorator(func) | Takes the original function                             |
# | wrapper()       | Adds extra behavior before/after original function runs |
# | return wrapper  | Replaces original function with enhanced version        |
# | f()             | Calls the enhanced version                              |
#


def decorator(func):# it is the function that teck another functon as an argument and return function
    def wrapper():
        print("this is the 1st line I execute start - decooreter.py:92")
        func()
        print("i want to see the line which time print - decooreter.py:94")
    return wrapper

def say__hello():
    print("HelloI! - decooreter.py:98")

f=decorator(say__hello)
f()
# @decorator

# for quick revtion go  on gate smasher viideo on this topic in youtube (6.34min)

