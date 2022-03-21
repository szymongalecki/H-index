"""
Definition:
H-index score of a researcher is the largest integer H, 
such that the researcher has H papers with at least H citations each

Limitation: 
Researcher can't have bigger H-index than the number of papers

Variables:
1. 'h' stores current H-index value
2. 'papers' if necessary, stores number of papers needed to increment the H-index
3. 'result' holds consecutive H-index values
4. 'counter' stores number of papers that have the same number of citations, counter[citations] = number of papers 

To determine H-index of a researcher after every new paper, do the following:
1. loop through every paper
2. only care for papers with number of citations bigger than current H-index
3. add paper to the counter
4. check number of papers that constitute to the current H-index, counter[h]
5. H-index is incremented if researcher has h+1 papers with more than h citations
6. append H-index value to the results list
"""


def h_index(n, citations):
    h = 0
    papers = 0
    result = []
    counter = [0] * (n + 1)

    # 1. loop through every paper
    for c in citations:
        # 2. only care for papers with number of citations bigger than current H-index
        if c > h:
            # 3. add paper to the counter
            if c > n:
                counter[n] += 1
            else:
                counter[c] += 1
            # 4. check number of papers that constitute to the current H-index, counter[h]
            if papers == counter[h]:
                # 5. H-index is incremented if researcher has h+1 papers with more than h citations
                papers = 0
                h += 1
            else:
                papers += 1
        # 6. append H-index value to the results list
        result.append(h)
    return " ".join([str(h) for h in result])


t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    citations = map(int, input().split())
    print(f"Case #{test_case}: {h_index(n, citations)}")
