-- database reset
drop table inspection_receiver_numbers;
drop table inspection_purchase_orders;
drop table employee_projects;
drop table characteristics;
drop table gauges;
drop table inspection_reports;
drop table parts;
drop table machines;
drop table employees;
drop table locations;
drop table departments;
drop table projects;
drop table receiver_numbers;
drop table purchase_orders;
drop table job_orders;
drop table project_types;
drop table specification_types;
drop table characteristic_types;
drop table gauge_types;
drop table machine_types;
drop table location_types;
drop table disposition_types;

-- enumeration tables

create table disposition_types
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_disposition_types primary key (id),
    constraint uc_disposition_types unique (id)
);
-- pass, fail, rework...

create table location_types
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_location_types primary key (id),
    constraint uc_location_types unique (id)
);
-- work station, machine pad, conference room, wfh, main entry

create table machine_types
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_machine_types primary key (id),
    constraint uc_machine_types unique (id)
);
-- cnc machine, drill press, filament winder, label laser...

create table gauge_types
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_gauge_types primary key (id),
    constraint uc_gauge_types unique (id)
);
-- caliper, bore micrometer, indicator, cmm, vision system...

create table characteristic_types
(
    id varchar(32) not null,
    is_gdt boolean not null,

    -- primary key and unique constraints
    constraint pk_characteristic_types primary key (id),
    constraint uc_characteristic_types unique (id)
);
-- diameter, distance, circularity, position, surface profile...

create table specification_types
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_specification_types primary key (id),
    constraint uc_specification_types unique (id)
);
-- upper tailed, lower tailed, two tailed, no tailed

create table project_types
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_project_types primary key (id),
    constraint uc_project_types unique (id)
);

-- record tables

create table job_orders
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_job_orders primary key (id),
    constraint uc_job_orders unique (id)
);

create table purchase_orders
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_purchase_orders primary key (id),
    constraint uc_purchase_orders unique (id)
);

create table receiver_numbers
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_receiver_numbers primary key (id),
    constraint uc_receiver_numbers unique (id)
);

create table projects
(
    id varchar(32) not null,
    description varchar(128),
    day_started date not null,
    day_finished date,

    -- primary key and unique constraints
    constraint pk_projects primary key (id),
    constraint uc_projects unique (id),

    -- many projects relates to one project type
    project_type varchar(32) not null,
    constraint fk_project_type foreign key (project_type) references project_types(id)
);

create table departments
(
    id varchar(32) not null,
    description varchar(128) not null,

    -- primary key and unique constraints
    constraint pk_departments primary key (id),
    constraint uc_departments unique (id)
);
-- manufacturing engineering, marketing, new product development, cnc, welding, fabrication...

create table locations
(
    id varchar(32) not null,
    description varchar(128) not null,

    -- primary key and unique constraint
    constraint pk_locations primary key (id),
    constraint uc_locations unique (id),

    -- one location relates to one location type
    location_type_id varchar(32) not null,
    constraint fk_location_type foreign key (location_type_id) references location_types(id)
);
-- john doe's work station, machine pad for NKZ, conference room AB12...

create table employees
(
    id integer not null,
    first_name varchar(32) not null,
    last_name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_employees primary key (id),
    constraint uc_employees unique (id),

    -- one employee relates to one department
    department_id varchar(32) not null,
    constraint fk_employee_department foreign key (department_id) references departments(id),

    -- one employee relates to one location
    location_id varchar(32) not null,
    constraint fk_employee_location foreign key (location_id) references locations(id),

    -- first and last name combination is unique
    constraint uc_employee_name unique (first_name, last_name)
);
-- all the employees

create table machines
(
    id varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_machines primary key (id),
    constraint uc_machines unique (id),

    -- one machine relates to one machine type
    machine_type_id varchar(32) not null,
    constraint fk_machine_type foreign key (machine_type_id) references machine_types(id),

    -- one machine relates to one location
    machine_location_id varchar(32) not null,
    constraint fk_machine_location foreign key (machine_location_id) references locations(id)
);
-- all the machines for manufacturing and organization

create table parts
(
    id serial not null,
    drawing varchar(32) not null,
    revision varchar(2) not null,
    item varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_parts_id primary key (id),
    constraint uc_parts_id unique (id),

    -- part identifiers are unique
    constraint uc_parts unique (drawing, revision, item)
);

create table inspection_reports
(
    id integer not null,
    day_started date not null,
    day_finished date,

    -- primary key and unique constraints
    constraint pk_inspection_reports primary key (id),
    constraint uc_inspection_reports unique (id),

    -- one inspection report can relate to one job order
    job_order_id varchar(32),
    constraint fk_job_order_ins foreign key (job_order_id) references job_orders(id),

    -- one inspection report can relate to one employee
    employee_id integer,
    constraint fk_employee_ins foreign key (employee_id) references employees(id),

    -- one inspection report relates to one disposition type
    disposition varchar(32) not null,
    constraint fk_disposition_ins foreign key (disposition) references disposition_types(id),

    -- many inspection reports relate to one part
    part_id integer not null,
    constraint fk_part_id foreign key (part_id) references parts(id)
);

create table gauges
(
    id varchar(32) not null,
    last_calibrated date not null,

    -- primary key and unique constraints
    constraint pk_gauges primary key (id),
    constraint uc_gauges unique (id),

    -- one gauge relates to one gauge type
    gauge_type_id varchar(32) not null,
    constraint fk_gauge_type foreign key (gauge_type_id) references gauge_types(id),

    -- one gauge can relate to one employee
    employee_id integer,
    constraint fk_employee_gauge foreign key (employee_id) references employees(id),

    -- one gauge can relate to one location
    location_id varchar(32),
    constraint fk_location_gauge foreign key (location_id) references locations(id)
);

create table characteristics
(
    id serial not null,
    name varchar(32) not null,
    nominal decimal not null,
    usl decimal not null,
    lsl decimal not null,
    precision integer not null,
    measured decimal,

    -- primary key and unique constraints
    constraint pk_characteristics primary key (id),
    constraint uc_characteristics unique (id),

    -- one characteristic relates to one specification type
    specification_type_id varchar(32) not null,
    constraint fk_specification_type_id foreign key (specification_type_id) references specification_types(id),

    -- one characteristic relates to one characteristic type
    characteristic_type_id varchar(32) not null,
    constraint fk_characteristic_type_id foreign key (characteristic_type_id) references characteristic_types(id),

    -- one characteristic can relate to one employee
    employee_id integer,
    constraint fk_employee_char foreign key (employee_id) references employees(id),

    -- many characteristics can relate to one part
    part_id integer not null,
    constraint fk_part_id foreign key (part_id) references parts(id),

    -- one characteristic relates to one gauge
    gauge_id varchar(32) not null,
    constraint fk_gauge_id foreign key (gauge_id) references gauges(id)
);

-- linking tables

create table employee_projects
(
    id serial not null unique,
    employee_id integer not null references employees(id) on update cascade,
    project_id varchar(32) not null references projects(id) on update cascade,
    constraint pk_employee_project primary key (id),
    constraint uc_employee_project unique (employee_id, project_id)
);

create table inspection_purchase_orders
(
    id serial not null unique,
    inspection_id integer not null references inspection_reports(id) on update cascade,
    purchase_order_id varchar(32) not null references purchase_orders(id) on update cascade,
    constraint pk_inspection_purchase_orders primary key (id),
    constraint uc_inspection_purchase_orders unique (inspection_id, purchase_order_id)
);

create table inspection_receiver_numbers
(
    id serial not null unique,
    inspection_id integer not null references inspection_reports(id) on update cascade,
    receiver_number_id varchar(32) not null references receiver_numbers(id) on update cascade,
    constraint pk_inspection_receiver_numbers primary key (id),
    constraint uc_inspection_receiver_numbers unique (inspection_id, receiver_number_id)
);