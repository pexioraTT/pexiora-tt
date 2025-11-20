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

- [x] T007 Créer la page d’accueil source/content/\_index.md
- [x] T008 Créer la page actualités source/content/actualites/index.md
- [x] T009 Créer la page adhésions source/content/adhesions/index.md
- [x] T010 Créer la page horaires source/content/horaires/index.md
- [x] T011 Créer la page staff source/content/staff/index.md
- [x] T012 Créer la page sponsors source/content/sponsors/index.md
- [x] T013 Créer le template actualités source/templates/actualites.html -> Supprimé, n'est finalement pas pertinent
- [x] T014 Créer le template adhésions source/templates/adhesions.html -> Supprimé, n'est finalement pas pertinent
- [x] T015 Créer le template horaires source/templates/horaires.html -> Supprimé, n'est finalement pas pertinent
- [x] T016 Créer le template staff source/templates/staff.html -> Supprimé, n'est finalement pas pertinent
- [x] T017 Créer le template sponsors source/templates/sponsors.html -> Supprimé, n'est finalement pas pertinent
- [x] T018 Configurer DecapCMS (source/static/admin/config.yml) avec une collection pour chaque page modifiable

## Phase 3 : Interactivité & Responsive

- [x] T019 Intégrer Alpine.js dans base.html pour le menu et transitions
- [x] T020 Vérifier la compatibilité mobile (responsive) sur tous les templates
- [x] T021 Ajouter les messages informatifs pour collections vides dans chaque template
- [x] T022 Vérifier l’accessibilité (WCAG 2.1 AA, ARIA, navigation clavier, contraste, alt text)

## Phase 4 : Qualité & Automatisation

- [x] T023 Mettre en place Husky, Prettier, Markdownlint, BATS (package.json, justfile, .husky/)
- [x] T024 Configurer les hooks et scripts de vérification
- [x] T025 Ajouter les tests d’accessibilité et de build dans tests/

## Phase 5 : Déploiement & Recette

- [x] T026 Vérifier la publication via DecapCMS (GitHub OAuth)
- [x] T027 Tester la rapidité de publication (<2 min)
- [x] T028 Vérifier le build et le déploiement Netlify
- [x] T029 Valider la conformité aux critères de succès
- [x] T030 Vérifier que les images sont optimisées et ont un alt text
- [x] T031 Vérifier que les messages d’erreur sont explicites et non techniques
- [x] T032 Mettre à jour la documentation et conventions
- [x] T033 Rédiger et mettre à jour la documentation utilisateur (README, guides, accessibilité)
- [x] T034 Revue de code obligatoire pour toute PR
- [x] T035 Validation automatique via CI/CD
- [x] T036 Mise à jour du plan à chaque évolution majeure
