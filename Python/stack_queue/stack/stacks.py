from collections import deque

def daily_temperature_getting_warmer_in_days_naive(temps: list[int]) -> list[int]:
    # [73, 74, 75, 71, 69, 72, 76, 73]
    if not temps:
        return []
    result = [0] * len(temps) 
    for i, temp in enumerate(temps):
        for j, temp2 in enumerate(temps[i+1:]):
            if temp2 > temp:
                result[i] = j + 1 
                break            
    return result

def daily_temperature_getting_warmer_in_days_ef(temps: list[int]) -> list[int]:
    if not temps:
        return []
    n = len(temps)
    stack = []
    result = [0] * n
    for today in range(n):
        while stack and temps[today] > temps[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = today - prev_day
        stack.append(today)
    return result


    

if __name__ == "__main__":
    print(
        daily_temperature_getting_warmer_in_days_ef(
            [73, 74, 75, 71, 69, 72, 76, 73]
        )
    )
