class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0 #chech weather we can complete the circuit
        tank = 0 #to trace whihc station to start with we cannot start in negative
        start = 0 #first station

        for i in range(len(gas)):

            gain = gas[i] - cost[i]

            total += gain
            tank += gain

            if tank < 0:
                start = i + 1
                tank = 0
        if total < 0:
            return -1
        return start 
        


        