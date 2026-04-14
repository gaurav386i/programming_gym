def select_max_activity(activity: list[list[int]]) -> int:
    if not activity:
        return None
    activity.sort(key=lambda x: x[1])
    res = []
    res.append(activity[0][1])
    for start, end in activity:
        if res and res[-1] <= start:
            res.append(end)
        else:
            continue
    return len(res)


if __name__ == "__main__":
    activity = [(2, 3), (1, 4), (5, 8), (6, 10)]
    activity_1 = [(1, 3), (2, 4), (3, 8), (10, 11)]
    print(select_max_activity(activity_1))