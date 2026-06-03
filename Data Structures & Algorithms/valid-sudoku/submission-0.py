class Solution:
    def containes_duplicates(self,liste:List[int])->bool:
        #je dois ajouter juste la containte des .
        liste=[x for x in liste if x!='.']
        return len(liste)!=len(set(liste))
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #unique horizontally
        for liste in board:
            if self.containes_duplicates(liste):
                return False
        #unique vertically
        #double list
        trans_board=[[board[j][i] for j in range(9)]for i in range(9)]
        for liste in trans_board:
            if self.containes_duplicates(liste):
                return False
        #reshape will be more efficient
        for i in range(0,9,3):
            for j in range(0,9,3):
                box=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if self.containes_duplicates(box):
                    return False
        return True
        
    
        