from Client import Client

class Company(object):

    clients = []

    def __init__(self, name, RFC, direction, clients=None):
        if clients is None:
            clients = []
        self.name = name
        self.RFC = RFC
        self.direction = direction
        self.clients = clients


    def add(self, c):
        self.clients.append(c)


    def __repr__(self):
        return "\n Nombre de Empresa: %s \n RFC: %s \n Dirección: %s \n \n Clientes registrados en %s: \n %s \n" % (
            self.name, self.RFC, self.direction, self.name, self.clients)



class Companies:

    companiesList = []

    def __init__(self, companiesList= None):
        if companiesList is None:
            companiesList = []
            self.companiesList = companiesList

    
    def addCompany(self, company):
        self.companiesList.append(company)


    def __repr__(self):

        return "\n Empresas dadas de Alta: \n %s \n" % (self.companiesList)
