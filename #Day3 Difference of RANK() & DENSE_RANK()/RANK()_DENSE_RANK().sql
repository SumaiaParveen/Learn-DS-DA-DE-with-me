-- Create a table called 'scores' with two columns: 'name' and 'score'
CREATE TABLE scores
(
  name VARCHAR(255),
  score INTEGER
);

-- Insert five rows into the 'scores' table
INSERT INTO scores (name, score)
VALUES ('Alice', 85),
       ('Bob', 95),
       ('Charlie', 75),
       ('Dave', 95),
       ('Eve', 75);

-- Select the 'name', 'score', and ranks calculated using RANK() and DENSE_RANK()
-- from the 'scores' table, ordered by score in descending order
SELECT name, score,
       RANK() OVER (ORDER BY score DESC) AS rank,
       DENSE_RANK() OVER (ORDER BY score DESC) AS dense_rank
FROM scores;
