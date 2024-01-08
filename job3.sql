-- 1. Créez une requête permettant d’afficher toutes les colonnes de la table students.
SELECT * from students;

-- 2. Créez une requête permettant de filtrer la table et d’afficher les élèves âgés de strictement plus de 20 ans.
SELECT * from students WHERE age > 20;

-- 3. Créez une requête permettant de faire un classement des élèves selon leur note dans un ordre croissant, puis dans un ordre décroissant.
SELECT * from students ORDER BY grade ASC; SELECT * from students ORDER BY grade DESC;