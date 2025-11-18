# Spécification des Features – Pexiora TT

**Sources** : constitution.md, README.md
**Date** : 2025-11-18

---

## Clarifications & Décisions

- L’authentification pour l’admin DecapCMS se fait uniquement via GitHub OAuth (Netlify Identity est déprécié et non utilisé).
- Chaque page modifiable (actualités, adhésions, horaires, staff, sponsors) doit être une collection distincte dans la configuration DecapCMS, avec les champs adaptés :
  - Staff : nom, rôle, photo
  - Horaires : jour, heure, lieu, saison
  - Adhésions : tarif, description, saison
  - Sponsors : nom, logo, lien
  - Actualités : titre, texte, date, image, tags
- Les trois dernières actualités affichées sur la page d’accueil sont extraites de la collection « actualités » DecapCMS, triées par date décroissante.
- Les images doivent être optimisées avant upload, stockées dans `static/uploads/` ou `static/images/`, et chaque image doit avoir un champ `alt` dans DecapCMS.
- Si une collection (staff, sponsors, actualités, etc.) est vide, la page affiche un message informatif (« Aucun élément pour le moment »).
- Les exigences d’accessibilité (WCAG 2.1 AA, ARIA, navigation clavier, contraste, alt text) sont validées par des outils comme axe ou Lighthouse.
- Les messages d’erreur affichés au visiteur sont explicites et non techniques (ex : « Aucun contenu disponible », « Accès refusé »).
- La rapidité de publication via DecapCMS est validée manuellement lors de la recette (modification visible en <2 min).
- Toute mention ou dépendance à Netlify Identity est supprimée des specs, docs et configuration.

---

## 1. User Scenarios & Testing

### User Story 1 – Page d'accueil (P1)

Un visiteur accède à la page d'accueil, voit la présentation du club et les trois dernières actualités.

**Test indépendant** : Accès à la page d'accueil, affichage correct des infos et des trois dernières actualités.

**Acceptance Scenarios** :

1. **Given** un visiteur, **When** il accède à l'URL principale, **Then** il voit la présentation du club et les trois dernières actualités.

---

### User Story 2 – Page actualités (P2)

Un visiteur consulte la page "Actualités" qui liste toutes les nouveautés, infos et événements du club.

**Test indépendant** : Accès à la page actu, affichage complet et trié des actualités.

**Acceptance Scenarios** :

1. **Given** un visiteur, **When** il accède à la page actu, **Then** il voit la liste complète des actualités, triées par date.

---

### User Story 3 – Page adhésions (P3)

Un visiteur consulte la page "Adhésions" pour voir les tarifs et modalités d'inscription.

**Test indépendant** : Accès à la page adhésions, affichage des tarifs et infos à jour.

**Acceptance Scenarios** :

1. **Given** un visiteur, **When** il accède à la page adhésions, **Then** il voit les tarifs et modalités d'inscription.

---

### User Story 4 – Page horaires et entraînements (P4)

Un visiteur consulte la page "Horaires et entraînements" pour voir les créneaux et lieux d'entraînement.

**Test indépendant** : Accès à la page horaires, affichage des créneaux et infos à jour.

**Acceptance Scenarios** :

1. **Given** un visiteur, **When** il accède à la page horaires, **Then** il voit les créneaux et lieux d'entraînement.

---

### User Story 5 – Page staff (P5)

Un visiteur consulte la page "Staff" pour voir la composition de l'équipe encadrante.

**Test indépendant** : Accès à la page staff, affichage des membres et rôles à jour.

**Acceptance Scenarios** :

1. **Given** un visiteur, **When** il accède à la page staff, **Then** il voit la liste des membres du staff et leurs rôles.

---

### User Story 6 – Page sponsors (P6)

Un visiteur consulte la page "Sponsors" pour voir les partenaires du club.

**Test indépendant** : Accès à la page sponsors, affichage des logos et liens des sponsors.

**Acceptance Scenarios** :

1. **Given** un visiteur, **When** il accède à la page sponsors, **Then** il voit la liste des sponsors avec logos et liens.

---

### User Story 7 – Mise à jour du contenu via DecapCMS (P1 à P6)

Un administrateur modifie le contenu de chaque page (staff, horaires, adhésions, actualités, sponsors) via DecapCMS.

**Test indépendant** : Modification d'un contenu via l'admin, publication effective sur le site.

**Acceptance Scenarios** :

1. **Given** un admin connecté, **When** il modifie une page via DecapCMS, **Then** la modification est visible côté public.

---

### Edge Cases

- Que se passe-t-il si une actualité n'a pas d'image ou de texte ?
- Que voit un visiteur si la liste des sponsors est vide ?
- Que se passe-t-il si les horaires sont modifiés en cours de saison ?
- Que voit un visiteur si le staff n'est pas renseigné ?
- Accès refusé à l'admin pour les non-authentifiés

---

## 2. Requirements

### Functional Requirements

- **FR-001** : Le site DOIT proposer une page d'accueil avec présentation et trois dernières actualités
- **FR-002** : Le site DOIT proposer une page actualités listant toutes les nouveautés, infos et événements
- **FR-003** : Le site DOIT proposer une page adhésions avec tarifs et modalités à jour
- **FR-004** : Le site DOIT proposer une page horaires et entraînements avec créneaux et lieux à jour
- **FR-005** : Le site DOIT proposer une page staff avec membres et rôles à jour
- **FR-006** : Le site DOIT proposer une page sponsors avec logos et liens
- **FR-007** : Le contenu de chaque page (hors accueil) DOIT être modifiable via DecapCMS
- **FR-008** : Les actualités DOIVENT être ajoutées, modifiées ou supprimées via DecapCMS
- **FR-009** : Les images DOIVENT être optimisées, avoir un alt text et être stockées dans les dossiers dédiés
- **FR-010** : Le site DOIT être responsive et conforme WCAG 2.1 AA
- **FR-011** : Les hooks Husky, scripts lint et tests DOIVENT être actifs et validés avant tout déploiement
- **FR-012** : Le site DOIT afficher des messages d’erreur clairs en cas de problème de contenu ou d’accès

### Key Entities

- **Actualité** : titre, texte, date, image, tags
- **Adhésion** : tarif, description, saison
- **Horaire** : jour, heure, lieu, saison
- **Staff** : nom, rôle, photo
- **Sponsor** : nom, logo, lien
- **Utilisateur CMS** : rôle (admin), authentification

---

## 3. Success Criteria

### Measurable Outcomes

- **SC-001** : 100% des pages accessibles et validées par test manuel
- **SC-002** : 95% des modifications CMS publiées en moins de 2 minutes
- **SC-003** : 100% des images ont un alt text et sont optimisées
- **SC-004** : 100% des tests d’accessibilité (contraste, navigation clavier, ARIA) passent
- **SC-005** : 0 erreur critique lors du build ou du déploiement Netlify
- **SC-006** : 100% des commits passent les hooks Husky et la CI

---

## 4. Assumptions

- Les admins sont invités via GitHub OAuth
- Les images sont optimisées avant upload
- Les utilisateurs non authentifiés n’ont pas accès à l’admin
- Les conventions du projet sont respectées par défaut

---

## 5. Dépendances

- Zola, Alpine.js, Bulma, DecapCMS, Netlify, Husky, Prettier, Markdownlint, BATS, Commitizen
- Configuration des fichiers : config.toml, netlify.toml, static/admin/config.yml
- Structure des dossiers : source/, static/, templates/, tests/

---

## 6. Notes

- Cette spécification est basée sur la constitution et les standards du projet, elle doit être révisée à chaque évolution majeure du README ou des instructions Copilot.
