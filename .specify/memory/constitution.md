<!--
Sync Impact Report
Version change: N/A → 1.0.0
Principes ajoutés : Stack Technique, Qualité & Lint, Documentation & Accessibilité, Workflow & CI/CD, Sécurité & Conformité
Sections ajoutées : Contraintes Techniques, Workflow de Développement, Bonnes pratiques, Dépannage courant
Templates vérifiés : plan-template.md ✅, spec-template.md ✅, tasks-template.md ✅
TODO(RATIFICATION_DATE): Date d’adoption initiale à renseigner
-->

# pexiora-tt Constitution

## Core Principles

### I. Stack Technique et Conventionnelle

Le projet DOIT utiliser Zola, Alpine.js, Bulma, DecapCMS, Netlify, Husky, Prettier, Markdownlint, BATS, Commitizen.
Toute modification de stack ou de structure DOIT être validée par revue et test.
Les conventions de structure de dossier et de nommage DOIVENT être respectées.
Rationale : Cohérence, sécurité, maintenabilité et facilité de contribution.

### II. Qualité & Lint Automatisés

Les hooks Husky DOIVENT être actifs sur tous les commits.
Les scripts lint (`npm run lint`, `just lint`) et tests (`just test`) DOIVENT passer avant tout merge.
Les tests BATS DOIVENT couvrir l’infrastructure critique.
Rationale : Prévenir les régressions et garantir la qualité du code.

### III. Documentation & Accessibilité

Toute fonctionnalité DOIT être documentée dans le README et les fichiers de configuration.
Les templates DOIVENT respecter les standards d’accessibilité (WCAG 2.1 AA, ARIA, alt text, navigation clavier).
Rationale : Faciliter la contribution, l’usage et l’inclusion.

### IV. Workflow & CI/CD Standardisés

### IV. Workflow & CI/CD Standardisés

Les contributions DOIVENT suivre le workflow GitHub Actions et Just.
Les messages de commit DOIVENT respecter Conventional Commits via Commitizen.
La CI/CD DOIT valider lint, build, tests et liens à chaque push/PR.
Rationale : Collaboration fluide, automatisation et qualité continue.

### V. Sécurité & Conformité

HTTPS DOIT être forcé.
Aucune donnée sensible ne DOIT être exposée côté client.
La validation des inputs CMS DOIT être assurée.
Rationale : Protection des utilisateurs et du projet.

## Contraintes Techniques

- Utilisation obligatoire des outils et conventions listés dans le README et `.github/copilot-instructions.md`.
- Respect du front matter TOML complet pour les fichiers Markdown.
- Images dans `static/uploads/` ou `static/images/` avec alt text obligatoire.
- Templates héritent de `base.html`, structure HTML5, Alpine.js pour l’interactivité, Bulma pour le style.
- CSS étend Bulma, mobile-first, variables personnalisées, classes préfixées.
- JavaScript réactif et déclaratif via Alpine.js, transitions pour animations.

## Bonnes pratiques

- Écrire en Markdown sémantique, utiliser taxonomies (tags, catégories).
- Optimiser les images avant upload, metadata complètes.
- CSS/JS minifiés en production, lazy loading des images.
- Service Worker (PWA) optionnel.
- SEO : meta descriptions, Open Graph, Twitter Cards, sitemap XML, flux RSS, Schema.org (à implémenter).

## Dépannage courant

- Vérifier la syntaxe TOML du front matter, références de templates, liens internes, structure des dossiers.
- Alpine.js : vérifier syntaxe des directives, ordre de chargement, débug avec `x-data` et `$inspect`.
- DecapCMS : vérifier configuration YAML, permissions de fichiers.

## Workflow de Développement

- Revue de code obligatoire pour toute PR.
- Validation automatique via GitHub Actions.
- Documentation à jour avant merge.
- Utiliser `just` pour les tâches courantes (dev, build, lint, test, clean, update-template).
- Respecter les standards de code, hooks pre-commit, tests passants, documentation mise à jour, code reviews.

## Governance

La constitution prévaut sur toute autre pratique.
Toute modification nécessite documentation, validation en PR, et migration planifiée si breaking change.
La conformité est vérifiée à chaque review et merge.
Versionnement sémantique : MAJOR pour rupture, MINOR pour ajout, PATCH pour clarification.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2025-11-18
