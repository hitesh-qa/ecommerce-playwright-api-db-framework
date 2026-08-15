--Clear existing data (keeps the schema/tables, resets the rows)
DELETE FROM payments;
DELETE FROM orders;
DELETE FROM products;
DELETE FROM users;

--Reset auto-increment counters so IDs always start fresh at 1
DELETE FROM sqlite_sequence Where name IN('users','products','orders','payments');

--Seed one demo user (id=1 - app.py's DEMO_USER_ID depends on this)
INSERT INTO users (username, email, password) VALUES
('demo_user', 'demo_user@example.com', 'hashed_password_placeholder');
