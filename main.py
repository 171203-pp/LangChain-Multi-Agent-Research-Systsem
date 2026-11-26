from src.tools.tools import web_search,scrape_url

result = scrape_url.invoke({
    "url": "https://aimagazine.com/"
})
print(result)