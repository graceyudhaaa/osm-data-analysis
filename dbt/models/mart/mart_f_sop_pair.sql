{{ config(
  materialized = 'view',
  )
}}

WITH match AS (
	SELECT
		id_tactic,
		id_opponent
	FROM  {{ ref('fct_match') }}
),
tactic AS (
	SELECT 
		id,
		formation,
		style_of_play,
		result
	FROM {{ ref('dim_tactic') }}
	WHERE "result" != 'draw'  
),
opponent AS (
	SELECT 
		id,
		strength,
		opponent_style_of_play AS style_of_play,
		opponent_formation AS formation
	FROM {{ ref('dim_opponent') }}
),
processed AS (
	SELECT DISTINCT 
		opponent.strength AS opponent_strength,
		tactic.formation AS tactic_formation,
		opponent.formation AS opponent_formation,
		tactic.style_of_play AS tactic_style_of_play,
		opponent.style_of_play AS opponent_style_of_play,
		tactic.result AS result
	FROM match
	LEFT JOIN tactic
		ON match.id_tactic = tactic.id
	LEFT JOIN opponent
		ON match.id_opponent = opponent.id
	WHERE result IS NOT NULL
)

SELECT DISTINCT 
	CASE result
		WHEN 'won' THEN opponent_strength
		WHEN 'lost' THEN 
			CASE opponent_strength
				WHEN 'strong' THEN 'weak'
				WHEN 'weak' THEN 'strong'
				else 'equal'
			END
	END AS strength,
	
	CASE result
		WHEN 'won' THEN  tactic_formation
		WHEN 'lost' THEN opponent_formation
	END
	AS formation,
	
	CASE result
		WHEN 'won' THEN tactic_style_of_play
		WHEN 'lost' THEN opponent_style_of_play
	END
	AS style_of_play
FROM processed
ORDER BY strength 