
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import json

# Load data from the JSON file
with open("data.json", "r") as file:
    historical_places_info = json.load(file)


class RetrieveOpeningHours(Action):
    def name(self) -> Text:
        return "action_retrieve_opening_hours"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                opening_hours = place_info.get("opening_hours")
                if opening_hours:
                    opening_hours_response = f"The opening hours of {place} are: {opening_hours}"
                    dispatcher.utter_message(text=opening_hours_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have information about the opening hours of {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots


class RetrieveEntranceFee(Action):
    def name(self) -> Text:
        return "action_retrieve_entrance_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                entrance_fee = place_info.get("entrance_fee")
                if entrance_fee:
                    entrance_fee_response = f"The entrance fee for {place} is: {entrance_fee}"
                    dispatcher.utter_message(text=entrance_fee_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have information about the entrance fee of {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots

class RetrieveAccessibility(Action):
    def name(self) -> Text:
        return "action_retrieve_accessibility"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                accessibility = place_info.get("accessibility")
                if accessibility:
                    accessibility_response = f"The accessibility features at {place} are: {accessibility}"
                    dispatcher.utter_message(text=accessibility_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have information about the accessibility of {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots


class RetrieveHistoricalContext(Action):
    def name(self) -> Text:
        return "action_retrieve_historical_context"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                historical_context = place_info.get("historical_context")
                if historical_context:
                    historical_context_response = f"Here is some historical context about {place}: {historical_context}"
                    dispatcher.utter_message(text=historical_context_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have historical context information about {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots

class RetrieveArchitectureFeatures(Action):
    def name(self) -> Text:
        return "action_retrieve_architecture_features"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                architecture_features = place_info.get("architecture_features")
                if architecture_features:
                    architecture_features_response = f"The architecture features of {place} include: {architecture_features}"
                    dispatcher.utter_message(text=architecture_features_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have information about the architecture features of {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots

class RetrieveLocalCultureCustoms(Action):
    def name(self) -> Text:
        return "action_retrieve_local_culture_customs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                local_culture_customs = place_info.get("local_culture_customs")
                if local_culture_customs:
                    culture_customs_response = f"Here are some local culture and customs associated with {place}: {local_culture_customs}"
                    dispatcher.utter_message(text=culture_customs_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have information about the local culture and customs of {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots

class RetrieveVisitorTipsRecommendations(Action):
    def name(self) -> Text:
        return "action_retrieve_visitor_tips_recommendations"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                visitor_tips_recommendations = place_info.get("visitor_tips_recommendations")
                if visitor_tips_recommendations:
                    tips_recommendations_response = f"Here are some visitor tips and recommendations for {place}: {visitor_tips_recommendations}"
                    dispatcher.utter_message(text=tips_recommendations_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have visitor tips and recommendations for {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots

class RetrieveNearbyAttractions(Action):
    def name(self) -> Text:
        return "action_retrieve_nearby_attractions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                nearby_attractions = place_info.get("nearby_attractions")
                if nearby_attractions:
                    nearby_attractions_response = f"Here are some nearby attractions near {place}: {nearby_attractions}"
                    dispatcher.utter_message(text=nearby_attractions_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have information about nearby attractions for {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots

class RetrieveGeneralInformation(Action):
    def name(self) -> Text:
        return "action_retrieve_general_information"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                directions = place_info.get("directions")
                if directions:
                    general_information_response = f"Here is some general information about {place}: {directions}"
                    dispatcher.utter_message(text=general_information_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have general information about {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots

class RetrieveSpecificPlaceInfo(Action):
    def name(self) -> Text:
        return "action_retrieve_specific_place_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = next(tracker.get_latest_entity_values("place"), None)
        slots = []

        if place:
            place_info = historical_places_info.get(place)
            if place_info:
                specific_place_info = place_info.get("specific_place_info")
                if specific_place_info:
                    specific_place_info_response = f"Here is some information about {place}: {specific_place_info}"
                    dispatcher.utter_message(text=specific_place_info_response)
                    slots.append(SlotSet("location", place))
                else:
                    dispatcher.utter_message(text=f"Sorry, I don't have specific information about {place}.")
            else:
                dispatcher.utter_message(text=f"I'm sorry, I don't have information about {place}.")
        else:
            dispatcher.utter_message(response="utter_default")

        return slots


# class ActionDefaultFallback(Action):
#     def name(self) -> Text:
#         return "action_default_fallback"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_default")
#         return []

