from typing import List, SupportsComplex, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    high, ans = float("-inf"), ""
    for name,score in scores:
        if score > high:
            high = score
            ans = name
    return ans


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
