CREATE OR REPLACE VIEW v_client_debt
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
LEFT JOIN products_clubcard cc
    ON cr.club_card_id = cc.id
LEFT JOIN products_aquaaerobics a
    ON cr.aqua_aerobics_id = a.id
LEFT JOIN products_personal p
    ON cr.personal_id = p.id
LEFT JOIN products_ticket t
    ON cr.ticket_id = t.id
LEFT JOIN products_timing tm
    ON cr.timing_id = tm.id
WHERE cr.schedule <= current_date
    OR cr.is_credit = True
);