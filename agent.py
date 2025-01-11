from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio

llm = ChatOpenAI(model="gpt-4o")

browser = Browser(
    config=BrowserConfig(
        headless=False,
        chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    )
)

async def main():
    agent = Agent(
        task="Find a one-way flight from Bali to Oman on 12 January 2025 on Google Flights. Return me the cheapest option.",
        llm=llm,
        browser=browser
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
