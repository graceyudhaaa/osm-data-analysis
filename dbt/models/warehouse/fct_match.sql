{{ config(
  materialized = 'table',
  )
}}

WITH stg AS (
    SELECT
        encode(digest((strength || opponent_formation || opponent_marking || opponent_offside_trap || opponent_style_of_play || opponent_tackling || opponent_training_camp), 'sha256'), 'hex') as id_opponent,
        encode(digest((formation || marking || offside_trap || style_of_play || tackling || training_camp || line_tactic_fw || line_tactic_mf || line_tactic_df || result), 'sha256'), 'hex') as id_tactic,
        goals,
        opponent_goals,
        posession,
        opponent_posession,
        shots,
        opponent_shots,
        pressing,
        style,
        tempo,
        goal_diff
    FROM
        {{ ref('staging') }}
),
tactic AS (
    SELECT
        id
    FROM
        {{ ref('dim_tactic' )}}
),
opponent AS (
    SELECT
        id
    FROM
        {{ ref('dim_opponent' )}}
)

SELECT
    tactic.id AS id_tactic,
    opponent.id AS id_opponent,
    goals AS goals,
    opponent_goals AS opponent_goals,
    posession AS posession,
    opponent_posession AS opponent_posession,
    shots AS shots,
    opponent_shots AS opponent_shots,
    pressing AS pressing,
    style AS style,
    tempo AS tempo,
    goal_diff AS goal_diff
FROM stg
LEFT JOIN tactic
        ON stg.id_tactic = tactic.id
LEFT JOIN opponent
        ON stg.id_opponent = opponent.id