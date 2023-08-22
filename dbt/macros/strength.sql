{% macro strength(stronger_team, your_team) %}
    CASE 
        WHEN {{ "stronger_team" }} = 'equal' THEN 'equal'
        WHEN {{ "stronger_team" }} = {{ "your_team" }} THEN 'weak'
        ELSE 'strong' 
    END

{% endmacro %}
