# Pexiora TT

Site web du club de tennis de table de Pexiora

## 🛠️ Technologies utilisées

- **[Zola](https://www.getzola.org/)** - Générateur de site statique rapide et moderne
- **[Alpine.js](https://alpinejs.dev/)** - Framework JavaScript léger pour les interactions
- **[Bulma](https://bulma.io/)** - Framework CSS moderne et responsive
- **[DecapCMS](https://decapcms.org/)** - Interface d'administration pour la gestion de contenu
- **[Netlify](https://www.netlify.com/)** - Plateforme de déploiement et d'hébergement
- **[Lefthook](https://github.com/evilmartians/lefthook)** - Hooks Git rapides et parallélisés
- **[Bun](https://bun.sh/)** - Exécuteur rapide pour scripts et CLIs

## 📋 Prérequis

- **[Zola](https://www.getzola.org/documentation/getting-started/installation/)**
- **[pnpm](https://pnpm.io/)** pour la gestion des paquets
- **[Just](https://github.com/casey/just)** pour l'automatisation des tâches
- **[direnv](https://direnv.net/)** pour la gestion de l'environnement
- **[Bun](https://bun.sh/)** pour exécuter rapidement les scripts (recommandé)

### 🔧 Installation rapide des outils

```bash
brew install zola just direnv nvm pnpm bun
```

## 🚀 Démarrage rapide

### Configurer l'environnement avec direnv

```bash
# Autoriser direnv pour ce projet
direnv allow
```

### Démarrer le serveur de développement

```bash
# Avec Netlify Dev (recommandé - inclut les fonctions Netlify)
just dev
```

### Ouvrir dans le navigateur

- Site : <http://localhost:1111>
- Admin CMS : <http://localhost:1111/admin>

## 📝 Gestion de contenu

### ✏️ Interface d'administration (DecapCMS)

- Accédez à `/admin` pour gérer le contenu
- Authentification via GitHub OAuth (backend GitHub)
- Interface WYSIWYG pour les articles
- Upload d'images intégré

### 📁 Structure des contenus

```
content/
├── _index.md          # Page d'accueil
```

## ⚡ Commandes disponibles

Le projet utilise [Just](https://github.com/casey/just) pour l'automatisation :

```bash
# 🚀 Développement
just dev              # Serveur de développement avec Netlify Dev

# 🔨 Construction
just build            # Construire le site pour production
just check            # Vérifier la configuration Zola

# 🔍 Qualité
just lint             # Vérifications (lint)
just format           # Correcteur (format)
just test             # Tests BATS automatisés

# 🔧 Maintenance
just clean            # Nettoyer les fichiers de build
just clean-all        # Nettoyage complet (inclut node_modules)
just update-template  # Mise à jour du template avec cruft
just check-updates    # Vérifier les mises à jour du template
```

Voir toutes les commandes : `just --list`

## 🎨 Personnalisation

### 🎨 Styles

- CSS personnalisé : `source/static/style.css`
- Variables CSS dans `:root`
- Basé sur Bulma (framework CSS moderne)

### 🧩 Templates

- Templates Zola dans `source/templates/`
- Moteur de template : Tera (syntaxe Jinja-like)
- Alpine.js intégré pour l'interactivité

### ⚙️ Configuration

- Configuration Zola : `source/config.toml`
- Configuration CMS : `source/static/admin/config.yml`
- Configuration Netlify : `source/netlify.toml`

### 🔍 Qualité du code

Ce projet utilise **Lefthook** pour maintenir la qualité du code au commit.
Les commandes suivantes sont mise a disposition pour controlé la qualité également :

```bash
# Installer les hooks git (automatique via script prepare)
bun run prepare

# Lancer les vérifications manuellement
bun run lint

# Corriger automatiquement les problèmes de formatage
bun run format  # Validation contenu (optionnel)

# Commit avec Commitizen (messages standardisés)
bun run commit
```

**Hooks automatiques :**

- **lint** : Lint
- **Commit-messages** : Valide le format des messages de commit

**Outils de qualité :**

- **Prettier** : Lint + format (JS/TS/JSON/CSS/HTML/Markdown)
- **Commitizen** : Messages de commit standardisés (Conventional Commits)
- **Commitlint** : Validation des messages de commit
- **BATS** : Tests automatisés de l'infrastructure

## 🚀 Déploiement

### 🌐 Netlify (recommandé)

- **Configuration automatique** (si vous avez utilisé le bouton "Deploy to Netlify")
  - Le site se déploie automatiquement à chaque push
  - Preview automatique sur les Pull Requests

### ⚙️ Variables d'environnement Netlify

Configurez dans l'interface Netlify :

- `ZOLA_VERSION=0.21.0`

## 🔒 Authentification CMS

DecapCMS utilise désormais l'authentification via GitHub OAuth (backend GitHub).

Pour activer l'authentification :

1. Configurez le backend GitHub dans le fichier `config.yml` de DecapCMS (`source/static/admin/config.yml`).
2. Suivez [la documentation officielle DecapCMS pour la configuration OAuth](https://decapcms.org/docs/github-backend/) :

## 🔧 Développement

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
|   ├── public/           # Site généré par Zola (ignoré par git)
│   └── static/           # Fichiers statiques
│       ├── admin/        # Configuration DecapCMS
│       │   ├── config.yml # Config CMS
│       │   └── index.html # Interface admin
│       ├── style.css     # CSS personnalisé avec variables Bulma
│       └── favicon.svg   # Icônes et assets
├── justfile              # Commandes d'automatisation (dev, build, lint)
├── package.json          # Dépendances Js
├── .envrc                # Configuration direnv (environnement automatique)
├── .prettierrc.json         # Configuration Linter
├── .prettierignore          # Configuration Linter
├── tests/                # Tests BATS pour l'infrastructure
└── .github/
    └── workflows/        # GitHub Actions (CI/CD)
```

### 🧪 Tests et qualité

- **Pre-commit hooks** : Vérifications automatiques avant commit
- **GitHub Actions** : CI/CD complet
- **Linting** : Markdown, YAML, TOML, CSS, JS
- **Tests** : Build, liens, performance, accessibilité

### 🔄 Mise à jour du template

Ce projet utilise [cruft](https://cruft.github.io/cruft/) pour les mises à jour :

```bash
# Vérifier les mises à jour disponibles
just check-updates

# Appliquer les mises à jour
just update-template
```

## 📚 Documentation

- **[Zola Documentation](https://www.getzola.org/documentation/)**
- **[Alpine.js Guide](https://alpinejs.dev/start-here)**
- **[Bulma Documentation](https://bulma.io/documentation/)**
- **[DecapCMS Docs](https://decapcms.org/docs/)**
- **[Netlify Docs](https://docs.netlify.com/)**
- **[pnpm Documentation](https://pnpm.io/)**

## 🐛 Dépannage

### Problèmes courants

**Erreur de build Zola**

```bash
# Vérifier la configuration
zola check

# Vérifier la syntaxe des templates
just lint
```

**Problèmes avec direnv**

```bash
# Recharger la configuration
direnv reload

# Vérifier le statut
direnv status
```

**Erreurs de déploiement Netlify**

- Vérifier les logs dans l'interface Netlify
- Tester le build localement : `just build`

## 🤝 Contribution

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commits avec pre-commit hooks
4. Push et créer une Pull Request

### 📏 Standards de code

- Respect des hooks pre-commit
- Tests passants
- Documentation mise à jour
- Code reviews

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🎯 Template créé avec

Ce site a été créé à partir du template **Zola + Bulma + DecapCMS + Netlify** avec :

- **[Cookiecutter](https://cookiecutter.readthedocs.io/)** pour la génération
- **[Cruft](https://cruft.github.io/cruft/)** pour les mises à jour
- **[Just](https://github.com/casey/just)** pour l'automatisation

### 📦 Créer un nouveau site avec ce template

```bash
# Installer cruft avec uv
uv tool install cruft

# Créer un nouveau site
cruft create https://github.com/Dev-Oc-Collectif/zola-template
```

**Maintenu par** [Dev'Oc](mailto:contact@dev-oc.fr) • **Propulsé par** [Zola](https://www.getzola.org/)
