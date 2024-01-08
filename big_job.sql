-- 1. Vous récupérez les données d’intérêt ici. Vous avez à votre disposition un dataset composé de deux tables, Country et World. Elles recensent le pourcentage d'utilisation de différentes sources d’énergie (charbon, gaz, pétrole, nucléaire, ...) en 2015 pour la production d’électricité par pays dans la table Country, puis par région du monde dans la table World.

-- 2. Créez la base de données CarbonFootprint, puis les tables Country et World.

-- 3. Utilisez des requêtes SQL afin d’analyser les données recueillies et tirez un maximum d’informations sur les émissions en carbone. Qu’est ce que vous observez ? 

J'observe dans un premier temps qu'il y a 4 pays, Albania, Congo, Nepal et Paraguay qui ont 100% de leur énergie produite par l'hydroélectrique. Suite à cela il y a 7 autres pays qui ont 90%+ de leur énergié produite par l'hydroélectrique.

En ce qui concerne les autres sources d'énergie il y a 4 pays qui ont 90%+ de leur énergie produite par le charbon. 

Il y a 4 pays qui ont 100%+ de leur énergie produite par le Gaz et 9 qui sont à 90%+. 

Pour le pétrole il y a 3 pays à 100% et 7 à 90%+. 

Par contre, pour l'énergie renouvelable et l'énergie nucléaire le maximum est de 78% pour la France (énergie nucléaire) et 56% pour l'énergie renouvelable (Denmark). 

On peut donc déjà remarqué que l'énergie nucléaire et l'énergie renouvelable sont moins utilisé en tant que source principale d'énergié comparé aux autres sources d'énergie. On remarque aussi que l'énergie qui represente globalement le % le plus élevé est le Gaz qui représente tout de même 90%+ de la production énergétique dans 13 pays. Comparé à 11 pour l'hydroélectrique, 4 pour le charbon et 10 pour le pétrole. 

En ce qui concerne productions énergétiques dans le monde on remarque que le charbon est la source d'énergie la plus utilisé avec 41% de la production énergétique mondiale. Ensuite vient le gaz avec 22%, le pétrole avec 21%, l'hydroélectrique avec 16%, l'énergie nucléaire avec 11% et l'énergie renouvelable avec 6%.

Le continent ou on remarque la plus grosse différence est l'Asie avec 61% de l'énergie qui provient du charbon pour l'Est et 66% pour le Sud. Au Moyen-Orient et en Afrique du Nord l'énergie la plus utilisée est le Gaz avec 64% de source d'énergie. Il y a ensuite des continents un peu plus équilibrés comme L'Europe 24/24/1/17/11/22. 

Sachant que le charbon est la source d'énergie la plus utilisé dans le monde, on peut donc en déduire que c'est aussi la source d'énergie qui pollue le plus. Avec plus de 60% de présence en Asie de l'est et Asie du sud on peut donc déterminé qu'il s'agit de la région qui pollue le plus. 


-- 9. Calculez et affichez l’émission totale annuelle pour un pays (toujours depuis une selection box). On définit la formule permettant de calculer cette valeur comme suit :



-- 10. Pour finir, en sachant qu’un arbre absorbe environ 25 kg de CO2 par an, affichez le nombre nécessaire d’arbres à planter afin d’absorber le CO2 engendré par un pays (sélectionné depuis la selection box, et oui) durant la production d’électricité.

