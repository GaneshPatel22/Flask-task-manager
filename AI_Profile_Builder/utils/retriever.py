import requests


def get_wikipedia_info(person_name):

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{person_name.replace(' ', '_')}"

    headers = {
        "User-Agent": "AIProfileBuilder/1.0"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code != 200:
            return {
                "text": "No Wikipedia information found.",
                "url": "",
                "image": ""
            }

        data = response.json()

        return {
            "text": data.get("extract", "No summary available."),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
            "image": data.get("thumbnail", {}).get("source", "")
        }

    except Exception as e:

        return {
            "text": f"Error: {str(e)}",
            "url": "",
            "image": ""
        }


def get_news(person_name):

    # News API can be added later

    return {
        "text": "",
        "sources": []
    }


def get_context(person_name):

    wiki = get_wikipedia_info(person_name)

    news = get_news(person_name)

    context = wiki["text"]

    if news["text"]:

        context += "\n\nRecent News\n"

        context += news["text"]

    sources = []

    if wiki["url"]:
        sources.append(wiki["url"])

    sources.extend(news["sources"])

    return {

        "context": context,

        "sources": sources,

        "image": wiki["image"]

    }


if __name__ == "__main__":

    result = get_context("Elon Musk")

    print(result)