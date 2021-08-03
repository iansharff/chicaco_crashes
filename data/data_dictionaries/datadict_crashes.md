# Crashes Data Dictionary
___

## CRASH_RECORD_ID: _Plain Text_
	This number can be used to link to the same crash in the Vehicles and People datasets. This number also serves as a unique ID in this dataset.

## RD_NO: _Plain Text_
	Chicago Police Department report number. For privacy reasons, this column is blank for recent crashes.

## CRASH_DATE_EST_I: _Plain Text_
	Crash date estimated by desk officer or reporting party (only used in cases where crash is reported at police station days after the crash)

## CRASH_DATE: _Date & Time_
	Date and time of crash as entered by the reporting officer

## POSTED_SPEED_LIMIT: _Number_
	Posted speed limit, as determined by reporting officer

## TRAFFIC_CONTROL_DEVICE: _Plain Text_
	Traffic control device present at crash location, as determined by reporting officer

## DEVICE_CONDITION: _Plain Text_
	Condition of traffic control device, as determined by reporting officer

## WEATHER_CONDITION: _Plain Text_
	Weather condition at time of crash, as determined by reporting officer

## LIGHTING_CONDITION: _Plain Text_
	Light condition at time of crash, as determined by reporting officer

## FIRST_CRASH_TYPE: _Plain Text_
	Type of first collision in crash

## TRAFFICWAY_TYPE: _Plain Text_
	Trafficway type, as determined by reporting officer

## LANE_CNT: _Number_
	Total number of through lanes in either direction, excluding turn lanes, as determined by reporting officer (0 = intersection)

## ALIGNMENT: _Plain Text_
	Street alignment at crash location, as determined by reporting officer

## ROADWAY_SURFACE_COND: _Plain Text_
	Road surface condition, as determined by reporting officer

## ROAD_DEFECT: _Plain Text_
	Road defects, as determined by reporting officer

## REPORT_TYPE: _Plain Text_
	Administrative report type (at scene, at desk, amended)

## CRASH_TYPE: _Plain Text_
	A general severity classification for the crash. Can be either Injury and/or Tow Due to Crash or No Injury / Drive Away

## INTERSECTION_RELATED_I: _Plain Text_
	A field observation by the police officer whether an intersection played a role in the crash. Does not represent whether or not the crash occurred within the intersection.

## NOT_RIGHT_OF_WAY_I: _Plain Text_
	Whether the crash begun or first contact was made outside of the public right-of-way.

## HIT_AND_RUN_I: _Plain Text_
	Crash did/did not involve a driver who caused the crash and fled the scene without exchanging information and/or rendering aid

## DAMAGE: _Plain Text_
	A field observation of estimated damage.

## DATE_POLICE_NOTIFIED: _Date & Time_
	Calendar date on which police were notified of the crash

## PRIM_CONTRIBUTORY_CAUSE: _Plain Text_
	The factor which was most significant in causing the crash, as determined by officer judgment

## SEC_CONTRIBUTORY_CAUSE: _Plain Text_
	The factor which was second most significant in causing the crash, as determined by officer judgment

## STREET_NO: _Number_
	Street address number of crash location, as determined by reporting officer

## STREET_DIRECTION: _Plain Text_
	Street address direction (N,E,S,W) of crash location, as determined by reporting officer

## STREET_NAME: _Plain Text_
	Street address name of crash location, as determined by reporting officer

## BEAT_OF_OCCURRENCE: _Number_
	Chicago Police Department Beat ID. Boundaries available at https://data.cityofchicago.org/d/aerh-rz74

## PHOTOS_TAKEN_I: _Plain Text_
	Whether the Chicago Police Department took photos at the location of the crash

## STATEMENTS_TAKEN_I: _Plain Text_
	Whether statements were taken from unit(s) involved in crash

## DOORING_I: _Plain Text_
	Whether crash involved a motor vehicle occupant opening a door into the travel path of a bicyclist, causing a crash

## WORK_ZONE_I: _Plain Text_
	Whether the crash occurred in an active work zone

## WORK_ZONE_TYPE: _Plain Text_
	The type of work zone, if any

## WORKERS_PRESENT_I: _Plain Text_
	Whether construction workers were present in an active work zone at crash location

## NUM_UNITS: _Number_
	Number of units involved in the crash. A unit can be a motor vehicle, a pedestrian, a bicyclist, or another non-passenger roadway user. Each unit represents a mode of traffic with an independent trajectory.

## MOST_SEVERE_INJURY: _Plain Text_
	Most severe injury sustained by any person involved in the crash

## INJURIES_TOTAL: _Number_
	Total persons sustaining fatal, incapacitating, non-incapacitating, and possible injuries as determined by the reporting officer

## INJURIES_FATAL: _Number_
	Total persons sustaining fatal injuries in the crash

## INJURIES_INCAPACITATING: _Number_
	Total persons sustaining incapacitating/serious injuries in the crash as determined by the reporting officer. Any injury other than fatal injury, which prevents the injured person from walking, driving, or normally continuing the activities they were capable of performing before the injury occurred. Includes severe lacerations, broken limbs, skull or chest injuries, and abdominal injuries.

## INJURIES_NON_INCAPACITATING: _Number_
	Total persons sustaining non-incapacitating injuries in the crash as determined by the reporting officer. Any injury, other than fatal or incapacitating injury, which is evident to observers at the scene of the crash. Includes lump on head, abrasions, bruises, and minor lacerations.

## INJURIES_REPORTED_NOT_EVIDENT: _Number_
	Total persons sustaining possible injuries in the crash as determined by the reporting officer. Includes momentary unconsciousness, claims of injuries not evident, limping, complaint of pain, nausea, and hysteria.

## INJURIES_NO_INDICATION: _Number_
	Total persons sustaining no injuries in the crash as determined by the reporting officer

## INJURIES_UNKNOWN: _Number_
	Total persons for whom injuries sustained, if any, are unknown

## CRASH_HOUR: _Number_
	The hour of the day component of CRASH_DATE.

## CRASH_DAY_OF_WEEK: _Number_
	The day of the week component of CRASH_DATE. Sunday=1

## CRASH_MONTH: _Number_
	The month component of CRASH_DATE.

## LATITUDE: _Number_
	The latitude of the crash location, as determined by reporting officer, as derived from the reported address of crash

## LONGITUDE: _Number_
	The longitude of the crash location, as determined by reporting officer, as derived from the reported address of crash

## LOCATION: _Point_
	The crash location, as determined by reporting officer, as derived from the reported address of crash, in a column type that allows for mapping and other geographic analysis in the data portal software
