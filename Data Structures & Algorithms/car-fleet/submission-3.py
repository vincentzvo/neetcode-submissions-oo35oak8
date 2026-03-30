class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        stack = []

        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s
            if stack and stack[-1] >= time:
                time = stack.pop()
            stack.append(time)

        return len(stack)