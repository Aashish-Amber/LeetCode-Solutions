class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        num_freq_map = {}
        ans = False
        for num in arr :
            rem_fac = k - abs(num%k)
            rem = abs(num%k)
            if rem_fac in num_freq_map and num_freq_map[rem_fac] :
                num_freq_map[rem_fac ] -=1
            else:
                if rem in num_freq_map :
                    num_freq_map[rem ]+=1
                else:
                    num_freq_map[rem ] = 1
            #print(num_freq_map)
                
        if 0 in num_freq_map:
            del num_freq_map[0]
            
        if set(num_freq_map.values())== {0} or len(list(num_freq_map.keys()))==0:
            ans = True
        
        return ans
                
                
                
        