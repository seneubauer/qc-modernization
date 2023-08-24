-- database reset
drop table inspections_lot_numbers;
drop table inspections_purchase_orders;
drop table inspections_job_numbers;
drop table employee_projects;
drop table features;
drop table print_features;
drop table inspections;
drop table gauges;
drop table parts;
drop table inspection_records;
drop table machines;
drop table projects;
drop table receiver_numbers;
drop table purchase_orders;
drop table job_numbers;
drop table employees;
drop table locations;
drop table departments;
drop table suppliers;
drop table lot_numbers;
drop table inspection_types;
drop table frequency_types;
drop table material_types;
drop table project_types;
drop table specification_types;
drop table dimension_types;
drop table gauge_types;
drop table machine_types;
drop table location_types;
drop table disposition_types;
drop table operation_types;

-- enumeration tables

create table operation_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_operation_types primary key (id),
    constraint uc_operation_types unique (id)
);

create table disposition_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_disposition_types primary key (id),
    constraint uc_disposition_types unique (id)
);

create table location_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_location_types primary key (id),
    constraint uc_location_types unique (id)
);

create table machine_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_machine_types primary key (id),
    constraint uc_machine_types unique (id)
);

create table gauge_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_gauge_types primary key (id),
    constraint uc_gauge_types unique (id)
);

create table dimension_types
(
    id integer not null,
    name varchar(32) not null,
    is_gdt boolean not null,

    -- primary key and unique constraints
    constraint pk_dimension_types primary key (id),
    constraint uc_dimension_types unique (id)
);

create table specification_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_specification_types primary key (id),
    constraint uc_specification_types unique (id)
);

create table project_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_project_types primary key (id),
    constraint uc_project_types unique (id)
);

create table material_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constriants
    constraint pk_material_types primary key (id),
    constraint uc_material_types unique (id)
);

create table frequency_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_frequency_types primary key (id),
    constraint uc_frequency_types unique (id)
);

create table inspection_types
(
    id integer not null,
    name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_inspection_types primary key (id),
    constraint uc_inspection_types unique (id)
);

-- record tables

create table lot_numbers
(
    id serial not null,
    name varchar(32) not null unique,

    -- primary key and unique constraints
    constraint pk_lot_numbers primary key (id),
    constraint uc_lot_numbers unique (id)
);

create table suppliers
(
    id serial not null,
    name varchar(128) not null unique,

    -- primary key and unique constraints
    constraint pk_suppliers primary key (id),
    constraint uc_suppliers unique (id)
);

create table departments
(
    id serial not null,
    name varchar(32) not null unique,
    description varchar(128) not null,

    -- primary key and unique constraints
    constraint pk_departments primary key (id),
    constraint uc_departments unique (id)
);

create table locations
(
    id serial not null,
    name varchar(32) not null unique,
    description varchar(128) not null,

    -- primary key and unique constraint
    constraint pk_locations primary key (id),
    constraint uc_locations unique (id),

    -- many locations relate to one location type
    location_type_id integer not null,
    constraint fk_location_type foreign key (location_type_id) references location_types(id)
);

create table employees
(
    id integer not null,
    first_name varchar(32) not null,
    last_name varchar(32) not null,

    -- primary key and unique constraints
    constraint pk_employees primary key (id),
    constraint uc_employees unique (id),

    -- many employees relate to one department
    department_id integer not null,
    constraint fk_employee_department foreign key (department_id) references departments(id),

    -- many employees relate to one location
    location_id integer not null,
    constraint fk_employee_location foreign key (location_id) references locations(id),

    -- first and last name combination is unique
    constraint uc_employee_name unique (first_name, last_name)
);

create table job_numbers
(
    id serial not null,
    name varchar(32) not null unique,
    production_rate integer not null,
    full_inspect_interval integer not null,
    released_qty integer not null,
    completed_qty integer not null,

    -- many job numbers relate to one employee
    employee_id integer not null,
    constraint fk_employee_id foreign key (employee_id) references employees(id),

    -- many job numbers relate to one material type
    material_type_id integer not null,
    constraint fk_material_type_ins foreign key (material_type_id) references material_types(id),

    -- many job numbers relate to one location
    location_id integer not null,
    constraint fk_location_id foreign key (location_id) references locations(id),

    -- primary key and unique constraints
    constraint pk_job_numbers primary key (id),
    constraint uc_job_numbers unique (id)
);

create table purchase_orders
(
    id serial not null,
    name varchar(32) not null unique,

    -- primary key and unique constraints
    constraint pk_purchase_orders primary key (id),
    constraint uc_purchase_orders unique (id),

    -- one purchase order is related to one supplier
    supplier_id integer not null,
    constraint fk_supplier_id foreign key (supplier_id) references suppliers(id)
);

create table receiver_numbers
(
    id serial not null,
    name varchar(32) not null unique,
    received_qty integer not null,

    -- primary key and unique constraints
    constraint pk_receiver_numbers primary key (id),
    constraint uc_receiver_numbers unique (id),

    -- many receiver numbers can relate to one purchase order
    purchase_order_id integer,
    constraint fk_purchase_order_id foreign key (purchase_order_id) references purchase_orders(id)
);

create table projects
(
    id serial not null,
    name varchar(32) not null unique,
    description varchar(128),
    day_started date not null,
    day_finished date,

    -- primary key and unique constraints
    constraint pk_projects primary key (id),
    constraint uc_projects unique (id),

    -- many projects relate to one project type
    project_type_id integer not null,
    constraint fk_project_type foreign key (project_type_id) references project_types(id)
);

create table machines
(
    id serial not null,
    name varchar(32) not null unique,

    -- primary key and unique constraints
    constraint pk_machines primary key (id),
    constraint uc_machines unique (id),

    -- many machines relate to one machine type
    machine_type_id integer not null,
    constraint fk_machine_type foreign key (machine_type_id) references machine_types(id),

    -- many machines relate to one location
    machine_location_id integer not null,
    constraint fk_machine_location foreign key (machine_location_id) references locations(id)
);

create table inspection_records
(
    id serial not null,

    -- primary key and unique constraints
    constraint pk_inspection_records primary key (id),
    constraint uc_inspection_records unique (id),

    -- many inspection reports can relate to one employee
    employee_id integer not null,
    constraint fk_employee_ins foreign key (employee_id) references employees(id),

    -- many inspections relate to one disposition type
    disposition_id integer not null,
    constraint fk_disposition_ins foreign key (disposition_id) references disposition_types(id)
);

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

create table gauges
(
    id serial not null,
    name varchar(32) not null unique,
    last_calibrated date not null,

    -- primary key and unique constraints
    constraint pk_gauges primary key (id),
    constraint uc_gauges unique (id),

    -- many gauges relate to one gauge type
    gauge_type_id integer not null,
    constraint fk_gauge_type foreign key (gauge_type_id) references gauge_types(id),

    -- many gauges can relate to one employee
    employee_id integer,
    constraint fk_employee_gauge foreign key (employee_id) references employees(id),

    -- many gauges can relate to one location
    location_id integer,
    constraint fk_location_gauge foreign key (location_id) references locations(id)
);

create table inspections
(
    id serial not null,
    part_index integer not null,
    datetime_measured timestamp not null,

    -- many inspections relate to one inspection report
    inspection_record_id integer not null,
    constraint fk_inspection_record_id foreign key (inspection_record_id) references inspection_records(id),

    -- many inspections relate to one part
    part_id integer not null,
    constraint fk_measurement_set_part foreign key (part_id) references parts(id),

    -- many inspections can relate to one employee
    employee_id integer not null,
    constraint fk_employee_char foreign key (employee_id) references employees(id),

    -- many inspections relate to one inspection type
    inspection_type_id integer not null,
    constraint fk_inspection_type_id foreign key (inspection_type_id) references inspection_types(id),

    -- primary key and unique constraints
    constraint pk_inspections primary key (id),
    constraint uc_inspections unique (id)
);

create table print_features
(
    id serial not null,
    name varchar(32) not null,
    nominal decimal not null,
    usl decimal not null,
    lsl decimal not null,
    precision integer not null,

    -- many measurement set schema details relate to one specification type
    specification_type_id integer not null,
    constraint fk_spectype_id_schema foreign key (specification_type_id) references specification_types(id),

    -- many measurement set schema details relate to one dimension type
    dimension_type_id integer not null,
    constraint fk_dimetype_id foreign key (dimension_type_id) references dimension_types(id),

    -- many measurement set schema details relate to one frequency type
    frequency_type_id integer not null,
    constraint fk_freqtype_id_schema foreign key (frequency_type_id) references frequency_types(id),

    -- many measurement set schema details relate to one gauge type
    gauge_type_id integer not null,
    constraint fk_gaugtype_id_schema foreign key (gauge_type_id) references gauge_types(id),

    -- many print feature relate to one operation
    operation_type_id integer not null,
    constraint fk_operation_type_id foreign key (operation_type_id) references operation_types(id),

    -- many print features relate to one part
    part_id integer not null,
    constraint fk_part_id foreign key (part_id) references parts(id),

    -- primary key and unique constraints
    constraint pk_schema_details primary key (id),
    constraint uc_schema_details unique (id)
);

create table features
(
    id serial not null,
    measured decimal,

    -- primary key and unique constraints
    constraint pk_features primary key (id),
    constraint uc_features unique (id),

    -- many features relate to one inspection
    inspection_id integer not null,
    constraint fk_inspection_id foreign key (inspection_id) references inspections(id),

    -- many features relate to one print
    print_feature_id integer not null,
    constraint fk_print_feature_id foreign key (print_feature_id) references print_features(id),

    -- many features can relate to one gauge
    gauge_id integer,
    constraint fk_gauge_id foreign key (gauge_id) references gauges(id)
);

-- linking tables

create table employee_projects
(
    id serial not null unique,
    employee_id integer not null references employees(id) on update cascade,
    project_id integer not null references projects(id) on update cascade,
    constraint pk_employee_project primary key (id),
    constraint uc_employee_project unique (employee_id, project_id)
);

create table inspections_job_numbers
(
    id serial not null unique,
    inspection_id integer not null references inspections(id) on update cascade,
    job_number_id integer not null references job_numbers(id) on update cascade,
    constraint pk_inspections_job_numbers primary key (id),
    constraint uc_inspections_job_numbers unique (inspection_id, job_number_id)
);

create table inspections_purchase_orders
(
    id serial not null unique,
    inspection_id integer not null references inspections(id) on update cascade,
    purchase_order_id integer not null references purchase_orders(id) on update cascade,
    constraint pk_inspection_purchase_orders primary key (id),
    constraint uc_inspection_purchase_orders unique (inspection_id, purchase_order_id)
);

create table inspections_lot_numbers
(
    id serial not null unique,
    inspection_id integer not null references inspections(id) on update cascade,
    lot_number_id integer not null references lot_numbers(id) on update cascade,
    constraint pk_inspection_lot_number primary key (id),
    constraint uc_inspection_lot_number unique (inspection_id, lot_number_id)
);
