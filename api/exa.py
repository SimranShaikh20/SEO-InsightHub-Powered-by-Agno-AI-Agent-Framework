EXA_API_KEY = "1ab45d41-a057-45db-92be-40fe08fdd994"

def fetch_keywords(keywords):
    # TODO: Use EXA_API_KEY in real requests
    print(f"Using Exa API Key: {EXA_API_KEY}")
    return {
        "trending_keywords": [kw + " trends" for kw in keywords],
        "search_volume": {kw: 500 + i * 20 for i, kw in enumerate(keywords)}
    }
