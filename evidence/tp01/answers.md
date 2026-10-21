# TP01 - Réponses

## A1
Le CSV c'est la donnée d'entrée, on n'y touche pas et on la repère par sa source et son hash. Le code est versionné dans Git. Le modèle est un résultat qu'on peut régénérer à partir du code et des données. Si on mélange tout, on ne sait plus quel modèle vient de quel code et de quelles données.

## A2
Churn est ce qu'on veut prédire. Si on le met en entrée, le modèle a déjà la réponse : il aura un très bon score en test mais ne servira à rien en vrai, puisqu'on ne connaît pas encore le churn.

## B2
1. Python : `requires-python = ">=3.11,<3.13"`. Dépendance directe : pandas.
2. Dans uv.lock, pandas apparaît avec sa version exacte (3.0.6).
3. scipy est une dépendance transitive (installée à cause de scikit-learn).
4. pyproject.toml dit ce dont le projet a besoin, uv.lock fixe les versions exactes installées, et .venv est l'environnement sur ma machine (pas dans Git, on peut le recréer).

## B3
`~= 1.26.0` accepte les versions de 1.26.0 à 1.27.0 exclu, `== 1.26.4` une seule version. Le lock garde celle qui a été choisie.

## C3
1. La cible a deux valeurs (Yes/No), donc c'est de la classification.
2. Il y a environ 73 % de No. Un modèle qui dit toujours No aurait déjà 73 % d'accuracy, donc il faudra regarder d'autres métriques (rappel, F1...).
3. Il y a 11 valeurs avec seulement des espaces, donc pandas ne peut pas convertir la colonne en nombre et la garde en texte.
4. Une chaîne avec des espaces n'est pas considérée comme une valeur manquante, isna() ne la voit pas.
5. Le même hash SHA-256 (16320c9c...055e91) et les mêmes comptages.

## D2
| Élément | Preuve | Limite |
|---|---|---|
| Code | Commit Git [hash] | Les modifs non commitées ne sont pas prises en compte |
| Paquets | pyproject.toml, uv.lock | L'OS ou la version de Python peuvent changer l'installation |
| Environnement | environment-before.json et environment.json identiques | Ne décrit pas tout le système ni le matériel |
| Données | URL + SHA-256 | Ne garantit pas la qualité des labels |
| Modèle | Pas encore fait | À voir dans les prochains TP |

On a créé nous-mêmes le projet et le uv.lock, avec uv 0.13.4 au lieu de 0.12.23.

## E
PR : https://github.com/uvsqq21916400/churnlab-2026/pull/1
Commit : 741b3cc
Question du binôme : Si je clone ton repo et que je lance uv sync --locked à froid, est-ce que ça marche directement ?
Réponse : Oui, j’ai testé avec un clone neuf. uv sync --locked marche directement : pyproject.toml et uv.lock sont dans le repo, et uv télécharge Python 3.11 s’il manque.
Par contre le CSV n’est pas dans Git (il est ignoré), donc il faut lancer scripts/download_data.py avant inspect_telco.py. Le script vérifie le hash.
Il faut aussi une version de uv récente (j’ai fait le lock avec la 0.13.4), une version trop ancienne risque de ne pas lire le lock.
J’ai précisé ces deux points dans le README (dernier commit).

## F
`git restore` efface la modification du fichier. `git restore --staged` la retire seulement du staging, la modification reste dans le fichier.
