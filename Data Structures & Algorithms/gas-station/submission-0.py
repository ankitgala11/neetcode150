class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0

        n = len(gas)
        total_gas_avl = 0
        total_gas_req = 0
        curr_gas = 0

        for i in range(n):

            total_gas_avl += gas[i]
            total_gas_req += cost[i]

            curr_gas += gas[i]-cost[i]
            if curr_gas<0:
                curr_gas = 0
                start = i+1
            
        
        if total_gas_avl<total_gas_req:return -1
        return start
