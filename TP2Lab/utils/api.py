import requests

def call_slm(prompt):

    url = "https://reality.utad.net/slm"

    data = {
        "model": "llama-3.2-1b-instruct",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:

        response = requests.post(
            url,
            json=data
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "error": str(e)
        }
