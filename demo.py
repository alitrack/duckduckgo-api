from httpx import get
def fetch_search_results(query):
    """
    Fetch search results for a given query.

    :param query: Search query string
    :return: List of search results
    """
    search = get('http://127.0.0.1:8000/search',
                 params={
                     'q': query,
                     'max_results': 3,
                 })

    snippets = ""
    for index, result in enumerate(search.json()):
        snippet = f'[{index + 1}] "{result["body"]}" URL:{result["href"]}.'
        snippets += snippet
    return [{'role': 'system', 'content': snippets}]

print(fetch_search_results("ChatGPT 最新版本？"))