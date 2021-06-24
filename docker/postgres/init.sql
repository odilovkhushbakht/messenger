create user admin_db with password 'admin_db_password';
alter role admin_db set client_encoding to 'utf8';

create database messenger;
grant all privileges on database messenger to admin_db;