CREATE OR REPLACE VIEW v_client_club_card_active
AS 
(
SELECT *
FROM clients_clientclubcard cc
WHERE cc.date_begin <= current_date
    AND cc.date_end >= current_date
    AND cc.status IN (1, 2)
);