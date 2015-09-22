CREATE OR REPLACE VIEW v_client_debt_upcoming
AS 
(
SELECT cr.id, cr.date, cr.amount
     , cr.count, cr.aqua_aerobics_id
     , cr.client_id, cr.club_card_id
     , cr.personal_id, cr.ticket_id
     , cr.discount, cr.timing_id
     , cr.schedule, cr.is_credit
     , COALESCE(cc.name, a.name, p.name, t.name, tm.name, 'Unknown') As Name
FROM clients_client c
 LEFT JOIN finance_credit cr
    ON c.id = cr.client_id
 LEFT JOIN clients_clientclubcard ccc
    ON cr.club_card_id = ccc.id 
LEFT JOIN products_clubcard cc
    ON ccc.club_card_id = cc.id
LEFT JOIN clients_clientaquaaerobics ca
    ON cr.aqua_aerobics_id = ca.id
LEFT JOIN products_aquaaerobics a
    ON ca.aqua_aerobics_id = a.id
LEFT JOIN clients_clientpersonal cp
    ON cr.personal_id = cp.id
LEFT JOIN products_personal p
    ON cp.personal_id = p.id
LEFT JOIN clients_clientticket ct
    ON cr.ticket_id = ct.id
LEFT JOIN products_ticket t
    ON ct.ticket_id = t.id
LEFT JOIN clients_clienttiming ctm
    ON cr.timing_id = ctm.id
LEFT JOIN products_timing tm
    ON ctm.timing_id = tm.id
WHERE cr.schedule < current_date + 7 
    AND cr.schedule > current_date
);