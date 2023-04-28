import discord
from discord.ext import commands
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from discord.ext import commands
import os
import time
from discord.ext import commands

client = discord.Client(intents=discord.Intents.all())

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")


@client.event
async def on_ready():
    while True:
        try:

            driver.get(
                "https://product link")


            time.sleep(3)

            price = driver.find_element(By.CLASS_NAME, "pdp-price").text

            new_price = int(price.lstrip("₹"))

        except:
            print("reload issue")
        channel = client.get_channel(channel name)
        await channel.send(f"Sweat Pants current price: {new_price}")
        await channel.send("Telling price again in 5 mins........")
        print(channel)

        if new_price < 1609:
            channel = client.get_channel(channel name)
            await channel.send("buying opportunity maybe")
            await channel.send("fSweat Pants current price: {new_price}")

        time.sleep(randint(300, 315))

client.run("TOKEN")
