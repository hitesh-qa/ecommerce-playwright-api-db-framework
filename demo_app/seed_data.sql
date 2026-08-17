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

-- seed a few products for the storefront
INSERT INTO products (name, price, stock_quantity) VALUES
('Wireless Mouse', 19.99, 50),
('Mechanical Keyboard', 59.99, 30),
('USB-C Hub', 24.50, 100),
('Laptop Stand', 34.00, 20);