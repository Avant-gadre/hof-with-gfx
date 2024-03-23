--Magic
    NDefines.NGraphics.COUNTRY_FLAG_TEX_MAX_SIZE = 2048
    NDefines.NGraphics.COUNTRY_FLAG_SMALL_TEX_MAX_SIZE = 512
    NDefines.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_WIDTH = 10
    NDefines.NGraphics.COUNTRY_FLAG_STRIPE_TEX_MAX_HEIGHT = 8196
    NDefines.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_WIDTH = 41
    NDefines.NGraphics.COUNTRY_FLAG_LARGE_STRIPE_MAX_HEIGHT = 24000

---------------------- graphics
NDefines_Graphics.NMapMode.MAP_MODE_TERRAIN_TRANSPARENCY = 1.0					-- 0.7 How much transparent are the province colors in the simplified terrain map mode

NDefines_Graphics.NAirGfx.AIRPLANES_CURVE_POINT_DENSITY = 5					    -- 10.0 Higher value = more midpoints in the flight path.
NDefines_Graphics.NAirGfx.AIRPLANES_CURVE_MAX_EXTRAPOLATION = 20				-- 30.0 It's the limit value that avoid making gigantic curves that may happen when flight path is very long.
NDefines_Graphics.NAirGfx.AIRPLANES_CURVE_MIN_ELEVATION = 4.0					-- 4.0 Minimum height above the ground that the curve will generate it's points. Excludes first and last point (takeoff/landing)
NDefines_Graphics.NAirGfx.AIRPLANES_SCALE_TAKEOFF_DIST = 0.1					-- 0.1 Until first x% of the flight path, the airplane will scale up.
NDefines_Graphics.NAirGfx.AIRPLANES_SCALE_MIN = 0.1			 				    -- 0.1 Minimum airplane scale down when takeoff/landing.
NDefines_Graphics.NAirGfx.AIRPLANES_SCALE_LANDING_DIST = 0.9					-- 0.9 After last x% of the flight path, the airplane will scale down.
NDefines_Graphics.NAirGfx.AIRPLANES_SMOOTH_INTERPOLATION_MOVE = 0.15			-- 0.13 How smooth is the movement interpolation.
NDefines_Graphics.NAirGfx.AIRPLANES_SMOOTH_INTERPOLATION_TURN = 0.15			-- 0.095 How smooth is the turning interpolation.
NDefines_Graphics.NAirGfx.AIRPLANES_BANK_STRENGTH = 210.0						-- 210 Multiplier of how much the curve affects the wings banking. (angle limited by the following value)
NDefines_Graphics.NAirGfx.AIRPLANES_BANK_ANGLE_LIMIT = 55.0						-- 55 Bank angle limit.
NDefines_Graphics.NAirGfx.AIRPLANES_GROUND_COLLISION_OFFSET_Y = 0.0				-- Lets the 3d airplanes disappear after going a bit under the ground.
NDefines_Graphics.NAirGfx.AIRPLANES_1_FIGHTER_PATROL_ANIM = 10					-- 1,Number of fighters needed for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_3_FIGHTER_PATROL_ANIM = 30					-- 3,Number of fighters needed for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_1_BOMBER_BOMBING_ANIM = 10					-- 1,Number of bombers needed for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_3_BOMBER_BOMBING_ANIM = 30					-- 3,Number of bombers needed for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_1_FIGHTER_VS_1_FIGHTER_ANIM = 10			-- 1,Number of fighters needed per side for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_3_FIGHTER_VS_3_FIGHTER_ANIM = 30			-- 3,Number of bombers needed per side for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_1_TRANSPORT_SUPPLY_ANIM = 10				-- 1,Number of planes needed for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_3_TRANSPORT_SUPPLY_ANIM = 30				-- 3,Number of planes needed for a single instance of this animation
NDefines_Graphics.NAirGfx.AIRPLANES_1_SCOUT_PLANE_PATROL_ANIM = 10              -- 1
NDefines_Graphics.NAirGfx.AIRPLANES_3_SCOUT_PLANE_PATROL_ANIM = 30              -- 3     
NDefines_Graphics.NAirGfx.BOMBERS_DIVISION_FACTOR = 100					        -- 30 Number of effective bombers in a strategic region will be divided by this factor.
NDefines_Graphics.NAirGfx.MISSILES_DIVISION_FACTOR = 30					        -- 60 Number of missiles shown in a strategic region will be divided by this factor.
NDefines_Graphics.NAirGfx.FIGHTERS_DIVISION_FACTOR = 100					    -- 30 Number of missiles shown in a strategic region will be divided by this factor.
NDefines_Graphics.NAirGfx.SCOUT_PLANE_DIVISION_FACTOR = 100					    -- 30 Number of missiles shown in a strategic region will be divided by this factor.
NDefines_Graphics.NAirGfx.TRANSPORT_DIVISION_FACTOR = 100					    -- 30
NDefines_Graphics.NAirGfx.MAX_MISSILE_BOMBING_SCENARIOS = 1					    -- Max number of missile bombing scenarios in a strategic region.
NDefines_Graphics.NAirGfx.MAX_PATROL_SCENARIOS = 1						        -- Max number of patrol scenarios in a strategic region.
NDefines_Graphics.NAirGfx.MAX_BOMBING_SCENARIOS = 1						        -- Max number of bombings scenarios in a strategic region.
NDefines_Graphics.NAirGfx.MAX_DOGFIGHTS_SCENARIOS = 1						    -- Max number of dogfight scenarios in a strategic region.
NDefines_Graphics.NAirGfx.MAX_TRANSPORT_SCENARIOS = 1						    -- Max number of transport scenarios in a strategic region
NDefines_Graphics.NAirGfx.MAX_TRAINING_SCENARIOS = 1						    -- Max number of training scenarios in a strategic region
NDefines_Graphics.NAirGfx.MAX_SCOUT_SCENARIOS = 1

NDefines_Graphics.NGraphics.MAPICON_GROUP_PASSES = 10                           --20

NDefines_Graphics.NGraphics.MAX_NUMBER_OF_TEXTURES = 10000					    -- 10000 increase if you have more than this textures
NDefines_Graphics.NGraphics.RAILWAY_Y_OFFSET = 0.35						        -- 0.9 Railways are offset by this amount vertically from the map
NDefines_Graphics.NGraphics.RAILWAY_BRIDGE_Y_OFFSET = 0.2					    -- 0.6 Railway bridges are offset by this amount vertically from the map
NDefines_Graphics.NGraphics.RAILWAY_BRIDGE_WIDTH = 4.0					        -- Railways will have straight segments of this length for regular bridges
NDefines_Graphics.NGraphics.RAILWAY_BRIDGE_LARGE_WIDTH = 5.0				    -- Railways will have straight segments of this length for large bridges
NDefines_Graphics.NGraphics.RAILWAY_BRIDGE_GAP_WIDTH = 2.3					    -- Railways will have gaps of this length for regular bridges
NDefines_Graphics.NGraphics.RAILWAY_BRIDGE_GAP_LARGE_WIDTH = 2.5			    -- Railways will have gaps of this length for large bridges
NDefines_Graphics.NGraphics.TRAIN_MAP_SPEED = 4.25						        -- Trains will move at this relative speed. This has no gameplay implications. Changing this value (originally 4.0) may cause audio effects to lose sync with animation.
NDefines_Graphics.NGraphics.MIN_TRAIN_WAGON_COUNT = 1
NDefines_Graphics.NGraphics.MAX_TRAIN_WAGON_COUNT = 1
NDefines_Graphics.NGraphics.MAX_MESHES_LOADED_PER_FRAME = 1
NDefines_Graphics.NGraphics.LAND_UNIT_MOVEMENT_SPEED = 8
NDefines_Graphics.NGraphics.NAVAL_UNIT_MOVEMENT_SPEED = 10

NDefines_Graphics.NGraphics.DRAW_FOW_CUTOFF = 0							        -- Fog of war
NDefines_Graphics.NGraphics.DRAW_FOW_FADE_LENGTH = 0						    -- Fog of war
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_OPTIMIZATION_RANGE = 15.0			-- 30.0 smaller value = faster gradient borders but may have artifacts on large provinces (value to balance)
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_REFRESH_FREQ = 0.1				    -- 0.12 how frequent is gradient borders repainting (optimization for high-speed gameplay)
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_FIELD_COUNTRY_REFRESH = 10			-- 10 When country changes it's size by X provinces, then it refresh it's thickness and rebuilds all provinces

NDefines_Graphics.NGraphics.TRADE_ROUTE_NUM_CONVOYS_SCALE_FACTOR = 1.25
NDefines_Graphics.NGraphics.TRADE_ROUTE_MAX_NUM_CONVOYS = 3
NDefines_Graphics.NGraphics.TRADE_ROUTE_CONVOY_SPEED = 5.0
NDefines_Graphics.NGraphics.TRADE_ROUTE_CONVOY_ROUTE_OFFSET = 0.2
NDefines_Graphics.NGraphics.TRADE_ROUTE_LINE_OFFSET = 0.3
NDefines_Graphics.NGraphics.TRADE_ROUTE_MAX_LINES = 3

NDefines_Graphics.NGraphics.WEATHER_DISTANCE_CUTOFF = 1000					    -- 1500 At what distance weather effects are hidden
NDefines_Graphics.NGraphics.WEATHER_DISTANCE_FADE_LENGTH = 200					-- 400 How far the fade out distance should be
NDefines_Graphics.NGraphics.WEATHER_ZOOM_IN_CUTOFF = 250					    -- 358 At what distance weather effects are faded out the most when zooming in
NDefines_Graphics.NGraphics.WEATHER_ZOOM_IN_FADE_LENGTH = 150					-- 220 How far the zoom in fade out distance should be
NDefines_Graphics.NGraphics.WEATHER_ZOOM_IN_FADE_FACTOR = 0.05					-- 0.0 How much the weather effects should fade out when maximum zoomed in
NDefines_Graphics.NGraphics.WEATHER_PLAYBACK_RATE = 0.5						    -- 0.15 Playback rate at maximum distance
NDefines_Graphics.NGraphics.WEATHER_PLAYBACK_RATE_CUTOFF = 150					-- 500 Playback rate maximum distance
NDefines_Graphics.NGraphics.WEATHER_PLAYBACK_RATE_LENGTH = 200					-- 200 For how long to fade between normal playback rate and maximum distance playback rate

NDefines_Graphics.NGraphics.COUNTRY_COLOR_SATURATION_MODIFIER = 0.63			-- 0.8

NDefines_Graphics.NGraphics.CAMERA_ZOOM_SPEED = 45						        -- 50
NDefines_Graphics.NGraphics.CAMERA_ZOOM_KEY_SCALE = 0.025					    -- 0.02
NDefines_Graphics.NGraphics.CAMERA_ZOOM_SPEED_DISTANCE_MULT = 5.5				-- 6.0 Zoom speed multiplier. When camera is max zoome out, the zooming in speed will get 100% of CAMERA_ZOOM_SPEED_DISTANCE_MULT zooming speed.

NDefines_Graphics.NFrontend.CAMERA_MIN_HEIGHT = 30.0						    --6
NDefines_Graphics.NGraphics.COUNTRY_COLOR_BRIGHTNESS_MODIFIER = 0.83			-- 0.5
NDefines_Graphics.NFrontend.CAMERA_INTERPOLATION_SPEED = 0.15				    -- 0.19

----------------------------

NDefines_Graphics.NMapIcons.STRATEGIC_AIR_PRIORITY_AIR_MISSION = 290
NDefines_Graphics.NGraphics.VICTORY_POINT_MAP_ICON_TEXT_CUTOFF = {300, 500, 1500}

NDefines_Graphics.NGraphics.MAP_ICONS_GROUP_CAM_DISTANCE = 100				--group moving and still units
NDefines_Graphics.NGraphics.MAP_ICONS_STATE_GROUP_CAM_DISTANCE = 325.0		--group into states
NDefines_Graphics.NGraphics.MAP_ICONS_STRATEGIC_GROUP_CAM_DISTANCE = 400		--group units into air regions
NDefines_Graphics.NGraphics.MAP_ICONS_STRATEGIC_AREA_HUGE = 220					--size limit for air region grouping
NDefines_Graphics.NGraphics.MAP_ICONS_STATE_HUGE = 100							--size limit for state grouping
NDefines_Graphics.NGraphics.MAPICON_GROUP_STRATEGIC_SIZE = 1000
NDefines_Graphics.NGraphics.MAP_ICONS_GROUP_SPLIT_SELECTED_LIMIT = 10
NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE = 200
NDefines_Graphics.NGraphics.MAP_ICONS_COARSE_COUNTRY_GROUPING_DISTANCE_STRATEGIC = 0

NDefines_Graphics.NGraphics.COMMANDGROUP_PRESET_COLORS_HSV = {
	0.0/360.0, 1.0, 0.75,	--red
	10.0/360.0, 1.0, 0.75,	--orange
	60.0/360.0, 1.0, 0.75,	--yellow
	120.0/360.0, 0.85, 0.75,	--green
	155.0/360.0, 1.0, 0.75,	--greenish
	180.0/360.0, 1.0, 0.75,	--turq
	220.0/360.0, 1.0, 0.75,	--blue
	260.0/360.0, 1.0, 0.85,	--dark purple
	330.0/360.0, 0, 0.75		--white
}

NDefines_Graphics.NGraphics.AIRBASE_ICON_DISTANCE_CUTOFF = 900
NDefines_Graphics.NGraphics.NAVALBASE_ICON_DISTANCE_CUTOFF = 900

NDefines_Graphics.NGraphics.STRATEGIC_AIR_COLOR_BAD = {0.65, 0, 0, 1}
NDefines_Graphics.NGraphics.STRATEGIC_AIR_COLOR_GOOD = {0, 0.65, 0, 1}
NDefines_Graphics.NGraphics.STRATEGIC_AIR_COLOR_AVERAGE = {0.65, 0.65, 0, 1}
NDefines_Graphics.NGraphics.STRATEGIC_AIR_COLOR_NEUTRAL = {130.0/255, 130.0/255, 130.0/255, 1}

NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_STRATEGIC_REGIONS = 250.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_SUPPLY_AREA_A = 250 --250.0
NDefines_Graphics.NGraphics.GRADIENT_BORDERS_THICKNESS_SUPPLY_AREA_B = 250 --250.0
	
NDefines_Graphics.NGraphics.RESISTANCE_COLOR_GOOD = {0.0, 0.65, 0, 1}
NDefines_Graphics.NGraphics.RESISTANCE_COLOR_AVERAGE = {0.65, 0.65, 0, 1}
NDefines_Graphics.NGraphics.RESISTANCE_COLOR_BAD = {0.65, 0, 0, 1}
	
NDefines_Graphics.NGraphics.STRATEGIC_NAVY_COLOR_MISSION = {0.65, 0.65, 0.0, 1}
NDefines_Graphics.NGraphics.STRATEGIC_NAVY_COLOR_NEUTRAL = {130.0/255, 130.0/255, 130.0/255, 1}

NDefines_Graphics.NGraphics.ROOT_FRONT_OFFSET = 2

--Map modes
    NDefines.NMapMode.MAP_MODE_MANPOWER_RANGE_MAX = 10000000
    NDefines.NMapMode.MAP_MODE_MANPOWER_RANGE_COLOR_FROM = { 0.2, 0.2, 0.7, 0.5 }
    NDefines.NMapMode.MAP_MODE_MANPOWER_RANGE_COLOR_TO = { 1, 0.125, 0.0, 0.75 }