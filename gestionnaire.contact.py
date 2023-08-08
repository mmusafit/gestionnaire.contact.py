class contact:
    def __init__(self,nom,prenom,numero_telephone,adresse_email):
        self.nom=nom
        self.prenom=prenom
        self.numero_telephone=numero_telephone
        self.adresse_email=adresse_email
        self.next=None

    def getnom(self):
        return self.nom

    def getprenom(self):
        return self.prenom

    def getnumero_telephone(self):
        return self.numero_telephone

    def getadresse_email(self):
        return self.adresse_email

    def getNext(self):
        return self.next

    def setnom(self,newnom):
        self.nom=newnom

    def setnext(self,newnext):
        self.next=newnext

    def setprenom(self):
        return self.prenom

    def setnext(self,newnext):
        self.next=newnext

    def setnumero_telephone(self,new_numero_telephone):
        self.numero_telephone=new_numero_telephone

    def setNext(self,newnext):
        self.next=newnext

    def setadresse_email(self,new_adresse_email):
        self.adresse_email=new_adresse_email



class liste_contacts:
    def __init__(self):
        self.contact=None

    def isEmpty(self):
        return self.contact==None

    def add(self,item):
        temp=contact(item)
        temp.setNext(self.contact)
        self.contact=temp

    def addAfter(self,base,item):
        temp=contact(item)
        temp.setNext(base.getNext())
        base.setNext(temp)


