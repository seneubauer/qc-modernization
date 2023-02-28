-- enumerations

create table location_types
(
    id varchar(25) not null,

    -- primary key and unique constraints
    constraint pk_location_types primary key (id),
    constraint uc_location_types unique (id)
);
-- work station, machine pad, conference room, wfh, main entry

create table machine_types
(
    id varchar(25) not null,

    -- primary key and unique constraints
    constraint pk_machine_types primary key (id),
    constraint uc_machine_types unique (id)
);
-- cnc machine, drill press, filament winder, label laser

create table gauge_types
(
    id varchar(25) not null,

    -- primary key and unique constraints
    constraint pk_gauge_types primary key (id),
    constraint uc_gauge_types unique (id)
);
-- caliper, bore micrometer, indicator, cmm, vision system

