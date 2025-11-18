#!/usr/bin/env bats

# Tests pour Pexiora TT

@test "Zola peut construire le site" {
    cd source
    run zola build
    [ "$status" -eq 0 ]
}

@test "Le fichier config.toml est valide" {
    [ -f "source/config.toml" ]
    cd source
    run zola check
    [ "$status" -eq 0 ]
}

@test "Les templates HTML existent" {
    [ -f "source/templates/base.html" ]
    [ -f "source/templates/index.html" ]
    [ -f "source/templates/page.html" ]
}

@test "Le contenu principal existe" {
    [ -f "source/content/_index.md" ]
}

@test "Les fichiers statiques existent" {
    [ -f "source/static/style.css" ]
}

@test "Le justfile est fonctionnel" {
    run just --version
    [ "$status" -eq 0 ]

    run just --list
    [ "$status" -eq 0 ]
}

@test "La configuration Netlify est présente" {
    [ -f "source/netlify.toml" ]
}
