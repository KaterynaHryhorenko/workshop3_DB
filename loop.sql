 
SET SERVEROUTPUT ON
 
DECLARE
country_name pop_destiny.country_fk%TYPE := 'Zambia';
koef_population pop_destiny.population%TYPE := 9936;
koef_area pop_destiny.area%TYPE := 833;
add_date date;
begin


 add_date  := TO_CHAR(SYSDATE, 'DD.MM.YYYY');
 
  FOR i IN 1..5 LOOP
        INSERT INTO pop_destiny (
        country_fk,
        population,
        area,
        add_date)
        values(
        trim(country_name),
        i*koef_population,
        i*koef_area,
        add_date
        );
        end loop;
end;