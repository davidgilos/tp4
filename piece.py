class Piece:
    def __init__(self,line,col,couleur):
        """Initialise un fou à la position (ligne,colonne) avec la bonne couleur 0 pour noir, 1 pour blanc"""
        self.pos = (line,col) # Sa position
        self.color = couleur # Sa couleur ... il faudra mettre super() si on a une classe Pièce mère.

    def deplacer(self,nouvPos,plateau):
        if self.deplacementValide(nouvPos,plateau):
            self.pos = nouvPos
        # else on ne change rien : on retourne la position courante 
        # pour signifier que le changement a eu lieu ... ou pas
        return self.pos

    def deplacementValide(self,nouvPos,plateau):
        pos_dep = self.pos
        pos_arr = nouvPos 
        # Si une pièce à l'arrivée et identique à la couleur du fou
        pieceArr = plateau.getPiece(pos_arr[0],pos_arr[1])
        if pieceArr != None and pieceArr.color == self.color:
            return False
    


