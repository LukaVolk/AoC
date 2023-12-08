from concurrent.futures import ProcessPoolExecutor, as_completed

def process_iteration(stevec, groups, all_ranges):
    num = stevec

    for group in groups[:-1]:
        group = group.splitlines()[1:]
        for line in group:
            count, start, length = map(int, line.split())
            if num >= count and num <= count + length:
                num = num - count + start
                break
        a = 0

    print(f"{stevec} / {num}")

    if preveri_parallel(num, all_ranges):
        return stevec
    return None

def preveri_single(num, a):
    return num >= a[0] and num <= a[1]

def preveri_parallel(num, all_ranges):
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(preveri_single, num, a) for a in all_ranges]
        results = [future.result() for future in as_completed(futures)]

    return any(results)

def main():
    groups = open("input.txt").read().split("\n\n")
    _, seeds_str = groups[0].split(": ")
    seeds = [int(i) for i in seeds_str.split()]

    all_ranges = []
    for i in range(0, len(seeds), 2):
        all_ranges.append((seeds[i], seeds[i + 1] + seeds[i] - 1))

    rez = float('inf')
    groups = groups[::-1]
    stevec = 0

    while True:
        with ProcessPoolExecutor() as executor:
            futures = {executor.submit(process_iteration, stevec + i, groups, all_ranges): stevec + i for i in range(10)}

            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    print(f"Result: {result}")
                    return

        stevec += 10

    print(rez)

if __name__ == "__main__":
    main()
