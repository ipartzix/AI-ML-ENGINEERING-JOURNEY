# ============================================
# 📘 Object-Oriented Programming in Python
# ============================================

# 🔹 What is OOP?
# OOP is a programming paradigm based on the concept of "objects"
# Objects bundle data (attributes) and functions (methods)
# Python supports full OOP features

# --------------------------------------------
# 🔹 1. Class
# A class is a blueprint/template to create objects

# Syntax:
# class ClassName:
#     # attributes and methods

# --------------------------------------------
# 🔹 2. Object
# An object is an instance of a class

# Syntax:
# obj = ClassName()

# --------------------------------------------
# 🔹 3. Encapsulation
# Binding data and methods together and hiding internal details
# Achieved using private ( __var ) and public variables

# Example:
# class Account:
#     def __init__(self, balance):
#         self.__balance = balance  # private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# --------------------------------------------
# 🔹 4. Inheritance
# Allows one class to inherit properties and methods from another class
# Promotes code reusability

# Example:
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# --------------------------------------------
# 🔹 5. Polymorphism
# Same function name behaves differently for different classes

# Example:
# class Bird:
#     def sound(self):
#         print("Chirp")

# class Cat:
#     def sound(self):
#         print("Meow")

# def make_sound(animal):
#     animal.sound()

# make_sound(Bird())
# make_sound(Cat())

# --------------------------------------------
# 🔹 6. Abstraction
# Hides complex implementation details and shows only essential features
# Implemented using abstract classes (abc module)

# Example:
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car started")

# --------------------------------------------
# 🔹 Access Modifiers in Python

# Public:     self.name         → Accessible everywhere
# Protected:  self._name        → Conventionally for internal use
# Private:    self.__name       → Not directly accessible from outside

# --------------------------------------------
# 🔹 Real-Life Analogy

# Class         → Blueprint of a phone
# Object        → A specific phone built using that blueprint
# Encapsulation → Phone's internal chip hidden under case
# Inheritance   → Smartphone inherits features of Phone
# Polymorphism  → Same "charge()" works for Phone and Laptop
# Abstraction   → You use a phone without knowing its circuit

# --------------------------------------------
# 🔹 Advantages of OOP

# ✔️ Modularity – Each class is self-contained
# ✔️ Reusability – Use classes in multiple programs
# ✔️ Security – Sensitive data is hidden
# ✔️ Maintainability – Easy to update and fix

# --------------------------------------------
# 🔹 Basic Example

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, I am {self.name}")

# p1 = Person("Partha", 21)
# p1.greet()

# ============================================
# ✅ End of OOPs Theory in Python
# ============================================
