CREATE TABLE country (
    country  VARCHAR2(38) NOT NULL,
    region1  VARCHAR2(128) NOT NULL
);

ALTER TABLE country ADD CONSTRAINT country_pk PRIMARY KEY ( country );


CREATE TABLE country_type

(
    agriculture  NUMBER(38, 3),
    industry     NUMBER(38, 3),
    services     NUMBER(38, 3),
    country_fk   VARCHAR2( 38 ) NOT NULL, 
    add_date DATE ) 
;

ALTER TABLE country_type
    ADD CONSTRAINT country_type_CK_1 CHECK ( agriculture + industry + services = 1 );



CREATE TABLE gdp

(
    gdp         NUMBER(38, 2),
    country_fk  VARCHAR2( 38) NOT NULL, add_date DATE ) 
;

ALTER TABLE gdp ADD CONSTRAINT gdp_ck_1 CHECK ( gdp >= 0 );




CREATE TABLE net_migration

(
    net_migration  NUMBER(38, 2),
    country_fk     VARCHAR2( 38) NOT NULL, 
    add_date DATE ) 
;



CREATE TABLE pop_destiny

(
    population  NUMBER(38),
    area        NUMBER(38),
    country_fk  VARCHAR2( 38) NOT NULL, add_date DATE ) 
;

ALTER TABLE pop_destiny ADD CONSTRAINT "pop destiny_CK_1" CHECK ( population >= 0 );

ALTER TABLE pop_destiny ADD CONSTRAINT "pop destiny_CK_2" CHECK ( area >= 0 );



CREATE TABLE region (
    region VARCHAR2(128) NOT NULL
);

ALTER TABLE region ADD CONSTRAINT region_pk PRIMARY KEY ( region );

ALTER TABLE country
    ADD CONSTRAINT country_region_fk FOREIGN KEY ( region1 )
        REFERENCES region ( region );

ALTER TABLE country_type
    ADD CONSTRAINT "country type_country_FK" FOREIGN KEY ( country_fk )
        REFERENCES country ( country );

ALTER TABLE gdp
    ADD CONSTRAINT gdp_country_fk FOREIGN KEY ( country_fk )
        REFERENCES country ( country );

ALTER TABLE net_migration
    ADD CONSTRAINT "Net migration_country_FK" FOREIGN KEY ( country_fk )
        REFERENCES country ( country );

ALTER TABLE pop_destiny
    ADD CONSTRAINT "pop destiny_country_FK" FOREIGN KEY ( country_fk )
        REFERENCES country ( country );


