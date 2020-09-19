# %%
def mean(arr):
    return sum(arr) / len(arr)


# %%
def median(arr):
    dummy = sorted(arr)

    # n = len(arr)
    # if n & 1:
    #     return float(dummy[n // 2])
    # else:
    #     return (dummy[n // 2] + dummy[(n // 2) - 1]) / 2.0

    # mid, is_odd = divmod(len(arr), 2)
    # return dummy[mid] if is_odd else sum(dummy[mid - 1:mid + 1]) / 2

    mid = len(dummy) // 2
    return (dummy[mid] + dummy[~mid]) / 2


# %%
def mode(arr):
    dummy = sorted(arr)

    # dictionary = {}
    # for elem in dummy:
    #     if elem in dictionary:
    #         dictionary[elem] += 1
    #     else:
    #         dictionary[elem] = 1
    # return max(dictionary, key=dictionary.get)

    return max(dummy, key=arr.count)


# %%
'''
arr     = [10, 40, 30, 50, 20]
weights = [ 1,  2,  3,  4,  5]
'''


def weighted_mean(arr, weights):
    numerator = sum([x * w for (x, w) in zip(arr, weights)])
    return numerator / sum(weights)


# %%
_ = int(input())
arr = [int(x) for x in input().split()]


# %%
weights = list(map(int, input().split()))


# %%
print(f'{mean(arr):.1f}')


# %%
print(f'{median(arr):.1f}')


# %%
print(mode(arr))


# %%
print(f'{weighted_mean(arr, weights):.1f}')
