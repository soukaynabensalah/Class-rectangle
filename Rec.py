class Rectangle() :
    def __init__(self, longueur, largueur) :
         self.longueur = longueur
         self.largueur = largueur
         
    def P(self) :
        return 2 * (self.longueur + self.largueur)
        
    def Air(self) :
        return self.longueur * self.largueur
        
    def IsCarre(self) :
        if self.longueur == self.largueur :
            return "Il s'agit d'un carré"
        else :
            return "Il ne s'agit pas d'un carré"
    
    def AffichageRectangle(self) :
        print("la longueur de rectangle est : ",self.longueur)
        print("la largueur de rectangle est : ",self.largueur)
        print("l'air de rectangle est : ", self.Air())
        print("le périmètre de rectangle est : ", self.P())
        print(self.IsCarre())



rec1 = Rectangle(1, 30)
rec2 = Rectangle(5, 5)

print(rec1.P())
print(rec1.Air())
print(rec1.IsCarre())
print(rec2.IsCarre())
print("*****")
rec1.AffichageRectangle()
print("*****")
rec2.AffichageRectangle()
       
   
         
