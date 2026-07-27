class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        top,bottom=0,row-1
        mid_row=0
        while top <= bottom:
            mid_row=(top+bottom)//2
            if target < matrix[mid_row][0]: bottom=mid_row-1
            elif target > matrix[mid_row][-1]: top=mid_row+1
            else: break
        start,end=0,col-1
        while start<=end:
            value=(start+end)//2
            if target < matrix[mid_row][value]:end=value-1
            elif target > matrix[mid_row][value]:start=value+1
            else: return True
        return False
        