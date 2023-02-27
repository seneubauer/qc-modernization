-- create an enumeration table for direction types
create table dir_types
(
	id int not null unique,
	dir_type char(2) not null unique,
	constraint dir_types_pk primary key (id)
);

-- create an enumeration table for workspace columns
create table workspace_columns
(
	id int not null unique,
	col varchar(3) not null unique,
	constraint col_pk primary key (id)
);

-- create an enumeration table for workspace columns
create table workspace_rows
(
	id int not null unique,
	row int not null unique,
	constraint row_pk primary key (id)
);

-- create an enumeration table for workspace assignment types
create table workspace_assignment_types
(
	id varchar(20) not null unique,
	constraint workspace_assignment_type_pk primary key (id)
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
	last_replaced_date date,
	evaluation float,
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
	item varchar(20) not null,
	developer_notes text,
	operator_notes text,
	constraint parts_pk primary key (id)
);

-- create a table for requested programs
create table requests
(
	id int identity(0, 1) not null unique,
	drawing varchar(20) not null,
	item varchar(20) not null,
	revision varchar(10) not null,
	request_date date not null,
	completed bit not null,
	notes text,
	constraint requests_pk primary key (id)
);

-- create a table for programs
create table programs
(
	py float not null,
	px float not null,
	ny float not null,
	nx float not null,
	name varchar(20) not null unique,
	part varchar(20) foreign key references parts(id),
	fixture varchar(20) foreign key references fixtures(id),
	developer_notes text,
	operator_notes text,
	requires_attn bit not null,
	requires_proof bit not null,
	start_date date not null,
	finish_date date,
	constraint programs_pk primary key (name)
);

-- create a table for the workspace layout groups
create table workspace_layout_groups
(
	id int identity(0, 1) not null unique,
	group_name varchar(30) unique,
	constraint workspace_layout_groups_pk primary key(id)
);

-- create a table for workspace layout assignments
create table workspace_layout_assignments
(
	id int identity(0, 1) not null unique,
	id_type varchar(20) foreign key references workspace_assignment_types(id),
	fixture_id varchar(20) foreign key references fixtures(id),
	part_id varchar(20) foreign key references parts(id),
	program_id varchar(20) foreign key references programs(id),
	anchor_col int foreign key references workspace_columns(id),
	anchor_row int foreign key references workspace_rows(id),
	group_id int foreign key references workspace_layout_groups(id),
);