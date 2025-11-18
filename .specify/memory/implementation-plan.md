# Plan d’implémentation – Pexiora TT

**Sources** : features-spec.md, constitution.md, README.md
**Date** : 2025-11-18

---

## 1. Structure du projet

- `source/content/` : Pages Markdown (accueil, actualités, adhésions, horaires, staff, sponsors)
- `source/templates/` : Templates Tera (base.html, page.html, section.html, actualites.html, staff.html, sponsors.html, etc.)
- `source/static/` : Assets (logo.png, favicon.svg, style.css, images, uploads)
- `source/static/admin/config.yml` : Configuration DecapCMS (collections pour chaque page modifiable)
- `tests/` : Tests BATS pour l’infrastructure
- `justfile` : Commandes d’automatisation

---

## 2. Phases d’implémentation

### Phase 1 – Initialisation & Structure

- Créer la structure des dossiers et fichiers de base
- Mettre en place le style CSS avec la palette autour de #002a4b
- Ajouter le logo et favicon
- Préparer les templates de base (base.html, page.html, section.html)

### Phase 2 – Pages & Collections

- Créer les pages Markdown :
  - Accueil (`_index.md`)
  - Actualités (`actualites/index.md`)
  - Adhésions (`adhesions/index.md`)
  - Horaires (`horaires/index.md`)
  - Staff (`staff/index.md`)
  - Sponsors (`sponsors/index.md`)
- Créer les templates spécifiques pour chaque type de page
- Configurer DecapCMS (`config.yml`) avec une collection pour chaque page modifiable

### Phase 3 – Interactivité & Responsive

- Intégrer Alpine.js pour l’interactivité (menu, transitions, etc.)
- Vérifier la compatibilité mobile et l’accessibilité (WCAG 2.1 AA)
- Ajouter les messages informatifs pour les collections vides

### Phase 4 – Qualité & Automatisation

- Mettre en place Husky, Prettier, Markdownlint, BATS
- Configurer les hooks et scripts de vérification
- Ajouter les tests d’accessibilité et de build

### Phase 5 – Déploiement & Recette

- Vérifier la publication via DecapCMS (GitHub OAuth)
- Tester la rapidité de publication (<2 min)
- Vérifier le build et le déploiement Netlify
- Valider la conformité aux critères de succès

---

## 3. Points d’attention

- Authentification admin uniquement via GitHub OAuth
- Collections DecapCMS distinctes et bien configurées
- Images optimisées et alt text systématique
- Messages d’erreur explicites et non techniques
- Accessibilité et responsive systématiquement testés
- Documentation et conventions à jour

---

## 4. Livrables

- Pages et templates fonctionnels
- Configuration DecapCMS complète
- Style et palette cohérents
- Tests et automatisation opérationnels
- Documentation à jour

---

## 5. Gouvernance

- Revue de code obligatoire pour toute PR
- Validation automatique via CI/CD
- Respect des conventions et constitution du projet
- Mise à jour du plan à chaque évolution majeure
