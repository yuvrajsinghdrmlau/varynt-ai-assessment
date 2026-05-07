def route_request(task):

    providers = {
        "image": "OpenAI Image API",
        "video": "Runway API",
        "voice": "ElevenLabs API"
    }

    provider = providers.get(task, "Unknown Provider")

    return {
        "task": task,
        "provider": provider
    }