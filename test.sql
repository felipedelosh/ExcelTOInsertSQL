SET SERVEROUTPUT ON;
DECLARE
  v_numero number := 2;
BEGIN

  --Tabla del número v_numero
  for i in 1..10
  loop
  
    DBMS_OUTPUT.PUT_LINE(v_numero || ' * ' || i || ' = ' || v_numero * i);
    
  end loop;
  
END;
/