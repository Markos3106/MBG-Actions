from prova_solucio5 import *
import pytest

@pytest.mark.parametrize(
    "biblioteca, res_esperat", 
    [
        ([{"llibre": "El Quixot", "categoria": "novel·la"}], 
        ['El Quixot']), #Aixo és el resultat.
        ([{"llibre": "El Quixot", "categoria": "novel·la"}, {"llibre": "Crim i Càstig", "categoria": "novel·la"}],
        ['El Quixot', 'Crim i Càstig']) #Aixo és el resultat.
    ]
)
def test_llibres_per_categoria(biblioteca, res_esperat):
    resultat = llibres_per_categoria(biblioteca, "novel·la")
    assert resultat == res_esperat

@pytest.mark.parametrize(
    "biblioteca, parametre1, res_esperat",
    [
        ([{"llibre": "Pepito Grillo", "prestecs": [{"retornat": True}]}],
        "Pepito Grillo",  #Llibre que volem buscar
        True),  #Resultat
        ([{"llibre": "Pepito Grillo", "prestecs": [{"retornat": True},{"retornat": False}]}],
        "Pepito Grillo",
        False)
    ]
)
def test_esta_disponible(biblioteca, parametre1, res_esperat):
    """
    El test és per veure que el llibre que tenim ha estat retornat o encara no el tenim disponible.
    """
    #El parametre 1 és el llibre que volem saber per la funció de si esta disponible.
    resultat = esta_disponible(biblioteca, parametre1)
    assert resultat == res_esperat

@pytest.mark.parametrize(
    "biblioteca, usuari, res_esperat",
    [
        ([{"llibre": "Pepito Grillo", "prestecs": [{"usuari": "Maria","retornat": True}]}],
        "Maria",
        False),
        ([{"llibre": "Pepito Grillo", "prestecs": [{"usuari": "Pere","retornat": False}]}],
        "Pere",
        True)
    ]
)
def test_usuari_te_prestecs(biblioteca, usuari, res_esperat):
    """
    Aquest test és per veure que l'usuari que li pasem ha retornat el llibre o no.
    """
    resultat = usuari_te_prestecs(biblioteca, usuari)
    assert resultat == res_esperat
    
@pytest.mark.parametrize(
    "biblioteca, llibre, res_esperat",
    [
        ([{"llibre": "Rasputin", "prestecs": [
            {"usuari": "Pere", "dies": 15},
            {"usuari": "Maria", "dies": 30}
            ]}],
        "Rasputin", #Aixo és el llibre
        45), #El total de dies que ha de retornar
        ([{"llibre": "El Senyor dels Anells", "prestecs": [
            {"usuari": "Joan", "dies": 10},
            {"usuari": "Marta", "dies": 25}
            ]}],
        "El Senyor dels Anells", #Aixo és el llibre
        35), #El total de dies que ha de retornar
    ]
)
def test_dies_prestec_total(biblioteca, llibre, res_esperat):
    """
    La funció et diu els dies que que no han estat en la llibreria, basicament els dies de prestec total.
    """
    resultat = dies_prestec_total(biblioteca, llibre)
    assert resultat == res_esperat