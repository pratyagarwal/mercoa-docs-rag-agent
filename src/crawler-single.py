import asyncio
from crawl4ai import *

async def crawl_website(url: str, depth: int=3) -> str:
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url, depth=depth)
        return result.markdown

async def main():
    url = "https://mercoa.com/"
    depth = 3
    markdown_content = await crawl_website(url, depth)
    print("markdown_content", markdown_content)

if __name__ == "__main__":
    asyncio.run(main())
