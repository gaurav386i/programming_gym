"""
Given an array of intervals intervals where intervals[i] = [starti, endi], merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""
def merge_intervals(intervals: list[list]) -> list[list]:
    if len(intervals) <= 1:
        return intervals
    intervals.sort()
    merged = []

    for intrvl in intervals:
        if not merged or merged[-1][1] < intrvl[0]:
            merged.append(intrvl)
        else:
            merged[-1][1] = max(merged[-1][1], intrvl[1])
    return merged

if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_intervals(intervals))

        
