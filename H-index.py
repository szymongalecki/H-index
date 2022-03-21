def h_index(n, citations):
    h = 0
    papers = 0
    result = []
    counter = [0] * (n + 1)

    for c in citations:
        if c > h:
            if c > n:
                counter[n] += 1
            else:
                counter[c] += 1
            if papers == counter[h]:
                papers = 0
                h += 1
            else:
                papers += 1
        result.append(h)
    return " ".join([str(h) for h in result])


t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    citations = map(int, input().split())
    print(f"Case #{test_case}: {h_index(n, citations)}")
