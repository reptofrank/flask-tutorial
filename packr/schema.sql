CREATE TABLE post (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  author_id INT(11) NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR(255) NOT NULL,
  body VARCHAR(255) NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);