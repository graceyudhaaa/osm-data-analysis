{{
    config(
        materialized="table",
        cluster_by = 'result'
    )
}}

SELECT
    DISTINCT encode(digest((formation || marking || offside_trap || style_of_play || tackling || training_camp || line_tactic_fw || line_tactic_mf || line_tactic_df || result), 'sha256'), 'hex') as id,
    formation,
    marking,
    offside_trap,
    style_of_play,
    tackling,
    training_camp,
    line_tactic_fw,
    line_tactic_mf,
    line_tactic_df,
    result
FROM
    {{ ref('staging') }}