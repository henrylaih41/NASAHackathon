# start map
startMap = 100000


# stations
stationMap = {"name":"Investigation station",
			"event":{
				"penguin":{
						"choose":{"look":{"spirit":30,
										"point":-30},
								"eat":{"spirit":-30,
										"point":30,
										"hunger":-30}},
						"costTime":5},
				"boat":{
						"event":{},
						"costTime":0},
				"station":{
						# TODO :update item list
						"choose":{"stay":{},
								"find":{"spirit":20,
										"point":20},
						"costTime":6},
				"blizzard":{"_force":"died"}
				}},
			"human":{}}

plateauMap = {"name":"Plateau",
			"event":{
				"blizzard":{"new":"died"}},
			"human":{
				"Mountain sickness":{
						"Viagra":"none",
						"else":{"spirit":-30,
								"point":30,
								"_force":"back"}
									}
					}
			}

seashoreMap = {"name":"Seashore",
			"event":{
				"fishing":{
					"choose":{"do":{"hunger":-20}},
					"costTime":5
				},
				"pack":{"take":{"hunger":-20,
								"point":10},
						"costTime":1
				}
			},
			"human":{}}
humanDisease = {"scurvy":{"day":8},
				"hunger":{"food":2},
				"freeze":-40,
				"snowBlindness":{"day":3}}