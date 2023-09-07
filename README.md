# Cortex Groove

## Changelog
CortexGroove est (dans un premier temps) une librairie.
C'est à dire que les utilisateurs ont des réseaux de neurones, ici appelé UserNeuralNetwork qui représente n'importe quel réseaux - donc la lib que l'utilisateur préfère etc...
Ces utilisateurs implémentent sur leur classe une interface INeuralNetwork qui sera appelé par l'Engine.
L'Engine est le coeur du framework, c'est via cette objet que l'on va paramétrer nos différents réseaux neuroneaux.

L'Engine et l'interface sont dans le dossier src/main_lib
Et un exemple de NN implémenté à l'engine se trouve dans src/main_test.py

## Organisation générale
Le projet Cortex Groove est constitué de plusieurs modules :
 - Librairie :
    Il y a en premier lieu une librairie python qui permet de faire fonctionner les différents réseaux de neurones ensembles.
 - Service API :
    Un service permettant d'intéragir avec Cortex Groove via API REST est disponible. Il s'agit d'un projet Django, 
    permettant notamment d'avoir une mémoire des différents réseaux et leurs configurations.
 - Website :
    Une interface web interactive permettra de configurer, entrainer et faire des prédictions avec de plusieurs réseaux de neurones.

## Reflexions sur les objectifs

### Lot 1

 - L'objectif est dans un premier temps de faire une librairie python, ou l'utilisateur doit déclarer ses réseaux.
 - La librairie permet simplement de faire le lien entre les réseaux et ne permet pas d'entrainer les réseaux.

### Lot 2

 - Pouvoir entrainer dynamique des réseaux permettra d'optimiser en temps réels les réseaux, et tester de manière dynamique plusieurs configurations.
 - Intégrer un site web avec Nuxt / Tailwind et une interface API REST via Django.

# Librairie Python
Exemple d'utilisation de la librairie 
```python
from CortexGroove import INeuralNetwork, Engine

"""
    On hérite d'une part du réseau de neurone utilisateur, et d'autre part de l'interface de CortexGroove
    Ici le réseau de l'utilisateur est TensorFlowNeuralNetwork, mais il peut s'agir de n'importe quel réseau de neurone.
"""
class NeuralNetworkCortex(TensorFlowNeuralNetwork, INeuralNetwork):
    
    # Ici "shape" correspond à la forme du réseau, tel que : [format de donnée en entrée, format de donnée en sortie]
    # Exemple plus bas
    def __init__(self, shape):
        ...

    # Méthode hérité de INeuralNetwork, qui va permettre de faire le lien entre CortexGroove et le réseau utilisateur
    def run(self, data):
        return TensorFlowNeuralNetwork.run(data)


# On initialise les réseaux en leur donnants leurs formes
neural_network_1 = NeuralNetworkCortex([3, 2])
neural_network_2 = NeuralNetworkCortex([2, 1])
neural_network_3 = NeuralNetworkCortex([3, 1])

# Création de l'orchestrateur
engine = Engine()

# Création des première couches
engine.set_layer(neural_network_1, layer_index: 0)
engine.set_layer(neural_network_2, layer_index: 0)

# Création de la dernière couches
engine.set_layer(neural_network_3, layer_index: 1)


"""
On peut maintenant tester notre réseau :
    En prenant des réseaux entrainés pour résoudre les fonctions respectives suivante :
        réseau 1 : [ (x0 / 2) + x1 - x2, x1 * 2 ]
        réseau 2 : [ x3 - x4 ]
        réseau 3 : [ y0 + y1 - y2 ]
"""

# Donnée de tests :
test_data = [
    [1, 2, 3], # x0 x1 x2
    [4, 5]     # x3 x4
]

expected_result = 4.5 # z

# On essaye de prédire un nouveau résultat
result = engine.run(test_data)

print(f"Result : {result}, expected result : {expected_result}")
```

Voici donc l'exemple illustré du code ci-dessus :
![SVG Image](./documentation/Example_Diagram.svg)

Avec les données :
![SVG Image](./documentation/Example_Diagram_withData.svg)

# Description technique

Vous trouverez tous les détails techniques dans le [fichier de description](./documentation/Description%20technique.md)
# Accroche

CortexGroove, le gestionnaire de réseaux de neurones qui vous fait danser au rythme des synapses !

Laissez-vous entraîner dans le tourbillon des années 70 avec CortexGroove, le manager de réseaux de neurones qui vous fera voyager dans le temps. Avec sa patte d'eph' algorithmique et son style afro-futuriste, il gère vos neurones artificiels à la manière d'un DJ virtuose.

Nostalgiques des boules à facettes et des pantalons pattes d'eph', plongez-vous dans l'univers psychédélique de CortexGroove. Son interface aux couleurs flashy et aux motifs hypnotiques vous garantit une expérience hors du commun.

Que vous soyez un chercheur en IA, un scientifique du dimanche ou un passionné de disco, CortexGroove est le compagnon idéal pour vos projets de réseaux de neurones. Il vous aidera à résoudre des problèmes complexes avec style et panache, tout en dansant sur les rythmes endiablés de l'époque.

Optimisez les performances de vos neurones artificiels avec la puissance de la discothèque ! CortexGroove, c'est la fusion parfaite entre la technologie d'aujourd'hui et l'ambiance funky des années 70. Alors, chaussez vos meilleures chaussures à semelles compensées et préparez-vous à groover avec CortexGroove !

Ne perdez pas le rythme, rejoignez la révolution CortexGroove et laissez-vous emporter par cette aventure psychédélique et groovy !

