class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        left,right=0,row*col-1
        while left<=right:
            mid=(left+right)//2
            mid_val=matrix[mid//col][mid%col]
            if target==mid_val:
                return True
            elif target < mid_val:
                right = mid-1
            else: left=mid+1
        return False
        