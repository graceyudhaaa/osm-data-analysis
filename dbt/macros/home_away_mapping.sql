{% macro home_away_mapping(your_team, home_away, true_state_col, false_state_col) %}
    CASE 
        WHEN {{ "your_team" }} = '{{ home_away }}' THEN {{ true_state_col }}
        ELSE {{ false_state_col }} 
    END


{% endmacro %}
