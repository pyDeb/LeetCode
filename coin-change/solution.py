
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create a list of length amount + 1 [0, amount]. Each index representing 
        # the the number of coins need to meet the
        # i-th target
        numbers = [x for x in range(amount + 1)]
        numbers[0] = 0
        
        for i in range(1, amount + 1):
            # sys.maxsize
            numbers[i] = 9223372036854775807
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    possible_amount = numbers[i - coin]
                    if possible_amount != 9223372036854775807 and 1 + possible_amount < numbers[i]:
                        numbers[i] = possible_amount + 1
                    
        if numbers[amount] == 9223372036854775807:
            return -1
        return numbers[amount]
        
