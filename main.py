from openai import OpenAI
from dotenv import load_dotenv
import os
import json

weather_data = {
    "Delhi": {
        "temperature": "36°C",
        "condition": "Sunny",
        "humidity": "40%"
    },
    "Mumbai": {
        "temperature": "29°C",
        "condition": "Rainy",
        "humidity": "85%"
    },
    "Bangalore": {
    "temperature": "24°C",
    "condition": "Cloudy",
    "humidity": "60%"
    },
    "Goa": {
    "temperature": "31°C",
    "condition": "Sunny",
    "humidity": "70%"
    }
}
flight_data = {
    "Delhi": {
        "airline": "IndiGo",
        "price": "₹5,200",
    "duration": "2 hrs"
    },
    "Mumbai": {
    "airline": "Air India",
    "price": "₹4,800",
    "duration": "1.5 hrs"
    },
    "Bangalore": {
    "airline": "Vistara",
    "price": "₹6,300",
    "duration": "2.5 hrs"
    },
    "Goa": {
    "airline": "Akasa Air",
    "price": "₹3,900",
    "duration": "1 hr"
    }
}
hotel_data = {
    "Delhi": [
    {
    "name": "The Grand Palace",
    "rating": 4.8,
    "price": "₹4500/night"
    },
    {
    "name": "City Comfort",
    "rating": 4.2,
    "price": "₹2800/night"
    }
    ],

    "Mumbai": [
        {
            "name": "Sea View Hotel",
            "rating": 4.7,
            "price": "₹5200/night"
        }
    ],

    "Bangalore": [
    {
    "name": "Skyline Suites",
    "rating": 4.5,
    "price": "₹3800/night"
    }
    ],

    "Goa": [
    {
    "name": "Beach Resort",
    "rating": 4.6,
    "price": "₹4500/night"
    }
]
}

attractions_data = {
"Delhi": [
"India Gate",
"Red Fort",
"Qutub Minar"
],

"Mumbai": [
"Gateway of India",

"Marine Drive",
"Juhu Beach"
],

"Bangalore": [
"Cubbon Park",
"Lalbagh Botanical Garden",
"Bangalore Palace"
],

"Goa": [
"Baga Beach",
"Fort Aguada",
"Dudhsagar Falls"
]
}


def get_weather(city):
    weather = weather_data.get(city)
    if weather is None:
        return "Sorry, weather information is not available."
    return (
        f"City: {city}\n"
        f"Temperature: {weather['temperature']}\n"
        f"Condition: {weather['condition']}\n"
        f"Humidity: {weather['humidity']}"
        )

def search_flights(destination):
    flight = flight_data.get(destination)
    if flight is None:
        return "Sorry, no flights are available for this destination."
    return (
        f"Destination: {destination}\n"
        f"Airline: {flight['airline']}\n"
        f"Price: {flight['price']}\n"
        f"Duration: {flight['duration']}"
    )

def find_hotels(city):
    hotels = hotel_data.get(city)
    if hotels is None:
        return "Sorry, no hotels found for this city."
    result = f"Hotels in {city}:\n\n"
    for hotel in hotels:
        result += (
            f"Hotel: {hotel['name']}\n"
            f"Rating: ⭐ {hotel['rating']}\n"
            f"Price: {hotel['price']}\n\n"
        )
    return result

def get_attractions(city):
    attractions = attractions_data.get(city)
    if attractions is None:
        return "Sorry, no tourist attractions found for this city."
    result = f"Top attractions in {city}:\n\n"
    for attraction in attractions:
        result += f"• {attraction}\n"
    return result

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GROQS_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
    )
tools = [
{
"type": "function",
"function": {
"name": "get_weather",
"description": "Get the current weather for a city.",
"parameters": {
"type": "object",
"properties": {

"city": {
"type": "string",
"description": "Name of the city"
}
},
"required": ["city"]
}
}
},

{
"type": "function",
"function": {
"name": "search_flights",
"description": "Find available flights to a destination.",
"parameters": {
"type": "object",
"properties": {
"destination": {
"type": "string",
"description": "Destination city"
}
},
"required": ["destination"]
}
}

},

{
"type": "function",
"function": {
"name": "find_hotels",
"description": "Find hotels in a city.",
"parameters": {
"type": "object",
"properties": {
"city": {
"type": "string",
"description": "Name of the city"
}
},
"required": ["city"]
}
}
},

{
"type": "function",
"function": {
"name": "get_attractions",
"description": "Get popular tourist attractions in a city.",
"parameters": {

"type": "object",
"properties": {
"city": {
"type": "string",
"description": "Name of the city"
}
},
"required": ["city"]
}
}
}
]
user_question = input("You: ") #Ask the ai a question

response = client.chat.completions.create(
model="llama-3.3-70b-versatile",
messages=[
{
"role": "user",
"content": user_question
}
],
tools=tools,
tool_choice="auto"
)
message = response.choices[0].message

# Did the AI choose a tool?
if message.tool_calls:

    tool_call = message.tool_calls[0]

    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

# Execute the correct tool
if tool_name == "get_weather":

    tool_result = get_weather(arguments["city"])

elif tool_name == "search_flights":
        tool_result = search_flights(arguments["destination"])

elif tool_name == "find_hotels":
        tool_result = find_hotels(arguments["city"])

elif tool_name == "get_attractions":
        tool_result = get_attractions(arguments["city"])

else:
        tool_result = "Unknown tool."

print("\n===== TOOL RESULT =====")
print(tool_result)
print("=======================\n")
messages = [
    {
        "role": "user",
        "content": user_question
    },
    message,
    {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": tool_result
    }
]

final_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages
    )

print("TravelMate AI:\n")
print(final_response.choices[0].message.content)