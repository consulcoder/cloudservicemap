from blog.models import *
from tool.models import *

def maxFromDictionary(dictionary):
    max = 0
    for value in dictionary:
        if value>max:
            max=value
    return max
def countRowOfCategory(subcategory):
    counter = {}
    for prov in Fournisseur.objects.all():
        counter[prov.id] = 0
    for serv in Service.objects.filter(sous_categorie=subcategory)
        """ Obetniedo provedores de servicios """
        prov_id = 1
        prov_name = str.upper(serv.fournisseurs)
        prov = Fournisseur.objects.get(str.upper(nom_f) = prov_name)
        if prov:
            prov_id = prov.id
        counter[prov_id] += 1
    return maxFromDictionaryKeyValue(counter)
class ColumnNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
def listCountRowOfCategory(category):
    dictCountRow = {}
    for cat in Sous_Categorie.objects.filter(categorie=category):
        dictCountRow[cat.id] = countRowOfCategory(cat)
    listCountRow = []
    for key,value in dictCountRow:
        listCountRow.append(ColumnNode(key,value))
    sorted(listCountRow, key=lambda column: column.value, reverse=True)
    return listCountRow



