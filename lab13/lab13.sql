.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet
  FROM students
  WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song
  FROM students
  WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students
  GROUP BY smallest HAVING COUNT(smallest) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color
  FROM students as a, students as b
  WHERE a.pet = b.pet AND a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT students.seven
  FROM students, numbers
  WHERE students.time = numbers.time AND students.number = 7 AND numbers.'7' = "True";


CREATE TABLE avg_difference AS
  SELECT ROUND(AVG(ABS(number - smallest)))
  FROM students;

