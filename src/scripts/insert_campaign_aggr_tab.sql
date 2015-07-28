DROP FUNCTION insert_into_campaign_aggr_tab_func(_TIMESTAMP character, _CAMPAIGN_ID character, _USER_COUNT integer, _PRODUCT_ID character, _IP character, _STAGE character);
CREATE FUNCTION insert_into_campaign_aggr_tab_func(_TIMESTAMP character, _CAMPAIGN_ID character, _USER_COUNT integer, _PRODUCT_ID character, _IP character, _STAGE character)
  RETURNS void AS
  $BODY$
      BEGIN
        INSERT INTO myschema.campaign_aggr_tab(TIMESTAMP,CAMPAIGN_ID,USER_COUNT,PRODUCT_ID,IP,STAGE)
        VALUES(_TIMESTAMP,_CAMPAIGN_ID,_USER_COUNT,_PRODUCT_ID,_IP,_STAGE);
      END;
  $BODY$
  LANGUAGE 'plpgsql' VOLATILE
  COST 100;

commit;

