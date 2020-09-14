def mean(arr):
    sum_of_the_set = sum(arr)
    return sum_of_the_set / len(arr)


def median(arr):
    n = len(arr)
    dummy = sorted(arr)
    if n & 1:
        return float(dummy[n // 2])
    else:
        return (dummy[n // 2] + dummy[(n // 2) - 1]) / 2.0


def mode(arr):
    dummy = sorted(arr)
    dictionary = {}
    for elem in dummy:
        if elem in dictionary:
            dictionary[elem] += 1
        else:
            dictionary[elem] = 1
    return max(dictionary, key=dictionary.get)


def weighted_mean(arr, weights):
    numerator = sum([x * w for (x, w) in zip(arr, weights)])
    return numerator / sum(weights)
