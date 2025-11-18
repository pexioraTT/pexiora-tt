# Justfile pour Pexiora TT
# Documentation: https://github.com/casey/just


# Couleurs pour les messages
RED := '\033[0;31m'
GREEN := '\033[0;32m'
YELLOW := '\033[0;33m'
BLUE := '\033[0;34m'
NC := '\033[0m' # No Color

# Afficher l'aide par défaut
default:
    @just --list

# Démarrer avec netlify dev (recommandé pour tester les fonctions Netlify)
[working-directory: 'source']
dev:
    @echo -e "{{GREEN}}🌐 Démarrage avec Netlify Dev...{{NC}}"
    netlify dev

# 🔨 Construction
# Construire le site pour la production
[working-directory: 'source']
build:
    @echo -e "{{BLUE}}🔨 Construction du site...{{NC}}"
    zola build


# Verifier le site
[working-directory: 'source']
check:
    @echo -e "{{BLUE}}🔨 Vérification du site...{{NC}}"
    zola check --skip-external-links
    @echo -e "{{GREEN}}✅ Vérification terminée avec succès{{NC}}"

# Linting
# Vérifier la qualité du code
lint:
    @echo -e "{{BLUE}} Exécution du Linter...{{NC}}"
    npm run lint
    @echo -e "{{GREEN}}✅ Linting terminé avec succès{{NC}}"

# 🧪 Tests avec BATS
# Exécuter tous les tests automatisés
test:
    @echo -e "{{BLUE}}🧪 Exécution des tests BATS...{{NC}}"
    bats tests/basic.bats
    @echo -e "{{GREEN}}✅ Tous les tests sont passés{{NC}}"

# 🧹 Nettoyage
# Nettoyer les fichiers de build
clean:
    @echo -e "{{YELLOW}}🧹 Nettoyage...{{NC}}"
    rm -rf public/
    rm -rf .sass-cache/

# Nettoyage complet (inclut node_modules si présent)
clean-all: clean
    @echo -e "{{YELLOW}}🧹 Nettoyage complet...{{NC}}"
    rm -rf node_modules/
    rm -rf .netlify/

# 🔧 Maintenance
# Mise à jour du template avec cruft
update-template:
    @echo -e "{{BLUE}}🔄 Mise à jour du template avec cruft...{{NC}}"
    @if command -v cruft >/dev/null 2>&1; then \
        cruft update; \
    else \
        echo -e "{{RED}}❌ cruft non installé. Installez-le avec : pipx install cruft{{NC}}"; \
    fi

# Vérifier les mises à jour disponibles
check-updates:
    @echo -e "{{BLUE}}🔍 Vérification des mises à jour...{{NC}}"
    @if command -v cruft >/dev/null 2>&1; then \
        cruft check; \
    else \
        echo -e "{{RED}}❌ cruft non installé{{NC}}"; \
    fi

