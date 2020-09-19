# %%
def say_hello(name):
    return f'Hello, {name}'


# %%
print(say_hello('Rahul'))


# %%
arr = [5, 1, 4, 2, 3]
for elem in arr:
    print(elem ** 2)

# %%
print(list(map(lambda x: x ** 2, arr)))
