from ts3plugin import ts3plugin

import ts3lib, ts3defines
import requests
import json
import os

class poke2telegram(ts3plugin):
    name = "Poke2Telegram"
    requestAutoload = False
    version = "1.0"
    apiVersion = 21
    author = "dbene"
    description = "This is a plugin for sending pokes to a telegram user"
    offersConfigure = False
    commandKeyword = ""
    infoTitle = None
    menuItems = []#[(ts3defines.PluginMenuType.PLUGIN_MENU_TYPE_CLIENT, 0, "text", "icon.png")]
    hotkeys = []#[("keyword", "description")]

    config = {}
    with open(os.path.dirname(os.path.realpath(__file__)) + '/config.json') as json_file:  
        config = json.load(json_file)

    def __init__(self):
        ts3lib.printMessageToCurrentTab("Poke2Telegram has started!")

    def stop(self):
        ts3lib.printMessageToCurrentTab("Poke2Telegram has stopped :(")

    def onClientPokeEvent(self, schid, fromClientID, pokerName, pokerUniqueIdentity, message, ffIgnored):
        url = self.config["baseURI"] + self.config["botToken"] + "/sendMessage?chat_id=" + self.config["chatID"] + "&text=" + pokerName + ": " + message
        #ts3lib.printMessageToCurrentTab(url)

        r = requests.get(url)
        return False
