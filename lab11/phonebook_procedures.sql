-- FUNCTION: search by pattern
CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phone
    FROM phonebook
    WHERE name ILIKE '%' || pattern || '%'
       OR phone LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

------------------------------------------------------------

-- PROCEDURE: insert or update single user
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

------------------------------------------------------------

-- PROCEDURE: insert many users with validation
CREATE OR REPLACE PROCEDURE insert_many_users(
    IN names TEXT[],
    IN phones TEXT[],
    OUT incorrect_data TEXT[]
)
AS $$
DECLARE
    i INT;
    bad_list TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        
        -- phone validation: 10–15 digits
        IF phones[i] !~ '^[0-9]{10,15}$' THEN
            bad_list := array_append(bad_list, names[i] || ' - ' || phones[i]);
            CONTINUE;
        END IF;

        CALL insert_or_update_user(names[i], phones[i]);

    END LOOP;

    incorrect_data := bad_list;
END;
$$ LANGUAGE plpgsql;

------------------------------------------------------------

-- FUNCTION: pagination
CREATE OR REPLACE FUNCTION get_page(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, phone
    FROM phonebook
    ORDER BY id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;

------------------------------------------------------------

-- PROCEDURE: deletion by name or phone
CREATE OR REPLACE PROCEDURE delete_by_value(value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = value OR phone = value;
END;
$$ LANGUAGE plpgsql;
