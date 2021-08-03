# People Data Dictionary
___

## PERSON_ID: _Plain Text_
	A unique identifier for each person record. IDs starting with P indicate passengers. IDs starting with O indicate a person who was not a passenger in the vehicle (e.g., driver, pedestrian, cyclist, etc.).

## PERSON_TYPE: _Plain Text_
	Type of roadway user involved in crash

## CRASH_RECORD_ID: _Plain Text_
	This number can be used to link to the same crash in the Crashes and Vehicles datasets. This number also serves as a unique ID in the Crashes dataset.

## RD_NO: _Plain Text_
	Chicago Police Department report number. For privacy reasons, this column is blank for recent crashes.

## VEHICLE_ID: _Plain Text_
	The corresponding CRASH_UNIT_ID from the Vehicles dataset.

## CRASH_DATE: _Date & Time_
	Date and time of crash as entered by the reporting officer

## SEAT_NO: _Plain Text_
	Code for seating position of motor vehicle occupant:

1= driver, 2= center front, 3 = front passenger, 4 = second row left, 5 = second row center, 6 = second row right, 7 = enclosed passengers, 8 = exposed passengers, 9= unknown position, 10 = third row left, 11 = third row center, 12 = third row right

## CITY: _Plain Text_
	City of residence of person involved in crash

## STATE: _Plain Text_
	State of residence of person involved in crash

## ZIPCODE: _Plain Text_
	ZIP Code of residence of person involved in crash

## SEX: _Plain Text_
	Gender of person involved in crash, as determined by reporting officer

## AGE: _Number_
	Age of person involved in crash

## DRIVERS_LICENSE_STATE: _Plain Text_
	State issuing driver's license of person involved in crash

## DRIVERS_LICENSE_CLASS: _Plain Text_
	Class of driver's license of person involved in crash

## SAFETY_EQUIPMENT: _Plain Text_
	Safety equipment used by vehicle occupant in crash, if any

## AIRBAG_DEPLOYED: _Plain Text_
	Whether vehicle occupant airbag deployed as result of crash

## EJECTION: _Plain Text_
	Whether vehicle occupant was ejected or extricated from the vehicle as a result of crash

## INJURY_CLASSIFICATION: _Plain Text_
	Severity of injury person sustained in the crash

## HOSPITAL: _Plain Text_
	Hospital to which person injured in the crash was taken

## EMS_AGENCY: _Plain Text_
	EMS agency who transported person injured in crash to the hospital

## EMS_RUN_NO: _Plain Text_
	EMS agency run number

## DRIVER_ACTION: _Plain Text_
	Driver action that contributed to the crash, as determined by reporting officer

## DRIVER_VISION: _Plain Text_
	What, if any, objects obscured the driver’s vision at time of crash

## PHYSICAL_CONDITION: _Plain Text_
	Driver’s apparent physical condition at time of crash, as observed by the reporting officer

## PEDPEDAL_ACTION: _Plain Text_
	Action of pedestrian or cyclist at the time of crash

## PEDPEDAL_VISIBILITY: _Plain Text_
	Visibility of pedestrian of cyclist safety equipment in use at time of crash

## PEDPEDAL_LOCATION: _Plain Text_
	Location of pedestrian or cyclist at the time of crash

## BAC_RESULT: _Plain Text_
	Status of blood alcohol concentration testing for driver or other person involved in crash

## BAC_RESULT VALUE: _Number_
	Driver’s blood alcohol concentration test result (fatal crashes may include pedestrian or cyclist results)

## CELL_PHONE_USE: _Plain Text_
	Whether person was/was not using cellphone at the time of the crash, as determined by the reporting officer
