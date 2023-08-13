{% macro result(your_result) %}
    CASE {{ "your_result" }}
        WHEN 'you won' THEN 'won'
        WHEN 'you lost' THEN 'lost'
        WHEN 'draw' THEN 'draw'
    END

{% endmacro %}
