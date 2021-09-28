CREATE TYPE status AS ENUM ('active', 'block');

CREATE TABLE users
(
	user_id serial,
	username varchar (128) UNIQUE NOT NULL,
	email varchar (128) UNIQUE NOT NULL,
	password varchar (128) UNIQUE NOT NULL,
	status STATUS DEFAULT 'active',
	apikey varchar (128) UNIQUE NOT NULL,


	CONSTRAINT PK_users_user_id PRIMARY KEY(user_id)
);


CREATE TABLE recipes
(
	recipe_id serial,
	username varchar (128) NOT NULL,
	title varchar (128) NOT NULL,
	description text NOT NULL,
	status STATUS DEFAULT 'active',
	created_at timestamp DEFAULT current_timestamp,

	CONSTRAINT PK_recipe_recipe_id PRIMARY KEY(recipe_id),
	CONSTRAINT FK_recipe_users FOREIGN KEY(username ) REFERENCES users(username )
);


INSERT INTO users (username, email, password, status, apikey)
VALUES
('cary', 'cary@gmail.com', 'cary', 'active', '1b2dc500-2bf6-446c-8603-bd7717826d81'),
('mark', 'mark@gmail.com', 'mark', 'active', '2b2dc500-2bf6-446c-8603-bd7717826d81'),
('dark', 'dark@gmail.com', 'dark', 'active', '3b2dc500-2bf6-446c-8603-bd7717826d81'),
('roy', 'roy@gmail.com', 'roy', 'active', '4b2dc500-2bf6-446c-8603-bd7717826d81'),
('joy', 'joy@gmail.com', 'joy', 'active', '6b2dc500-2bf6-446c-8603-bd7717826d81'),
('kate', 'kate@gmail.com', 'kate', 'active', '7b2dc500-2bf6-446c-8603-bd7717826d81'),
('gate', 'gate@gmail.com', 'gate', 'active', '8b2dc500-2bf6-446c-8603-bd7717826d81'),
('mat', 'mat@gmail.com', 'mat', 'active', '9b2dc500-2bf6-446c-8603-bd7717826d81'),
('leon', 'leon@gmail.com', 'leon', 'active', '10b2dc500-2bf6-446c-8603-bd7717826d81'),
('maks', 'maks@gmail.com', 'maks', 'block', '11b2dc500-2bf6-446c-8603-bd7717826d81'),
('julia', 'julia@gmail.com', 'julia', 'active', '12b2dc500-2bf6-446c-8603-bd7717826d81'),
('veronica', 'veronica@gmail.com', 'veronica', 'active', '13b2dc500-2bf6-446c-8603-bd7717826d81'),
('oliver', 'oliver@gmail.com', 'oliver', 'active', '14b2dc500-2bf6-446c-8603-bd7717826d81'),
('kara', 'kara@gmail.com', 'kara', 'active', '15b2dc500-2bf6-446c-8603-bd7717826d81'),
('sebastian', 'sebastian@gmail.com', 'sebastian', 'active', '16b2dc500-2bf6-446c-8603-bd7717826d81'),
('oleg', 'oleg@gmail.com', 'oleg', 'block', '17b2dc500-2bf6-446c-8603-bd7717826d81'),
('olga', 'olga@gmail.com', 'olga', 'block', '18b2dc500-2bf6-446c-8603-bd7717826d81'),
('ulyana', 'ulyana@gmail.com', 'ulyana', 'active', '20b2dc500-2bf6-446c-8603-bd7717826d81');


INSERT INTO users (username, email, password, status, apikey)
VALUES
('cary', 'cary@gmail.com', 'cary', 'active', '1b2dc500-2bf6-446c-8603-bd7717826d81'),
('mark', 'mark@gmail.com', 'mark', 'active', '2b2dc500-2bf6-446c-8603-bd7717826d81'),
('dark', 'dark@gmail.com', 'dark', 'active', '3b2dc500-2bf6-446c-8603-bd7717826d81'),
('roy', 'roy@gmail.com', 'roy', 'active', '4b2dc500-2bf6-446c-8603-bd7717826d81'),
('joy', 'joy@gmail.com', 'joy', 'active', '6b2dc500-2bf6-446c-8603-bd7717826d81'),
('kate', 'kate@gmail.com', 'kate', 'active', '7b2dc500-2bf6-446c-8603-bd7717826d81'),
('gate', 'gate@gmail.com', 'gate', 'active', '8b2dc500-2bf6-446c-8603-bd7717826d81'),
('mat', 'mat@gmail.com', 'mat', 'active', '9b2dc500-2bf6-446c-8603-bd7717826d81'),
('leon', 'leon@gmail.com', 'leon', 'active', '10b2dc500-2bf6-446c-8603-bd7717826d81'),
('maks', 'maks@gmail.com', 'maks', 'active', '11b2dc500-2bf6-446c-8603-bd7717826d81'),
('julia', 'julia@gmail.com', 'julia', 'active', '12b2dc500-2bf6-446c-8603-bd7717826d81'),
('veronica', 'veronica@gmail.com', 'veronica', 'active', '13b2dc500-2bf6-446c-8603-bd7717826d81'),
('oliver', 'oliver@gmail.com', 'oliver', 'active', '14b2dc500-2bf6-446c-8603-bd7717826d81'),
('kara', 'kara@gmail.com', 'kara', 'active', '15b2dc500-2bf6-446c-8603-bd7717826d81'),
('sebastian', 'sebastian@gmail.com', 'sebastian', 'active', '16b2dc500-2bf6-446c-8603-bd7717826d81'),
('oleg', 'oleg@gmail.com', 'oleg', 'active', '17b2dc500-2bf6-446c-8603-bd7717826d81'),
('olga', 'olga@gmail.com', 'olga', 'active', '18b2dc500-2bf6-446c-8603-bd7717826d81'),
('ulyana', 'ulyana@gmail.com', 'ulyana', 'active', '20b2dc500-2bf6-446c-8603-bd7717826d81');





