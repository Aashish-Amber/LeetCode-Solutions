class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir_map = {'N':1,'S':-1,'E':1,'W':-1}
        dir_x_y_set = {(0,0)}
        dir_sumx = 0
        dir_sumy = 0 
        ans = False
        for direction in path:
            if direction == 'E' or direction == 'W':
                dir_sumx = dir_sumx + dir_map[direction]
                
            if direction == 'N' or direction == 'S':
                dir_sumy = dir_sumy + dir_map[direction]
                
            dir_x_y = (dir_sumx,dir_sumy)
            
            if dir_x_y in dir_x_y_set:
                ans = True
                break
            else:
                dir_x_y_set.add(dir_x_y)
                
        return ans
            