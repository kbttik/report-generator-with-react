
CREATE SCHEMA IF NOT EXISTS reporter;
USE reporter;

CREATE TABLE IF NOT EXISTS tags
(
  id  INT(10),
  tag VARCHAR(20)
);

INSERT INTO tags (id, tag) VALUES (1, "r");
INSERT INTO tags (id, tag) VALUES (2, "R");

CREATE TABLE IF NOT EXISTS reports
(
  id    INT(10),
  url   VARCHAR(50),
  title VARCHAR(30),
  create_at TIMESTAMP
);
