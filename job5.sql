-- 1. Créez une requête permettant d’afficher les pays dont la population est supérieure à celle de "Russia".
SELECT * FROM world WHERE population > (SELECT population FROM world WHERE name = "Russia");

-- 2. Créez une requête permettant d’afficher les pays d'Europe dont le PIB par habitant est supérieur à celui d’ "Italy".
SELECT * from world WHERE GDP/population > (SELECT GDP/population FROM world WHERE name = "Italy");

-- 3. Créez une requête permettant d’afficher les pays dont la population est supérieure à celle du Royaume-Uni mais inférieure à celle de l'Allemagne.
SELECT * from world WHERE poputation > (SELECT population from world WHERE population = 'Royaume-Unis')  AND population < (SELECT population from world WHERE name = "Allemagne");

-- 4. L'Allemagne (80 millions d'habitants) est le pays le plus peuplé d'Europe. L'Autriche (8,5 millions d'habitants) compte 11% de la population allemande.
-- Créez une requête permettant d’afficher le nom et la population de chaque pays d'Europe, en pourcentage de la population de l'Allemagne. 
SELECT name, CONCAT(ROUND((population / (SELECT population FROM countries WHERE name = 'Germany')) * 100), '%') AS pourcentage FROM countries WHERE continent = 'Europe';

-- 5. Créez une requête permettant de trouver le plus grand pays de chaque continent, en indiquant son continent, son nom et sa superficie.
SELECT continent, name, surfacearea FROM world WHERE surfacearea = (SELECT MAX(surfacearea) FROM world GROUP BY continent);

-- 6. Créez une requête permettant de trouver les continents où tous les pays ont une population inférieure ou égale à 25 000 000.
SELECT continent FROM world WHERE population <= 25000000;
