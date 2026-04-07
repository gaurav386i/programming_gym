"""
Given an array of intervals intervals where intervals[i] = [starti, endi], merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""
def merge_intervals(intervals: list[list]) -> list[list]:
    output = []
    for intvl in intervals:
        
        
