CREATE VIEW queries AS
  SELECT
    region.region                 AS region,
    country.country               AS country,
    gdp.gdp                       AS gdp,
    country_type.services         AS services,
    pop_destiny.population        AS population,
    net_migration.net_migration   AS net_migration
FROM
    region left
    JOIN country ON region.region = country.region1
    LEFT JOIN gdp ON gdp.country_fk = country.country
    LEFT JOIN country_type ON country_type.country_fk = country.country
    LEFT JOIN pop_destiny ON pop_destiny.country_fk = country.country
    LEFT JOIN net_migration ON net_migration.country_fk = country.country
WHERE
    country_type.add_date = TO_DATE('2020/05/2', 'yyyy/mm/dd')
    AND gdp.add_date = TO_DATE('2020/05/2', 'yyyy/mm/dd')
    AND country_type.add_date = TO_DATE('2020/05/2', 'yyyy/mm/dd')
    AND net_migration.add_date = TO_DATE('2020/05/2', 'yyyy/mm/dd');
    

    
