CREATE TABLE IF NOT EXISTS menu(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS course(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
text TEXT NOT NULL,
price TEXT NOT NULL,
url TEXT NOT NULL,
time INTEGER NOT NULL
);