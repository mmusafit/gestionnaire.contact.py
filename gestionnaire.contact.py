
class Contact:
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

class ListeContacts:
    def __init__(self):
        self.contact = None

    def is_empty(self):
        return self.contact is None

    def add(self, item):
        temp = Contact(item['nom'], item['prenom'], item['numero_telephone'], item['adresse_email'])
        temp.setnext(self.contact)  # Utilisez "setnext" au lieu de "set_next"
        self.contact = temp

    def add_after(self, base, item):
        temp = Contact(item['nom'], item['prenom'], item['numero_telephone'], item['adresse_email'])
        temp.set_next(base.get_next())
        base.set_next(temp)


# Création de quelques contacts
Contact1 = {"nom": "Doe", "prenom": "John", "numero_telephone": "123456789", "adresse_email": "john@example.com"}
Contact2 = {"nom": "Smith", "prenom": "Jane", "numero_telephone": "987654321", "adresse_email": "jane@example.com"}

# Création d'une liste de contacts
Contacts_list = ListeContacts()

# Ajout de contacts à la liste
Contacts_list.add(Contact1)
Contacts_list.add(Contact2)

# Affichage des contacts
current_Contact = Contacts_list.contact
while current_Contact is not None:
    print("Nom:", current_Contact.nom)
    print("Prénom:", current_Contact.prenom)
    print("Numéro de téléphone:", current_Contact.numero_telephone)
    print("Adresse email:", current_Contact.adresse_email)
    print()
    current_Contact = current_Contact.next
