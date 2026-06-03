class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left=0

        m=len(matrix)
        n=len(matrix[0])

        right=m*n-1

        while left<=right:

            mid= (left+right)//2

            mid_i = mid//n
            mid_j = mid % n

            curr_num = matrix[mid_i][mid_j]

            if curr_num > target:
                right = mid-1
            elif curr_num < target:
                left = mid+1
            else:
                return True
        
        return False
        


        