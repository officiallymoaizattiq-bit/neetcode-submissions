class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rr = 0, len(matrix) - 1
        row = -1
        while rl <= rr:                        
            rmid = (rl + rr) // 2
            if target < matrix[rmid][0]:        
                rr = rmid - 1
            elif target > matrix[rmid][-1]:     
                rl = rmid + 1
            else:                               
                row = rmid
                break

        if row == -1:                           
            return False

        cl, cr = 0, len(matrix[0]) - 1
        while cl <= cr:                          
            cmid = (cl + cr) // 2
            if matrix[row][cmid] == target:
                return True
            elif matrix[row][cmid] > target:
                cr = cmid - 1
            else:
                cl = cmid + 1
        return False