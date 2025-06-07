print("Hello there! Welcome to CryptoSquad!\nI am your AI assisstant and your buddy in eevery step of the way.\nAsk me anything from profitability to efficiency of Bitcoin ,Ethereum and Cardanno.")
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}
def get_response(user_query) :
  user_query = user_query.lower()
  if "sustainable"  in user_query:
    recommend=max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    return f"Go for {recommend} as it has the highest sustainability score of {crypto_db[recommend]['sustainability_score']*10}/10."
  elif "trending" in user_query or "growth" in user_query:
    trending_cryptos = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]]

    if trending_cryptos:
      return f"Currently, {', '.join(trending_cryptos)} are trending with a rising price trend."
    else:
      return "No cryptocurrencies are currently trending with a rising price trend."
  elif "best" in user_query or "recommend" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 7:
                return f" {name} is both rising and sustainable! A solid choice."
        return " Can't find one that fits both profitability and sustainability."

  elif "bitcoin" in user_query:
    return f" Bitcoin: Trend - {crypto_db['Bitcoin']['price_trend']}, Energy Use - {crypto_db['Bitcoin']['energy_use']}, Sustainability Score - {crypto_db['Bitcoin']['sustainability_score']}"

  elif "cardano" in user_query:
    return f" Cardano: Trend - {crypto_db['Cardano']['price_trend']}, Energy Use - {crypto_db['Cardano']['energy_use']}, Sustainability Score - {crypto_db['Cardano']['sustainability_score']}"

  elif "ethereum" in user_query:
    return f" Ethereum: Trend - {crypto_db['Ethereum']['price_trend']}, Energy Use - {crypto_db['Ethereum']['energy_use']}, Sustainability Score - {crypto_db['Ethereum']['sustainability_score']}"

  elif "help" in user_query:
    return " Ask things like 'Which crypto is trending?', 'What's most sustainable?', or 'Tell me about Cardano'."

  elif "exit" in user_query or "bye" in user_query:
    return " Goodbye! Remember: Crypto is risky—do your own research!"

  else:
    return " I'm not sure how to help with that. Try asking about trending, sustainable, or specific coins."
  
while True:
    user_query = input("\nYou: ")
    response = get_response(user_query)
    print("CryptoBuddy:", response)
    if "goodbye" in response.lower():
        break



 