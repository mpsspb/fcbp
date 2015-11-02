DROP VIEW v_external_aqua;

CREATE OR REPLACE VIEW v_external_aqua
AS 
(
SELECT a.id, a.date, a.date_start, a.date_begin, a.date_end
     , a.status, a.aqua_aerobics_id, a.client_id
FROM clients_clientaquaaerobics a

UNION ALL

SELECT a.id, a.date, a.date_start, a.date_begin, a.date_end
     , a.status, a.aqua_aerobics_id, ea.client_id
FROM clients_clientaquaaerobics a
    INNER JOIN clients_aquaaerobicsclients ea
        ON a.id = ea.client_aqua_id
);