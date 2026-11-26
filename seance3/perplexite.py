# ============================================================
#  Séance 3 --- la brique durable, l'instrument de mesure d'un moteur
#  Ces trois fonctions ne savent rien du modèle mesuré. Elles reçoivent les
#  probabilités qu'un moteur a données aux tokens réellement écrits, que ce
#  moteur soit le bigramme d'aujourd'hui ou le Transformer des séances
#  suivantes. Elles resserviront telles quelles pour choisir un moteur,
#  vérifier une quantification et mesurer l'oubli après un affinage.
# ============================================================
import math


def surprise(p):
    """La surprise, en bits, d'un token auquel le modèle donnait la
    probabilité p. Une probabilité nulle donne une surprise infinie."""
    if p == 0:
        return math.inf
    return math.log2(1 / p)


def entropie_croisee(probas):
    """La surprise moyenne par token, en bits, sur toutes les probabilités."""
    if not probas:
        raise ValueError("probas must be a non-empty iterable of probabilities")
    total = 0.0
    for p in probas:
        total += surprise(p)
    return total / len(probas)


def perplexite(probas):
    """La perplexité, 2 puissance la surprise moyenne. Elle se lit comme le
    nombre de candidats équiprobables entre lesquels le modèle hésite."""
    h = entropie_croisee(probas)
    return 2 ** h
#demo deja caputurer