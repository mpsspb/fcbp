CREATE UNIQUE INDEX ind_client_full_name 
ON clients_client (UPPER(first_name), UPPER(last_name), UPPER(patronymic), born);