    NDefines.NDiplomacy.OPINION_FOR_DEMO_FROM_WT_GENERATION = 0					-- Vanilla is -2.0
    NDefines.NProduction.MAX_CIV_FACTORIES_PER_LINE = 20                        -- Vanilla is 15
    NDefines.NCountry.MIN_STABILITY = -0.5										-- Vanilla is 0.0
    -- Peace Conferences
    NDefines.NDiplomacy.PEACE_SCORE_SCALE_FACTOR = 2.15							-- Vanilla is 1.35
    NDefines.NDiplomacy.PEACE_SCORE_DISTRIBUTION = { 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2 } -- Vanilla is 0.2 in the first five turns
    NDefines.NAI.PEACE_AI_EVALUATE_OTHER_ALWAYS = true							-- Vanilla is false

    NDefines.NDiplomacy.EMBARGO_COST = 50                                       -- Vanilla is 100
    NDefines.NDiplomacy.EMBARGO_THREAT_THRESHOLD = -1                           -- Vanilla is 30
    NDefines.NAI.EMBARGO_WORLD_TENSION_THREAT_DIVISOR = 0                       -- Vanilla is 2.5

    NDefines.NGame.LAG_DAYS_FOR_LOWER_SPEED = 30								-- Vanilla is 10
    NDefines.NGame.LAG_DAYS_FOR_PAUSE = 60										-- Vanilla is 25
    NDefines.NCountry.EVENT_PROCESS_OFFSET = 5									-- Vanilla is 20

    NDefines.NGame.END_DATE = "1959.1.1.1"										-- Vanilla is 1949.1.1.1
    NDefines.NGame.HANDS_OFF_START_TAG = "BHU"									-- Vanilla is URG： Uraguay is disapparing

    -- General AI
    NDefines.NAI.RESEARCH_BONUS_FACTOR = 1.5									-- Vanilla is 0.9
    NDefines.NAI.MIN_AI_SCORE_TO_TRADE_LAW_OVERRIDE_HARD_CODED_SCORE = 0.0		-- Vanilla is 1000.0
    NDefines.NAI.XP_RATIO_REQUIRED_TO_RESEARCH_WITH_XP = 1.6					-- Vanilla is 2 - needed to make AI research naval techs with XP
    NDefines.NAI.RESEARCH_WITH_XP_AI_WEIGHT_MULT = 4.0							-- Vanilla is 1.2 - bigger prio for naval techs if can spend XP

    NDefines.NAI.ASSIGN_TANKS_TO_NON_WAR_FRONT = 0								-- Vanilla is 0.4
    NDefines.NAI.ASSIGN_TANKS_TO_MOUNTAINS = -10								-- Vanilla is -6
    NDefines.NAI.ASSIGN_TANKS_TO_JUNGLE = -10									-- Vanilla is -6

    NDefines.NAI.FRONT_EVAL_UNIT_ACCURACY = 1.5									-- Vanilla is 1.0
    NDefines.NAI.MIN_FORCE_RATIO_TO_PROTECT = 0									-- Vanilla is 0.5
    NDefines.NAI.FRONT_EVAL_PERCENT_TO_ASSIST_ALLY_FRONT = 0					-- Vanilla is 0.5

    NDefines.NAI.CALL_ALLY_NEUTRAL_DESIRE = 75									-- Vanilla is 25
    NDefines.NAI.JOIN_ALLY_NEUTRAL_DESIRE = 75									-- Vanilla is 25

    -- Combat AI
    NDefines.NMilitary.EQUIPMENT_COMBAT_LOSS_FACTOR = 0.60						-- Vanilla is 0.7
    NDefines.NAI.FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.6			-- Vanilla is 0.5
    NDefines.NAI.HEAVILY_FORTIFIED_RATIO_TO_CONSIDER_A_FRONT_FORTIFIED = 0.6	-- Vanilla is 0.5
    NDefines.NMilitary.PLAN_EXECUTE_CAREFUL_MAX_FORT = 8						-- Vanilla is 5
    NDefines.NAI.ATTACK_HEAVILY_DEFENDED_LIMIT = 0.8							-- Vanilla is 0.5
    NDefines.NAI.STR_BOMB_AA_IMPORTANCE_FACTOR = 0		                        -- Vanilla is 0.5

    -- WA-Plane

    NDefines.NAI.LAND_DEFENSE_AIR_SUPERIORITY_IMPORTANCE = 2.0							-- Strategic importance of air superiority ( amount of enemy planes in area )

    NDefines.NAI.LAND_DEFENSE_CIVIL_FACTORY_IMPORTANCE = 150							-- Strategic importance of civil factories
    NDefines.NAI.LAND_DEFENSE_MILITARY_FACTORY_IMPORTANCE = 200							-- Strategic importance of military factories
    NDefines.NAI.LAND_DEFENSE_FIGHERS_PER_PLANE = 2.0									-- Amount of air superiority planes requested per enemy plane
    NDefines.NAI.LAND_DEFENSE_INTERSEPTORS_PER_BOMBERS = 2.0							-- Amount of air interceptor planes requested per enemy bomber
    NDefines.NAI.LAND_DEFENSE_INTERSEPTORS_PER_PLANE = 0								-- Amount of air interceptor planes requested per enemy plane (non bomber)
    NDefines.NAI.LAND_DEFENSE_SUPPLY_HUB_IMPORTANCE = 80								-- Strategic importance of supply hubs
    NDefines.NAI.LAND_DEFENSE_AA_IMPORTANCE_FACTOR = 1.0								-- Factor of AA influence on strategic importance ( 0.0 - 1.0 )
    NDefines.NAI.LAND_DEFENSE_INFRA_IMPORTANCE_FACTOR = 70								-- Factor of infrastructure influence on strategic importance ( 0.0 - 1.0 )

    NDefines.NAI.LAND_COMBAT_AIR_SUPERIORITY_IMPORTANCE = 2.0 							-- Strategic importance of air superiority ( amount of enemy planes in area )
    NDefines.NAI.LAND_COMBAT_OUR_ARMIES_AIR_IMPORTANCE = 25 							-- Strategic importance of our armies
    NDefines.NAI.LAND_COMBAT_OUR_COMBATS_AIR_IMPORTANCE = 100							-- Strategic importance of our armies in the combats
    NDefines.NAI.LAND_COMBAT_IMPORTANCE_SCALE = 5 										-- Lend combat total importance scale (every land combat score get's multiplied by it)
    NDefines.NAI.LAND_COMBAT_FIGHTERS_PER_PLANE = 1.2									-- Amount of air superiority planes requested per enemy plane
    NDefines.NAI.LAND_COMBAT_CAS_PER_ENEMY_ARMY = 50									-- Amount of CAS planes requested per enemy army
    NDefines.NAI.AIR_SUPERIORITY_FOR_FRIENDLY_CAS_RATIO = 0.0							-- Demand at least this proportion of our cas planes as air superiority regardless of other needs
    NDefines.NAI.LAND_COMBAT_CAS_PLANES_PER_ENEMY_ARMY_LIMIT = 1500						-- Limit of CAS planes requested by enemy armies
    NDefines.NAI.LAND_COMBAT_ANTI_LOGISTICS_PER_ENEMY_ARMY = 0    						-- Amount of CAS planes requested per enemy army for anti-logistics
    NDefines.NAI.LAND_COMBAT_CAS_PER_COMBAT = 150										-- Amount of CAS requested per combat
    NDefines.NAI.LAND_COMBAT_BOMBERS_PER_LAND_FORT_LEVEL = 30							-- Amount of bomber planes requested per enemy land fort level
    NDefines.NAI.LAND_COMBAT_MIN_EXCORT_WINGS = 3										-- Min amount of airwings requested to excort operations
    NDefines.NAI.LAND_COMBAT_INTERCEPT_PER_PLANE = 0									-- Amount of interception planes requested per enemy plane

    NDefines.NAI.NAVAL_COMBAT_TRANSFER_AIR_IMPORTANCE = 500.0							-- Naval combat involving enemy land units

    NDefines.NAI.STR_BOMB_AIR_SUPERIORITY_IMPORTANCE = 0.0								-- Strategic importance of air superiority ( amount of enemy planes in area )

    NDefines.NAI.STR_BOMB_MIN_ENEMY_FIGHTERS_IN_AREA = 2800								-- If amount of enemy fighters is higher than this mission won't perform
    NDefines.NAI.STR_BOMB_FIGHTERS_PER_PLANE = 50.0										-- Amount of air superiority planes requested per enemy plane
    NDefines.NAI.STR_BOMB_MIN_EXCORT_PLANES = 100											-- Min amount of planes requested to excort operations
    NDefines.NAI.RECON_PLANES_NAVAL = 500                           					-- scale on recon for naval areas
    NDefines.NAI.RECON_PLANES_LAND_COMBAT = 25                   	 					-- scale on recon for land combat areas
    NDefines.NAI.RECON_PLANES_STRATEGIC = 50                     	 					-- scale on recon for strategic areas

    -- Hof-Navy
	NDefines.NAI.AGGRESSION_LIGHT_GUN_EFFICIENCY_ON_LIGHT_SHIPS = 0.8  -- Vanilla is 1.0
	NDefines.NAI.AGGRESSION_HEAVY_GUN_EFFICIENCY_ON_LIGHT_SHIPS = 0.6  -- Vanilla is 0.25
	NDefines.NAI.AGGRESSION_TORPEDO_EFFICIENCY_ON_LIGHT_SHIPS = 0.25   -- Vanilla is 0.1

	NDefines.NAI.AGGRESSION_LIGHT_GUN_EFFICIENCY_ON_HEAVY_SHIPS = 0.05 -- Vanilla is 0.1

	NDefines.NAI.CARRIER_HOURS_DELAY_AFTER_EACH_COMBAT = 0			   -- Vanilla is 3

    NDefines.NAI.CARRIER_STACK_PENALTY = 16							   -- Vanilla is 4 Hof is 10

    NDefines.NAI.CARRIER_STACK_PENALTY_EFFECT = 0.4					   -- Vanilla is 0.2 Hof is 0.6
    NDefines.NAI.SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE = 0.05		   -- Vanilla is 0.035

    -- Diplomacy
    NDefines.NAI.FASCISTS_BEFRIEND_FASCISTS = 0									-- Vanilla is 10
    NDefines.NAI.FASCISTS_ALLY_FASCISTS = 0										-- Vanilla is 0
    NDefines.NAI.FASCISTS_ANTAGONIZE_FASCISTS = 0								-- Vanilla is -10

    NDefines.NAI.FASCISTS_BEFRIEND_DEMOCRACIES = 0								-- Vanilla is -25
    NDefines.NAI.FASCISTS_ALLY_DEMOCRACIES = 0									-- Vanilla is -100
    NDefines.NAI.FASCISTS_ANTAGONIZE_DEMOCRACIES = 0							-- Vanilla is 100

    NDefines.NAI.FASCISTS_BEFRIEND_COMMUNISTS = -25								-- Vanilla is -25
    NDefines.NAI.FASCISTS_ALLY_COMMUNISTS = -100								-- Vanilla is -100
    NDefines.NAI.FASCISTS_ANTAGONIZE_COMMUNISTS = 0							    -- Vanilla is 100

    NDefines.NAI.DEMOCRACIES_BEFRIEND_FASCISTS = 0								-- Vanilla is -25
    NDefines.NAI.DEMOCRACIES_ALLY_FASCISTS = 0									-- Vanilla is -50
    NDefines.NAI.DEMOCRACIES_ANTAGONIZE_FASCISTS = 0							-- Vanilla is 0

    NDefines.NAI.DEMOCRACIES_BEFRIEND_DEMOCRACIES = 0							-- Vanilla is 0
    NDefines.NAI.DEMOCRACIES_ALLY_DEMOCRACIES = 0								-- Vanilla is 0
    NDefines.NAI.DEMOCRACIES_ANTAGONIZE_DEMOCRACIES = 0							-- Vanilla is -25

    NDefines.NAI.DEMOCRACIES_BEFRIEND_COMMUNISTS = 0							-- Vanilla is -25
    NDefines.NAI.DEMOCRACIES_ALLY_COMMUNISTS = 0								-- Vanilla is -50
    NDefines.NAI.DEMOCRACIES_ANTAGONIZE_COMMUNISTS = 0							-- Vanilla is 0

    NDefines.NAI.COMMUNISTS_BEFRIEND_FASCISTS = -25								-- Vanilla is -25
    NDefines.NAI.COMMUNISTS_ALLY_FASCISTS = -100								-- Vanilla is -100
    NDefines.NAI.COMMUNISTS_ANTAGONIZE_FASCISTS = 10							-- Vanilla is 100

    NDefines.NAI.COMMUNISTS_BEFRIEND_DEMOCRACIES = 0							-- Vanilla is -25
    NDefines.NAI.COMMUNISTS_ALLY_DEMOCRACIES = 0								-- Vanilla is -50
    NDefines.NAI.COMMUNISTS_ANTAGONIZE_DEMOCRACIES = 0							-- Vanilla is 10

    NDefines.NAI.COMMUNISTS_BEFRIEND_COMMUNISTS = 0							    -- Vanilla is 25
    NDefines.NAI.COMMUNISTS_ALLY_COMMUNISTS = 0								    -- Vanilla is 0
    NDefines.NAI.COMMUNISTS_ANTAGONIZE_COMMUNISTS = -25							-- Vanilla is -10

    -- Railway
    NDefines.NMilitary.STRATEGIC_SPEED_INFRA_BASE = 2.0                         -- Vanilla is 5
    NDefines.NMilitary.STRATEGIC_SPEED_INFRA_MAX = 5.0                          -- Vanilla is 10
    NDefines.NMilitary.STRATEGIC_SPEED_RAIL_BASE = 8.0                          -- Vanilla is 15
    NDefines.NMilitary.STRATEGIC_SPEED_RAIL_MAX = 10.0                          -- Vanilla is 25
    NDefines.NMilitary.STRATEGIC_REDEPLOY_ORG_RATIO = 0.01 				        -- Vanilla is 0.1

    -- Other
    NDefines.NMilitary.BATALION_NOT_CHANGED_EXPERIENCE_DROP = 0.0		        -- Vanilla is 0
    NDefines.NMilitary.BATALION_CHANGED_EXPERIENCE_DROP = 0.2			        -- Vanilla is 0.5

    --Expericence
    NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 800			                    -- Vanilla is 500
    NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 800			                    -- Vanilla is 500
    NDefines.NMilitary.MAX_AIR_EXPERIENCE = 800 				                -- Vanilla is 500
    
    NDefines.NMilitary.RIVER_CROSSING_SPEED_PENALTY = -0.3         			    -- Vannilla is -0.25
    NDefines.NMilitary.RIVER_CROSSING_SPEED_PENALTY_LARGE = -0.6   				-- Vannilla is -0.5
    NDefines.NMilitary.TRAINING_MAX_DAILY_COUNTRY_EXP = 0.10					-- Vannilla is 0.08
    NDefines.NMilitary.ENCIRCLED_DISBAND_MANPOWER_FACTOR = 0.1       			-- Vannilla is 0.2
    NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 10                    -- Vannilla is 20
    NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 3                    -- Vannilla is 5
    NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 3                      -- Vannilla is 10

    NDefines.NTechnology.BASE_YEAR_AHEAD_PENALTY_FACTOR = 3		                -- Vanilla is 2

    --Volunteers
    NDefines.NDiplomacy.VOLUNTEERS_PER_TARGET_PROVINCE = 0.0					-- Vanilla is 0.05
    NDefines.NDiplomacy.VOLUNTEERS_PER_COUNTRY_ARMY = 0						    -- Vanilla is 0.05 
    NDefines.NDiplomacy.VOLUNTEERS_RETURN_EQUIPMENT = 1.0						-- Vanilla is 0.95
    NDefines.NDiplomacy.VOLUNTEERS_TRANSFER_SPEED = 7						    -- Vanilla is 14
    NDefines.NDiplomacy.VOLUNTEERS_DIVISIONS_REQUIRED = 0						-- Vanilla is 30 

    NDefines.NDiplomacy.OPINION_PER_VOLUNTEER = 30						        -- Vanilia is 3
	NDefines.NDiplomacy.MAX_OPINION_FROM_VOLUNTEERS = 30				        -- Vanilia is 30

    NDefines.NCountry.AIR_VOLUNTEER_PLANES_RATIO = 0				            -- Vanilia is 0.1
    NDefines.NCountry.AIR_VOLUNTEER_BASES_CAPACITY_LIMIT = 0		            -- Vanilia is 0.2

    NDefines.NDiplomacy.VOLUNTEERS_DIVISIONS_REQUIRED = 0						-- Vanilla is 30 