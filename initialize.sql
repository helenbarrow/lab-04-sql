CREATE TABLE users(
	user_id INT PRIMARY KEY,
	username VARCHAR(50),
	email VARCHAR(100),
	created_at DATETIME
);

CREATE TABLE posts (
	post_id INT PRIMARY KEY,
	user_id INT,
	title VARCHAR(100),
	content TEXT,
	created_at DATETIME,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email, created_at)
VALUES(1, 'alice', 'alice@example.com', '2026-01-01 10:00:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(2, 'helen', 'helen@example.com', '2026-01-02 10:01:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(3, 'bob', 'bob@example.com', '2026-01-03 10:02:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(4, 'kensington', 'kensington@example.com', '2026-01-04 10:03:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(5, 'braden', 'braden@example.com', '2026-01-05 10:04:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(6, 'colton', 'colton@example.com', '2026-01-06 10:05:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(7, 'ansley', 'ansley@example.com', '2026-01-07 10:06:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(8, 'laura', 'laura@example.com', '2026-01-08 10:07:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(9, 'olivia', 'olivia@example.com', '2026-01-09 10:08:00');

INSERT INTO users (user_id, username, email, created_at)
VALUES(10, 'analucia', 'analucia@example.com', '2026-01-10 10:09:00');



INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (1, 1, 'First Post', 'Hello World!', '2026-09-01 11:00:00');

INSERT INTO posts (post_id, user_id, title, content, created_at)
VALUES (2, 2, 'Second Post', 'Good Morning!', '2026-09-02 11:01:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (3, 3, 'Third Post', 'Good Afternoon!', '2026-09-03 11:02:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (4, 4, 'Fourth Post', 'Good Evening!', '2026-09-04 11:03:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (5, 5, 'Fifth Post', 'Good Night!', '2026-09-05 11:04:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (6, 6, 'Sixth Post', 'Happy Thanksgiving!', '2026-09-06 11:05:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (7, 7, 'Seventh Post', 'Merry Christmas!', '2026-09-07 11:06:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (8, 8, 'Eigth Post', 'Happy Easter!', '2026-09-08 11:07:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (9, 9, 'Ninth Post', 'Happy Fourth of July!', '2026-09-09 11:08:00');

INSERT INTO posts (post_id, user_id, title, content, created_at) 
VALUES (10, 10, 'Tenth Post', 'School's Starting!', '2026-09-10 11:09:00');

