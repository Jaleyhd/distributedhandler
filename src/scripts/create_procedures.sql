DROP FUNCTION find_clicks_func(character);
CREATE OR REPLACE FUNCTION find_clicks_func(campaign_id_inp CHAR(7))
  RETURNS TABLE(f1 CHAR(7), f2 CHAR(15)) AS $$
BEGIN
  RETURN QUERY SELECT product_id,timestamp
  FROM myschema.campaign_aggr_tab 
  WHERE campaign_id=campaign_id_inp;
END;

$$ LANGUAGE 'plpgsql' VOLATILE; 
