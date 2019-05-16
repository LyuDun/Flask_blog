
# 常用sql

```SQL
drop database if exists database_name;
create database database_name default charset utf-8 collate utf8_bin
use database_name
create table tab_new like tab_old
create table table_new as select col1,col2... from tab_old definition only
drop table table_name
alter table table_name add column column_name type
alter table table_name add primary key(col)
alter table table_name drop primary key
create [unique] index index_name on table_name
drop index index_name
create view view_name as select ...
drop view view_name
select * from table_name where ......
insert into table_name(field1,field2) values(......)
update table_name set field_name = value1 where 
select * from table_name order by ...[desc]
select count as totalcount from table_name
select avg() as sumvalue from table_name
select ... from a where a IN (select ... from table_name)

多表查询
select table1.xx, table2.xx from table1 join table2 where table1.xx = table2.xx

外联
select a.name b.name from  a left join b on a.xx = b.xx
select a.name b.name from a rifht join b on b.xx = a.xx

```