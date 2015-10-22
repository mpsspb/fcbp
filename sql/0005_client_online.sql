DROP VIEW v_client_online;

CREATE OR REPLACE VIEW v_client_online
AS 
(
SELECT row_number() over() as id, client_id, date, product
FROM (
    SELECT cc.client_id, ucc.date, 'clubcard' as product
    FROM clients_clientclubcard cc
     LEFT JOIN clients_useclientclubcard ucc
        ON cc.id = ucc.client_club_card_id
    WHERE ucc.end IS NULL

    UNION ALL

    SELECT a.client_id, ua.date, 'aqua' as product
    FROM clients_clientaquaaerobics a
     LEFT JOIN clients_useclientaquaaerobics ua
        ON a.id = ua.client_aqua_aerobics_id
    WHERE ua.end IS NULL

    UNION ALL

    SELECT t.client_id, ut.date, 'ticket' as product
    FROM clients_clientticket t
     LEFT JOIN clients_useclientticket ut
        ON t.id = ut.client_ticket_id
    WHERE ut.end IS NULL

    UNION ALL

    SELECT p.client_id, up.date, 'personal' as product
    FROM clients_clientpersonal p
     LEFT JOIN clients_useclientpersonal up
        ON p.id = up.client_personal_id
    WHERE up.end IS NULL
    ) online
);