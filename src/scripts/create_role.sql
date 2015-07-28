DO
$body$
BEGIN
   IF NOT EXISTS (
      SELECT *
      FROM   pg_catalog.pg_user
      WHERE  usename = 'jaleydholakiya') THEN

      CREATE ROLE jaleydholakiya LOGIN PASSWORD 'pwd';
      GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO jaleydholakiya;
      GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO jaleydholakiya;
   END IF;
END
$body$
