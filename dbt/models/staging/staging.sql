{{ config(materialized='view') }}

WITH lowercase_data AS
    (
        SELECT
            LOWER(stronger_team) AS stronger_team,
            LOWER(your_team) AS your_team,
            LOWER(home_formation) AS home_formation,
            LOWER(away_formation) AS away_formation,
            LOWER(home_style_of_play) AS home_style_of_play,
            LOWER(home_marking) AS home_marking,
            LOWER(home_offside_trap) AS home_offside_trap,
            LOWER(home_tackling) AS home_tackling,
            LOWER(away_style_of_play) AS away_style_of_play,
            LOWER(away_marking) AS away_marking,
            LOWER(away_offside_trap) AS away_offside_trap,
            LOWER(away_tackling) AS away_tackling,
            LOWER(home_training_camp) AS home_training_camp,
            LOWER(away_training_camp) AS away_training_camp,
            LOWER(line_tactic_fw) AS line_tactic_fw,
            LOWER(line_tactic_mf) AS line_tactic_mf,
            LOWER(line_tactic_df) AS line_tactic_df,
            pressing AS pressing,
            style AS style,
            tempo AS tempo,
            home_posession AS home_posession,
            away_posession AS away_posession,
            home_goals AS home_goals,
            away_goals AS away_goals,
            home_shots AS home_shots,
            away_shots AS away_shots,
            LOWER(result) AS result,
            LOWER(your_result) AS your_result
        FROM {{ source("staging", "raw") }}
    ),

    processed_data AS
    (
        SELECT 
            {{strength(stronger_team, your_team)}} AS strength,

            {% for prop in ['formation', 'goals', 'marking', 'offside_trap', 'posession', 'shots', 'style_of_play', 'tackling', 'training_camp'] %}

            {{ home_away_mapping(your_team, "home", "home_"~prop, "away_"~prop) }} AS {{prop}},
            {{ home_away_mapping(your_team, "away", "home_"~prop, "away_"~prop) }} AS opponent_{{prop}},
            
            {% endfor %}

            line_tactic_fw,
            line_tactic_mf,
            line_tactic_df,

            pressing,
            style,
            tempo,

            {{ result(your_result) }} AS result

        FROM lowercase_data
    )

SELECT
    *,
    ABS(goals - opponent_goals) AS goal_diff
FROM processed_data


/*
    Uncomment the line below to remove records with null "id" values
*/

-- where id is not null
