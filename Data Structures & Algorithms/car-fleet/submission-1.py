class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        # doesnt work as im calculating independently , but if one position is after another it cannot reach before 
        # time = []
        # groups = {}
        # for pos,sp in zip(position,speed):
        #     time.append((target - pos)//sp)

        # for i in time:
        #     groups[i] = groups.get(i,0) + 1 


        # return len(groups)


        cars = sorted(zip(position,speed), reverse = True )

        stack = []

        for pos, spd in cars:
            time = (target - pos) /spd

            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)

        