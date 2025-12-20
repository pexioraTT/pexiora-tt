# Instructions GitHub Copilot pour Pexiora TT

## 🎯 Vue d'ensemble du projet

Ce projet est un site web statique construit avec **Zola**, un générateur de site statique rapide écrit en Rust. Le site utilise les technologies modernes suivantes :

### 🛠️ Stack technique

- **Zola** : Générateur de site statique principal (Rust)
- **Alpine.js** : Framework JavaScript léger pour les interactions côté client
- **Bulma** : Framework CSS moderne et responsive
- **DecapCMS** : Interface d'administration pour la gestion de contenu
- **Netlify** : Plateforme de déploiement et d'hébergement
- **Lefthook** : Hooks Git rapides et parallélisés
- **Prettier** : Formatage automatique du code
- **Bun** : Exécuteur rapide pour scripts et CLIs
- **BATS** : Tests automatisés de l'infrastructure
- **Commitizen** : Standardisation des messages de commit

### 📁 Structure du projet

```
pexiora-tt/
├── source/                  # Dossier source principal Zola
│   ├── config.toml         # Configuration principale de Zola
│   ├── netlify.toml        # Configuration Netlify (build, redirections)
│   ├── content/            # Contenu du site (Markdown)
│   │   └── _index.md      # Page d'accueil
│   ├── templates/         # Templates Zola (HTML + Tera)
│   │   ├── base.html     # Template de base avec Bulma
│   │   ├── index.html    # Template d'accueil avec Alpine.js
│   │   ├── page.html     # Template pour les pages
│   │   ├── section.html  # Template pour les sections
│   │   └── feed.xml      # Template RSS
│   └── static/           # Fichiers statiques
│       ├── admin/        # Configuration DecapCMS
│       │   ├── config.yml # Config CMS
│       │   └── index.html # Interface admin
│       ├── style.css     # CSS personnalisé avec variables Bulma
│       └── favicon.svg   # Icônes et assets
├── public/               # Site généré par Zola (ignoré par git)
├── justfile              # Commandes d'automatisation (dev, build, lint)
├── package.json          # Dépendances Js
├── .envrc                # Configuration direnv (environnement automatique)
├── lefthook.yml          # Hooks Git
├── .prettierrc.json         # Configuration Linter
├── .prettierignore          # Configuration Linter
├── tests/                # Tests BATS pour l'infrastructure
└── .github/
    └── workflows/        # GitHub Actions (CI/CD)
```

## 🎨 Guidelines de développement

### Langage de template : Tera

Zola utilise le moteur de template **Tera** (similaire à Jinja2). Syntaxe principale :

- Variables : `{{ variable }}`
- Blocs : `{% block name %}...{% endblock %}`
- Conditions : `{% if condition %}...{% endif %}`
- Boucles : `{% for item in items %}...{% endfor %}`
- Filtres : `{{ text | upper }}`

### Front Matter (TOML)

Les fichiers Markdown utilisent le front matter TOML :

```toml
+++
title = "Titre de la page"
description = "Description pour le SEO"
date = 2024-01-01
[extra]
image = "images/uploads/devoc.png"
site = "https://www.dev-oc.fr/"
+++
```

### Alpine.js

Utiliser Alpine.js pour les interactions JavaScript :

- `x-data` : Données réactives
- `x-show` : Affichage conditionnel
- `x-if` : Rendu conditionnel
- `@click` : Gestion d'événements
- `x-transition` : Animations

### Bulma CSS

Framework CSS moderne avec système de grille et composants :

- Classes utilitaires : `.is-primary`, `.has-text-centered`
- Système de grille responsive : `.columns`, `.column`
- Composants : `.navbar`, `.card`, `.button`, `.notification`
- Modifiers : `.is-large`, `.is-success`, `.is-outlined`
- Variables CSS personnalisées dans `style.css` pour étendre Bulma

### Qualité du code

Hooks Git automatiques configurés grace a Lefthook.

Commande manuelle disponible :

- `bun run lint` : Vérification complète
- `bun run format` : Correction automatique
- `bun run dev` : Netlify dev
- `bun run build` : Build Zola depuis source/

## 📋 Commandes disponibles (Just)

Utiliser `just` pour les tâches courantes :

- `just dev` : Serveur de développement avec Netlify Dev
- `just build` : Construire le site pour production
- `just check` : Vérifier la configuration Zola
- `just lint` : Vérifications (lint)
- `just format` : Correction automatique (format)
- `just test` : Tests BATS automatisés
- `just clean` : Nettoyage des builds
- `just clean-all` : Nettoyage complet (inclut node_modules)
- `just update-template` : Mise à jour du template avec cruft
- `just check-updates` : Vérifier les mises à jour du template

## 🎯 Conventions de code

### Fichiers Markdown

- Utiliser le front matter TOML complet
- Titre H1 uniquement dans le contenu, pas dans le front matter
- Images dans `static/uploads/` ou `static/images/`
- Alt text obligatoire pour les images

### Templates HTML

- Hériter de `base.html`
- Utiliser la structure sémantique HTML5
- Intégrer Alpine.js pour l'interactivité
- Optimiser pour l'accessibilité (ARIA, alt, etc.)
- Utiliser les classes Bulma pour le style

### CSS

- Étendre Bulma plutôt que le remplacer
- Utiliser les variables CSS personnalisées
- Mobile-first approach avec Bulma responsive
- Préfixer les classes personnalisées avec un namespace

### JavaScript (Alpine.js)

- Logique dans `x-data`
- Éviter la manipulation directe du DOM
- Préférer les directives Alpine.js
- Code réactif et déclaratif
- Utiliser les transitions Alpine.js pour les animations

## 🔧 Configuration DecapCMS

L'interface d'admin est disponible à `/admin/` avec :

- Authentification via GitHub OAuth (backend GitHub)
- Collections configurées dans `static/admin/config.yml`
- Prévisualisations en temps réel
- Upload d'images automatique

## 🚀 Déploiement

### Netlify

- Build command : `zola build`
- Publish directory : `public`
- Node.js version : 22
- Variables d'environnement configurées

### GitHub Actions

- CI automatique sur push/PR
- Tests de qualité (lint, build, links)
- Déploiement automatique sur merge

## 📱 Responsive Design

Le site est optimisé pour :

- Mobile-first
- Breakpoints Pico.css
- Images responsive
- Typography fluide

## ♿ Accessibilité

Standards respectés :

- WCAG 2.1 AA
- Navigation au clavier
- Screen readers
- Contraste suffisant
- Alt text sur images

## 🔍 SEO

Optimisations intégrées :

- Meta descriptions
- Open Graph
- Twitter Cards
- Sitemap XML
- Flux RSS
- Schema.org (à implémenter)

## 🎪 Bonnes pratiques

### Contenu

- Écrire en Markdown sémantique
- Utiliser les taxonomies (tags, catégories)
- Optimiser les images avant upload
- Metadata complètes

### Performance

- Images optimisées et responsive
- CSS/JS minifiés en production
- Lazy loading des images
- Service Worker (PWA optionnel)

### Sécurité

- Headers de sécurité via Netlify
- HTTPS forcé
- Pas de données sensibles en front
- Validation des inputs CMS

## 🆘 Dépannage courant

### Erreurs de build Zola

- Vérifier la syntaxe TOML du front matter
- Vérifier les références de templates
- Contrôler les liens internes
- Valider la structure des dossiers

### Problèmes Alpine.js

- Vérifier la syntaxe des directives
- Contrôler l'ordre de chargement des scripts
- Débugger avec `x-data` et `$inspect`

### Issues DecapCMS

- Vérifier la configuration YAML
- Contrôler l'authentification Netlify
- Valider les permissions de fichiers

---

💡 **Conseil** : Utilisez `just health` pour vérifier l'état de votre environnement de développement et `just --list` pour voir toutes les commandes disponibles.
