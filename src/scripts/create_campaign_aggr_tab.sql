CREATE OR REPLACE FUNCTION create_campaign_aggr_tab_func()
  RETURNS void AS
$_$
BEGIN

IF EXISTS (
    SELECT *
    FROM   pg_catalog.pg_tables 
    WHERE  schemaname = 'myschema'
    AND    tablename  = 'campaign_aggr_tab'
    ) THEN
   RAISE NOTICE 'Table "myschema"."campaign_aggr_tab" already exists.';
ELSE
   CREATE TABLE myschema.campaign_aggr_tab (
   TIMESTAMP	CHAR(15)	NOT NULL,
   CAMPAIGN_ID	CHAR(7)		NOT NULL,
   USER_COUNT	INT		NOT NULL,
   PRODUCT_ID 	CHAR(7)		NOT NULL,
   IP		CHAR(15)	NOT NULL,
   STAGE	CHAR(4)		NOT NULL,
   PRIMARY KEY( CAMPAIGN_ID,PRODUCT_ID,IP,STAGE)
);

END IF;

END;
$_$ LANGUAGE plpgsql;
