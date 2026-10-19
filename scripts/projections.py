#!/usr/bin/env python3
"""
Script de calcul du classement actuel et de projection transitive
basé sur un fichier TOML de résultats FFTT pour Pexiora TT.
Nécessite Python 3.11+ (tomllib inclus) ou le paquet `tomli` pour les versions plus anciennes.
"""

import pathlib
import sys
import pathlib
from dataclasses import dataclass, field
from typing import Dict, List, Optional

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        sys.exit("Erreur : Le module 'tomllib' est requis. Utilisez Python 3.11+ ou installez 'tomli' (`pip install tomli`).")

@dataclass
class ClubStats:
    name: str
    v: int = 0
    n: int = 0
    d: int = 0
    f: int = 0
    pts: int = 0
    diff_manches: int = 0
    initial_index: int = 0

    def compute_points(self, pt_config: Dict[str, int]):
        self.pts = (self.v * pt_config.get('v', 3) +
                    self.n * pt_config.get('n', 2) +
                    self.d * pt_config.get('d', 1) +
                    self.f * pt_config.get('f', 0))

def parse_score(score_str: str) -> Optional[tuple[int, int]]:
    """Extrait le score au format 'dom-ext'."""
    try:
        dom, ext = map(int, score_str.strip().split('-'))
        return dom, ext
    except (ValueError, AttributeError):
        return None

def process_poule(poule: dict, pt_config: dict) -> tuple[List[ClubStats], List[ClubStats]]:
    """
    Calcule le classement actuel et la projection pour une poule.
    """
    clubs: Dict[str, ClubStats] = {}

    # 1. Initialiser la liste des clubs
    for idx, c in enumerate(poule.get('classement', [])):
        club_name = c['club']
        if club_name == "EXEMPT":
            continue
        clubs[club_name] = ClubStats(
            name=club_name,
            v=c.get('v', 0),
            n=c.get('n', 0),
            d=c.get('d', 0),
            f=c.get('f', 0),
            initial_index=idx
        )

    # 2. Mettre à jour les stats avec les rencontres saisies de Pexiora
    rencontres = poule.get('rencontres', [])
    for r in rencontres:
        dom = r.get('dom')
        ext = r.get('ext')
        score = r.get('score')
        statut = r.get('statut')

        if dom == "EXEMPT" or ext == "EXEMPT":
            continue

        if score and not statut:
            parsed = parse_score(score)
            if parsed:
                s_dom, s_ext = parsed
                diff = s_dom - s_ext

                # Mise à jour pour le club à domicile s'il s'agit de Pexiora
                if dom in clubs and "PEXIORA" in dom:
                    clubs[dom].diff_manches += diff
                    if s_dom > s_ext:
                        clubs[dom].v += 1
                    elif s_dom == s_ext:
                        clubs[dom].n += 1
                    else:
                        clubs[dom].d += 1

                # Mise à jour pour le club à l'extérieur s'il s'agit de Pexiora
                if ext in clubs and "PEXIORA" in ext:
                    clubs[ext].diff_manches -= diff
                    if s_ext > s_dom:
                        clubs[ext].v += 1
                    elif s_dom == s_ext:
                        clubs[ext].n += 1
                    else:
                        clubs[ext].d += 1

    # Calculer les points actuels
    for c in clubs.values():
        c.compute_points(pt_config)

    # Trier pour obtenir le classement actuel
    # Tri par : 1) Points (décroissant), 2) Diff de manches (décroissant), 3) Ordre initial dans le TOML
    classement_actuel = sorted(
        clubs.values(),
        key=lambda x: (x.pts, x.diff_manches, -x.initial_index),
        reverse=True
    )

    # 3. Projection transitive pour les rencontres non jouées
    # Calcul des forces relatives (ratio de victoires ou score moyen)
    projections = {name: ClubStats(name=c.name, v=c.v, n=c.n, d=c.d, f=c.f, diff_manches=c.diff_manches, initial_index=c.initial_index)
                   for name, c in clubs.items()}

    # Évaluer la puissance estimée de chaque équipe à partir de ses victoires/défaites
    ratings = {}
    for name, c in clubs.items():
        total_m = c.v + c.n + c.d
        if total_m > 0:
            ratings[name] = (c.v * 3 + c.n * 1.5) / total_m
        else:
            ratings[name] = 1.0  # Valeur neutre par défaut

    # Simuler les rencontres restantes de Pexiora
    for r in rencontres:
        dom = r.get('dom')
        ext = r.get('ext')
        score = r.get('score')
        statut = r.get('statut')

        if dom == "EXEMPT" or ext == "EXEMPT":
            continue

        if not score and statut != "reporte":
            r_dom = ratings.get(dom, 1.0)
            r_ext = ratings.get(ext, 1.0)

            # Modélisation transitive simple
            diff_rating = r_dom - r_ext

            if diff_rating > 0.5:
                # Domination nette Domicile
                s_dom, s_ext = 10, 4
            elif diff_rating < -0.5:
                # Domination nette Extérieur
                s_dom, s_ext = 4, 10
            elif diff_rating > 0.15:
                # Victoire serrée Domicile
                s_dom, s_ext = 8, 6
            elif diff_rating < -0.15:
                # Victoire serrée Extérieur
                s_dom, s_ext = 6, 8
            else:
                # Match équilibré
                s_dom, s_ext = 7, 7

            # Appliquer au club Pexiora concerné
            if dom in projections and "PEXIORA" in dom:
                projections[dom].diff_manches += (s_dom - s_ext)
                if s_dom > s_ext:
                    projections[dom].v += 1
                elif s_dom == s_ext:
                    projections[dom].n += 1
                else:
                    projections[dom].d += 1

            if ext in projections and "PEXIORA" in ext:
                projections[ext].diff_manches += (s_ext - s_dom)
                if s_ext > s_dom:
                    projections[ext].v += 1
                elif s_dom == s_ext:
                    projections[ext].n += 1
                else:
                    projections[ext].d += 1

            # Appliquer aussi la simulation théorique pour l'adversaire
            if dom in projections and "PEXIORA" not in dom:
                projections[dom].diff_manches += (s_dom - s_ext)
                if s_dom > s_ext:
                    projections[dom].v += 1
                elif s_dom == s_ext:
                    projections[dom].n += 1
                else:
                    projections[dom].d += 1

            if ext in projections and "PEXIORA" not in ext:
                projections[ext].diff_manches += (s_ext - s_dom)
                if s_ext > s_dom:
                    projections[ext].v += 1
                elif s_dom == s_ext:
                    projections[ext].n += 1
                else:
                    projections[ext].d += 1

    # 4. Compléter les rencontres restantes des autres clubs (hors Pexiora)
    # Le calendrier complet n'est pas connu : chaque club rencontre une fois
    # tous les autres, et les matchs restants sont simulés face à un
    # adversaire « moyen » de la poule.
    nb_rencontres = len(clubs) - 1
    for name, c in projections.items():
        if "PEXIORA" in name:
            continue
        restantes = nb_rencontres - (c.v + c.n + c.d + c.f)
        autres = [r for n, r in ratings.items() if n != name]
        r_moyen = sum(autres) / len(autres) if autres else 1.0
        diff_rating = ratings.get(name, 1.0) - r_moyen
        for _ in range(max(restantes, 0)):
            if diff_rating > 0.5:
                s_pour, s_contre = 10, 4
            elif diff_rating < -0.5:
                s_pour, s_contre = 4, 10
            elif diff_rating > 0.15:
                s_pour, s_contre = 8, 6
            elif diff_rating < -0.15:
                s_pour, s_contre = 6, 8
            else:
                s_pour, s_contre = 7, 7
            c.diff_manches += s_pour - s_contre
            if s_pour > s_contre:
                c.v += 1
            elif s_pour == s_contre:
                c.n += 1
            else:
                c.d += 1

    for c in projections.values():
        c.compute_points(pt_config)

    classement_projecte = sorted(
        projections.values(),
        key=lambda x: (x.pts, x.diff_manches, -x.initial_index),
        reverse=True
    )

    return classement_actuel, classement_projecte

def main():
    filename = pathlib.Path(__file__).parent.parent / "source" / "data" / "championnat-en-cours.toml"
    try:
        with open(filename, "rb") as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        print(f"Fichier '{filename}' non trouvé. Veuillez créer le fichier ou fournir le bon chemin.")
        return

    pt_config = data.get('points', {'v': 3, 'n': 2, 'd': 1, 'f': 0})
    poules = data.get('poules', [])

    print("=" * 70)
    print(f" PROJECTION DU CHAMPIONNAT - SAISON {data.get('saison', '')} PHASE {data.get('phase', '')}")
    print("=" * 70)

    for i, poule in enumerate(poules, 1):
        div = poule.get('division', 'Inconnue')
        montees = poule.get('montees', 0)
        descentes = poule.get('descentes', 0)

        actuel, projecte = process_poule(poule, pt_config)

        print(f"\n--- POULE {i} : {div} (Montées: {montees}, Descentes: {descentes}) ---")
        print("\n  [ CLASSEMENT ACTUEL ESTIMÉ ]")
        print(f"  {'Pos':<4} | {'Club':<28} | {'Pts':<4} | {'V-N-D':<7} | {'Diff':<5}")
        print("  " + "-" * 55)
        for rank, c in enumerate(actuel, 1):
            tag = ""
            if rank <= montees:
                tag = " (Zone Montée)"
            elif rank > len(actuel) - descentes:
                tag = " (Zone Descente)"
            print(f"  {rank:<4} | {c.name:<28} | {c.pts:<4} | {c.v}-{c.n}-{c.d:<3} | {c.diff_manches:<+5}{tag}")

        print("\n  [ PROJECTION FINALE PAR TRANSITIVITÉ ]")
        print(f"  {'Pos':<4} | {'Club':<28} | {'Pts':<4} | {'V-N-D':<7} | {'Diff':<5}")
        print("  " + "-" * 55)
        for rank, c in enumerate(projecte, 1):
            tag = ""
            if rank <= montees:
                tag = " [MONTÉE]"
            elif rank > len(projecte) - descentes:
                tag = " [RELEGATION]"
            print(f"  {rank:<4} | {c.name:<28} | {c.pts:<4} | {c.v}-{c.n}-{c.d:<3} | {c.diff_manches:<+5}{tag}")

if __name__ == "__main__":
    main()
