create database if not exists emails
;
use emails
;

drop table if exists emails
;
create table emails(
 id int auto_increment primary key,
 email varchar(100),
 created_at datetime not null default current_timestamp,
 updated_at datetime not null default current_timestamp
);

