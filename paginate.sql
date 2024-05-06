CREATE OR REPLACE PROCEDURE paginate(IN records_per_page INT, IN page_number INT)
LANGUAGE plpgsql
AS $$
DECLARE
    name_val TEXT;
    surname_val TEXT;
    phone_number_val TEXT;
    row_count INT := 0;
BEGIN
    FOR name_val, surname_val, phone_number_val IN
        SELECT name, surname, phone_number FROM telephone
        LIMIT records_per_page OFFSET page_number 
    LOOP
        -- Print debug information
        RAISE NOTICE 'Page Number: %, Records Per Page: %, Offset: %', page_number, records_per_page, (page_number - 1) * records_per_page;
        -- Process the data (you can print or do other operations here)
        row_count := row_count + 1;
    END LOOP;


    IF row_count = 0 THEN
        RAISE NOTICE 'No data found for the specified page.';
    END IF;
END;
$$;