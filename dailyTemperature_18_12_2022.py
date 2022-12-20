def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    top = -1
    ret  = []
    for i in range(len(temperatures)):
        while top > -1 and temperatures[i] > temperatures[stack[top]]:
            idx = stack[top]
            top -= 1
            ret[idx] = i - idx
        top += 1
        stack[top] = i

    return ret

test_case = [73,74,75,71,69,72,76,73]
