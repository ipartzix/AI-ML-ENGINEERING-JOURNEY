f = open("mew.txt", "r")
content = f.read()
print(content)
for line in f:
    print(line)
f.close()

# forn reed line by line
# for line in f:
#     print(line)


# other method
# # f = open("harry.txt", "r")
# content = f.read()
# print(content)
# f.close()

with open("harry.txt", "r") as f:  # context manager
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with synax
