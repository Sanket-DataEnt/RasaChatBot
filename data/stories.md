## story 001
*greeting
	- utter_greeting
*request_order
	- utter_request_order
*confirm_deny
	- utter_confirm_deny
*confirm_deny
	- utter_bye

## story 003
*greeting
	- utter_greeting
*request_cc
	- utter_request_cc
*number
	- utter_confirm_deny
*confirm_deny
	- utter_bye

## story 01
*greeting
	- utter_greeting
*display_menu
	- action_menu_type
*food_type
	- utter_ask
*food_veg_nveg
	- action_nveg_type
*order
	- action_cuisine_type
*confirm_affirm
	- utter_confirm_affirm
*bye
	- utter_bye

## story 02
*greeting
	- utter_greeting
*display_menu
	- action_menu_type
*food_type
	- utter_ask
*food_veg_nveg
	- action_nveg_type
*order
	- action_cuisine_type
*confirm_deny
	- utter_confirm_deny
*confirm_deny
	- utter_bye

## story 03
*greeting
	- utter_greeting
*display_menu
	- action_menu_type
*food_type
	- utter_ask
*food_veg_nveg
	- action_nveg_type
*order
	- action_cuisine_type
*confirm_deny
	- utter_confirm_deny
*confirm_affirm
	- action_menu_type
*food_type
	- utter_ask
*food_veg_nveg
	- action_nveg_type
*order
	- action_cuisine_type
*confirm_affirm
	- utter_confirm_affirm
*bye
	- utter_bye

## story 04
*greeting
	- utter_greeting
*display_menu
	- action_menu_type
*food_type
	- utter_ask
*food_veg_nveg
	- action_nveg_type
*order
	- action_cuisine_type
*confirm_deny
	- utter_confirm_deny
*confirm_affirm
	- action_menu_type
*food_type
	- utter_ask
*food_veg_nveg
	- action_nveg_type
*order
	- action_cuisine_type
*confirm_deny
	- utter_confirm_deny
*confirm_deny
	- utter_bye
	
## Generated Story 3367769478446566223
* greeting
    - utter_greeting
* request_cc{"CARDINAL": "2"}
    - utter_request_cc
* request_cc
    - utter_confirm_deny
* confirm_deny
    - utter_bye
    - export

## Generated Story 3367769478446566224
* greeting
    - utter_greeting
* request_order{"CARDINAL": "1"}
    - utter_request_order
* request_cc
    - utter_confirm_deny
* confirm_deny
    - utter_bye
    - export

## Generated Story 3367769478446566225
* greeting
    - utter_greeting
* request_order{"CARDINAL": "1"}
    - utter_request_order
* food_type{"food": "indian"}
    - slot{"food": "indian"}
    - utter_ask
* food_veg_nveg{"vegn": "vegetarian"}
    - slot{"vegn": "vegetarian"}
    - action_nveg_type
* order{"cuisine": "aloo paratha"}
    - slot{"cuisine": "aloo paratha"}
    - action_cuisine_type
* confirm_affirm
    - utter_confirm_deny
* confirm_deny
    - utter_confirm_affirm
    - utter_bye
    - export
	
## Generated Story -6764078884926401908
* greeting
    - utter_greeting
* number{"CARDINAL": "1"}
    - utter_request_order
* display_menu
    - action_menu_type
* food_type{"food": "indian"}
    - slot{"food": "indian"}
    - utter_ask
* food_type{"vegn": "vegetarian"}
    - slot{"vegn": "vegetarian"}
    - action_nveg_type
* order{"cuisine": "aloo paratha"}
    - slot{"cuisine": "aloo paratha"}
    - utter_confirm_deny
* confirm_deny
    - utter_confirm_affirm
    - utter_bye
    - export
	
## Generated Story -6764078884926401909
* greeting
    - utter_greeting
* number{"CARDINAL": "1"}
    - utter_request_order
* display_menu
    - action_menu_type
* food_type{"food": "indian"}
    - slot{"food": "indian"}
    - utter_ask
* food_type{"vegn": "vegetarian"}
    - slot{"vegn": "vegetarian"}
    - action_nveg_type
* order{"cuisine": "noodles"}
    - slot{"cuisine": "noodles"}
    - utter_confirm_deny
* confirm_deny
    - utter_confirm_affirm
    - utter_bye
    - export
	
## Generated Story -7804030496254038863
* greeting
    - utter_greeting
* number{"CARDINAL": "1"}
    - utter_request_order
* display_menu
    - action_menu_type
* food_type{"food": "indian"}
    - slot{"food": "indian"}
    - utter_ask
* order{"vegn": "non - vegetarian"}
    - slot{"vegn": "non - vegetarian"}
    - action_nveg_type
* order{"cuisine": "chicken - biryani"}
    - slot{"cuisine": "chicken - biryani"}
    - utter_confirm_deny
* confirm_affirm
    - action_menu_type
* food_type{"food": "chinese"}
    - slot{"food": "chinese"}
    - utter_ask
* greeting{"vegn": "vegetarian"}
    - slot{"vegn": "vegetarian"}
    - action_nveg_type
* order
* order
* order
* order{"cuisine": "noodles"}
    - slot{"cuisine": "noodles"}
* order{"cuisine": "noodles"}
    - slot{"cuisine": "noodles"}
    - utter_confirm_deny
    - utter_confirm_deny
* confirm_deny
    - utter_bye
    - export

## Generated Story -3319488700076162474
* greeting
    - utter_greeting
* number{"CARDINAL": "1"}
    - utter_request_order
* display_menu
    - action_menu_type
* food_type{"food": "italian"}
    - slot{"food": "italian"}
    - utter_ask
* greeting{"vegn": "vegetarian"}
    - slot{"vegn": "vegetarian"}
    - action_nveg_type
* order
* order{"cuisine": "pizza"}
    - slot{"cuisine": "pizza"}
    - utter_confirm_deny
* order
    - utter_confirm_affirm
    - utter_bye
    - export

## Generated Story -6773830504211837841
* greeting
    - utter_greeting
* number{"CARDINAL": "1"}
    - utter_request_order
* display_menu
    - action_menu_type
* food_type{"food": "indian"}
    - slot{"food": "indian"}
    - utter_ask
* food_veg_nveg{"vegn": "non - vegetarian"}
    - slot{"vegn": "non - vegetarian"}
* food_veg_nveg{"vegn": "non - vegetarian", "DATE": "today"}
    - slot{"vegn": "non - vegetarian"}
    - action_nveg_type
* order{"cuisine": "chicken - biryani"}
    - slot{"cuisine": "chicken - biryani"}
    - action_cuisine_type
* confirm_affirm
    - utter_confirm_deny
* order
    - utter_confirm_affirm
    - utter_bye
    - export
	
## Generated Story -8723893366883566515
* greeting
    - utter_greeting
* number{"CARDINAL": "2"}
    - utter_request_cc
* number{"CARDINAL": "9801234567"}
    - utter_confirm_deny
* confirm_affirm
    - action_menu_type
* food_type{"food": "dessert"}
    - slot{"food": "dessert"}
    - utter_ask
* food_veg_nveg{"vegn": "vegetarian"}
    - slot{"vegn": "vegetarian"}
* food_veg_nveg{"vegn": "vegetarian"}
    - slot{"vegn": "vegetarian"}
    - action_nveg_type
* order{"cuisine": "ice - cream"}
    - slot{"cuisine": "ice - cream"}
    - utter_confirm_deny
* order
    - utter_confirm_affirm
    - utter_bye
    - export

