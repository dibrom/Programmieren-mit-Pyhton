CREATE TABLE traindata (
 #id int,
 X float,
 `Y1 (Training Funktion)` float,
 `Y2 (Training Funktion)` float,
 `Y3 (Training Funktion)` float,
 `Y4 (Training Funktion)` float);
 

 CREATE TABLE testdata (
 #id int,
 `X (Test Funktion)` float,
 `Y1 (Test Funktion)` float,
 `Delta Y (Abweichung)` float,
 `Nummer der idealen Funktion` char(100));
 
 
 CREATE TABLE idealdata (
# id int,
`X (Test Funktion)`  float,
`Y1 (Ideale Funktion)`  float,
`Y2 (Ideale Funktion)`  float,
`Y3 (Ideale Funktion)`  float,
`Y4 (Ideale Funktion)`  float,
`Y5 (Ideale Funktion)`  float,
`Y6 (Ideale Funktion)`  float,
`Y7 (Ideale Funktion)`  float,
`Y8 (Ideale Funktion)`  float,
`Y9 (Ideale Funktion)`  float,
`Y10 (Ideale Funktion)` float,
`Y11 (Ideale Funktion)` float,
`Y12 (Ideale Funktion)` float,
`Y13 (Ideale Funktion)` float,
`Y14 (Ideale Funktion)` float,
`Y15 (Ideale Funktion)` float,
`Y16 (Ideale Funktion)` float,
`Y17 (Ideale Funktion)` float,
`Y18 (Ideale Funktion)` float,
`Y19 (Ideale Funktion)` float,
`Y20 (Ideale Funktion)` float,
`Y21 (Ideale Funktion)` float,
`Y22 (Ideale Funktion)` float,
`Y23 (Ideale Funktion)` float,
`Y24 (Ideale Funktion)` float,
`Y25 (Ideale Funktion)` float,
`Y26 (Ideale Funktion)` float,
`Y27 (Ideale Funktion)` float,
`Y28 (Ideale Funktion)` float,
`Y29 (Ideale Funktion)` float,
`Y30 (Ideale Funktion)` float,
`Y31 (Ideale Funktion)` float,
`Y32 (Ideale Funktion)` float,
`Y33 (Ideale Funktion)` float,
`Y34 (Ideale Funktion)` float,
`Y35 (Ideale Funktion)` float,
`Y36 (Ideale Funktion)` float,
`Y37 (Ideale Funktion)` float,
`Y38 (Ideale Funktion)` float,
`Y39 (Ideale Funktion)` float,
`Y40 (Ideale Funktion)` float,
`Y41 (Ideale Funktion)` float,
`Y42 (Ideale Funktion)` float,
`Y43 (Ideale Funktion)` float,
`Y44 (Ideale Funktion)` float,
`Y45 (Ideale Funktion)` float,
`Y46 (Ideale Funktion)` float,
`Y47 (Ideale Funktion)` float,
`Y48 (Ideale Funktion)` float,
`Y49 (Ideale Funktion)` float,
`Y50 (Ideale Funktion)` float
 );
 
 /*
ALTER TABLE `pmp`.`traindata` 
CHANGE COLUMN `id` `id` INT NOT NULL ,
ADD PRIMARY KEY (`id`);
*/

 /*
 ALTER TABLE `pmp`.`testdata` 
CHANGE COLUMN `id` `id` INT NOT NULL ,
ADD PRIMARY KEY (`id`);
*/
/*
ALTER TABLE `pmp`.`idealdata` 
CHANGE COLUMN `id` `id` INT NOT NULL ,
ADD PRIMARY KEY (`id`);
*/