from utils import mean, median, mode, weighted_mean

if __name__ == '__main__':
    _ = int(input())
    arr = [int(x) for x in input().split()]
    weights = list(map(int, input().split()))
    print(f'{mean(arr):.1f}')
    print(f'{weighted_mean(arr, weights):.1f}')
    print(f'{median(arr):.1f}')
    print(mode(arr))
