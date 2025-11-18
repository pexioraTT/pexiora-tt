module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "type-enum": [
      2,
      "always",
      [
        "feat", // Nouvelle fonctionnalité
        "fix", // Correction de bug
        "docs", // Documentation
        "style", // Formatage, point-virgule manquant, etc.
        "refactor", // Refactoring
        "test", // Ajout de tests
        "chore", // Maintenance, mise à jour des dépendances
        "perf", // Amélioration des performances
        "ci", // Changements CI/CD
        "build", // Changements build system
        "revert", // Annulation d'un commit précédent
      ],
    ],
    "subject-max-length": [2, "always", 72],
    "body-max-line-length": [2, "always", 100],
  },
};
