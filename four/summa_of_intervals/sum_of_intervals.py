class IntervalSumma:

    def __init__(self):
        pass

    @staticmethod
    def sum_intervals(intervals):
        result = 0
        left, right = [], []
        for element in intervals:
            left.append(element[0])
            right.append(element[1])

        left.sort()
        right.sort()

        for i in range(len(left) - 1):
            result += (right[i] - left[i])

            if right[i] >= left[i + 1]:
                result -= abs(right[i] - left[i + 1])

        result += right[-1] - left[-1]

        return result
