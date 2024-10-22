def min_breaks(n, m, memo):
    # Проверяем кэш
    key = (n, m)
    if key in memo:
        return memo[key]

    if n == 1 and m == 1:
        return 0
    if n == 1:
        return m - 1
    if m == 1:
        return n - 1

    
    min_cuts = n * m  

    # Разломы по горизонтали
    for i in range(1, n):
        cuts = min_breaks(i, m, memo) + min_breaks(n - i, m, memo) + 1
        if cuts < min_cuts:
            min_cuts = cuts

    # Разломы по вертикали
    for j in range(1, m):
        cuts = min_breaks(n, j, memo) + min_breaks(n, m - j, memo) + 1
        if cuts < min_cuts:
            min_cuts = cuts

    memo[key] = min_cuts

    return min_cuts

def main():
    n = 2
    m = 3

    memo = {}
    
    result = min_breaks(n, m, memo)

    print(f"Минимальное количество разломов: {result}")

if __name__ == "__main__":
    main()