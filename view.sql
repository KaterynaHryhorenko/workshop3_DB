create view queries
as 
select
region.region
,country.country
,gdp.gdp
,country_type.services
,pop_destiny.population
,net_migration.net_migration
from
region left join country on region.region = country.region1
left join gdp on gdp.country_fk = country.country
left join country_type on country_type.country_fk = country.country
left join pop_destiny on pop_destiny.country_fk = country.country
left join net_migration on net_migration.country_fk = country.country;
