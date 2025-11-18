# Liste des tâches – Pexiora TT

**Input** : implementation-plan.md
**Date** : 2025-11-18

---

## Phase 1 : Initialisation & Structure

- [x] T001 Créer la structure des dossiers source/content, source/templates, source/static, tests
- [x] T002 Ajouter le logo source/static/logo.png et favicon source/static/favicon.svg
- [x] T003 [P] Mettre en place le style CSS avec la palette autour de #002a4b dans source/static/style.css
- [x] T004 Créer le template de base source/templates/base.html
- [x] T005 Créer le template de page source/templates/page.html
- [x] T006 Créer le template de section source/templates/section.html

## Phase 2 : Pages & Collections

- [X] T007 Créer la page d’accueil source/content/\_index.md
- [X] T008 Créer la page actualités source/content/actualites/index.md
- [X] T009 Créer la page adhésions source/content/adhesions/index.md
- [X] T010 Créer la page horaires source/content/horaires/index.md
- [X] T011 Créer la page staff source/content/staff/index.md
- [X] T012 Créer la page sponsors source/content/sponsors/index.md
- [X] T013 Créer le template actualités source/templates/actualites.html -> Supprimé, n'est finalement pas pertinent
- [X] T014 Créer le template adhésions source/templates/adhesions.html -> Supprimé, n'est finalement pas pertinent
- [X] T015 Créer le template horaires source/templates/horaires.html -> Supprimé, n'est finalement pas pertinent
- [X] T016 Créer le template staff source/templates/staff.html -> Supprimé, n'est finalement pas pertinent
- [X] T017 Créer le template sponsors source/templates/sponsors.html -> Supprimé, n'est finalement pas pertinent
- [ ] T018 Configurer DecapCMS (source/static/admin/config.yml) avec une collection pour chaque page modifiable

## Phase 3 : Interactivité & Responsive

- [ ] T019 Intégrer Alpine.js dans base.html pour le menu et transitions
- [ ] T020 Vérifier la compatibilité mobile (responsive) sur tous les templates
- [ ] T021 Ajouter les messages informatifs pour collections vides dans chaque template
- [ ] T022 Vérifier l’accessibilité (WCAG 2.1 AA, ARIA, navigation clavier, contraste, alt text)

## Phase 4 : Qualité & Automatisation

- [ ] T023 Mettre en place Husky, Prettier, Markdownlint, BATS (package.json, justfile, .husky/)
- [ ] T024 Configurer les hooks et scripts de vérification
- [ ] T025 Ajouter les tests d’accessibilité et de build dans tests/

## Phase 5 : Déploiement & Recette

- [ ] T026 Vérifier la publication via DecapCMS (GitHub OAuth)
- [ ] T027 Tester la rapidité de publication (<2 min)
- [ ] T028 Vérifier le build et le déploiement Netlify
- [ ] T029 Valider la conformité aux critères de succès
- [ ] T030 Vérifier que les images sont optimisées et ont un alt text
- [ ] T031 Vérifier que les messages d’erreur sont explicites et non techniques
- [ ] T032 Mettre à jour la documentation et conventions
- [ ] T033 Rédiger et mettre à jour la documentation utilisateur (README, guides, accessibilité)
- [ ] T034 Revue de code obligatoire pour toute PR
- [ ] T035 Validation automatique via CI/CD
- [ ] T036 Mise à jour du plan à chaque évolution majeure
