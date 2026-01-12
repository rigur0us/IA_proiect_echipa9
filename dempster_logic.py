def dempster_rule(m1, m2):
    """
    Aplica regula de combinare Dempster–Shafer
    m1, m2 – dictionare de tip {frozenset: valoare}
    """
    result = {}
    conflict = 0.0

    for A, vA in m1.items():
        for B, vB in m2.items():
            intersection = A & B
            if not intersection:
                conflict += vA * vB
            else:
                result[frozenset(intersection)] = (
                    result.get(frozenset(intersection), 0) + vA * vB
                )

    if conflict == 1:
        raise ValueError("Conflict total intre surse")

    for key in result:
        result[key] /= (1 - conflict)

    return result
