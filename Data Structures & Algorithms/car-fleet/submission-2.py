class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        stack = []

        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s
            print(time)
            if stack and stack[-1] >= time:
                print(stack[-1])
                time = stack[-1]
                stack.pop()
            stack.append(time)
            print(stack[-1])

        return len(stack)