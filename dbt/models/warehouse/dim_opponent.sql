{{
    config(
        materialized="table",
        cluster_by = 'strength'
    )
}}


SELECT
    DISTINCT encode(digest((strength || opponent_formation || opponent_marking || opponent_offside_trap || opponent_style_of_play || opponent_tackling || opponent_training_camp), 'sha256'), 'hex') as id,
    strength,
    opponent_formation,
    opponent_marking,
    opponent_offside_trap,
    opponent_style_of_play,
    opponent_tackling,
    opponent_training_camp
FROM
    {{ ref('staging') }}