-- create an enumeration table for direction types
create table dir_types
(
	id int not null unique,
	dir_type char(2) not null unique,
	constraint dir_types_pk primary key (id)
);

-- create a table for fixtures
create table fixtures
(
	id varchar(20) not null unique,
	py float not null,
	px float not null,
	ny float not null,
	nx float not null,
	developer_notes text,
	operator_notes text,
	anchor_dir int foreign key references dir_types(id),
	anchor_val float not null,
	constraint fixtures_pk primary key (id)
);

-- create a table for parts
create table parts
(
	id varchar(20) not null unique,
	py float not null,
	px float not null,
	ny float not null,
	nx float not null,
	revision varchar(10) not null,
	item varchar(30) not null,
	developer_notes text,
	operator_notes text,
	constraint parts_pk primary key (id)
);

-- create a table for programs
create table programs
(
	id int not null unique,
	py float not null,
	px float not null,
	ny float not null,
	nx float not null,
	name varchar(30) not null unique,
	part varchar(20) foreign key references parts(id),
	fixture varchar(20) foreign key references fixtures(id),
	developer_notes text,
	operator_notes text,
	requires_attn bit not null,
	requires_proof bit not null,
	start_date date not null,
	finish_date date,
	constraint programs_pk primary key (id)
);