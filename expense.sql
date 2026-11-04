create database expense_db;
use expense_db;

create table expenses(
id INT NOT NULL auto_increment,
amount decimal(10,2),
category varchar(50),
description varchar(50),
primary key (id)
);
select * from expenses;

INSERT into expenses(amount,category,description)
values(500.00,'food','lunch');
INSERT into expenses(amount,category,description)
values(700.00,'shop','cake');

SELECT SUM(amount) AS total_spendings
FROM expenses;