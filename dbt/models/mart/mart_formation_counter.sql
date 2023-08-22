{{ config(
  materialized = 'view',
  )
}}

--SELECT encode(digest(strength, 'sha256'), 'hex') FROM osm.public.staging
WITH match AS (
	SELECT
		id_tactic,
		id_opponent
	FROM {{ ref('fct_match') }}
),
tactic AS (
	SELECT 
		id,
		formation,
		result
	FROM {{ ref('dim_tactic') }}
	WHERE "result" != 'draw'  
),
opponent AS (
	SELECT 
		id,
		strength,
		opponent_formation AS formation
	FROM {{ ref('dim_opponent') }}
),
processed AS (
	SELECT DISTINCT 
		opponent.strength AS opponent_strength,
		tactic.formation AS tactic_formation,
		opponent.formation AS opponent_formation,
		tactic.result AS result
	FROM match
	left join tactic
		on match.id_tactic = tactic.id
	left join opponent
		on match.id_opponent = opponent.id
	WHERE result is not null
)

SELECT DISTINCT
	CASE result
		WHEN 'won' THEN opponent_strength
		WHEN 'lost' THEN 
			CASE opponent_strength
				WHEN 'strong' THEN 'weak'
				WHEN 'weak' THEN 'strong'
				ELSE 'equal'
			END
	END
    AS strength,

	CASE result
		WHEN 'won' THEN opponent_formation
		WHEN 'lost' THEN tactic_formation 
	END
	AS formation,

	CASE result
		WHEN 'won' THEN tactic_formation
		WHEN 'lost' THEN opponent_formation
	END
	AS counter_formation
    
FROM processed
ORDER by strength 