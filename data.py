game_info = {
  "name" : "[place holder] ADVENTURE woo wow amazing so cool yes yes mmmmmmmmmmmm",
  "creator" : "me, not you, ME",
  "text_speed" : 0.05
}


start_stats = {
  'items' : ["small health potion","place_holder"],
  'coins' : 0,
  'stats' : {
    "health" : 100,
    "str" : 1,
    "def" : 1,
    "dex" : 1,
    'max_mana' : 10
  },
  'abilities' : ['bite'],
  'fights_won' : []
}


rooms = {
  1 : {
  "info" : "you are at the forest crossroads there are 2 paths you can take 1 goes to the town the outher goes deeper into the forest. what path do you want to take?",
  "options" : {
    "amount" : 2,
      1 : {
        "name" : "to the town",
        "type" : "room",
        "number" : 2
      },
      2 : {
        "name" : "deeper",
        "type" : "fight",
        "number" : 1
      }
    }
  },
  2 : {
    "info" : "town",
    "options" : {
      "amount" : 3,
      1 : {
        "name" : "back to the cross roads",
        "type" : "room",
        "number" : 1
      },
      2 : {
        "name" : "talk to billy bob joe",
        "type" : "person",
        "number" : 1
      },
      3 : {
        "name" : "to the shoppy shop",
        "type" : "shop",
        "number" : 1
      }
    }
  },
  3 : {
    "info" : "deeper into forest",
    "options" : {
      "amount" : 2,
      1 : {
        "name" : "back to the cross roads",
        "type" : "room",
        "number" : 1
      },
      2 : {
        "name" : "fight the [place holder] army",
        "type" : "fight",
        "number" : 2
      }
    }
  }
}

fights = {
  1 : {
    "info" : "you go deeper into the forest and find a monster!",
    "enemy" : "[place holder]",
    "level" : 1,
    "place" : 3,
    "repeat" : 0,
    "spawn_chance %" : 100,
    "rewards" : {
      "coins" : 10,
      "items" : [],
    }
  },
  2 : {
    "info" : "[holder place]",
    "enemy" : "[place holder]",
    "level" : 1,
    "place" : 3,
    "repeat" : 1,
    "spawn_chance %" : 100,
    "rewards" : {
      "coins" : 10,
      "items" : ["small health potion","small health potion","small health potion"]
    }
  }
}

enemys = {
  "[place holder]" : {
    "image" : """
    b
    e
    a
    n
    s""",
    "health" : 5,
    "str" : 1,
    "def" : 1,
    "dex" : 1
  }
}

items = {
  "small health potion" : {
    "type" : "heal",
    "amount" : 10,
    "consume/equip" : "consume",
    "message" : "drink a small health potion (heals 10)"
  },
  "place_holder" : {
    "type" : "hand",
    "amount" : 10,
    "consume/equip" : "equip",
    "message" : "equip place holder"
  }
}

abilities = {
  'bite' : {
    'type' : 'damage',
    'amount' : 2,
    'message' : 'bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! bite them! (deals 2 damage)',
    'cost' : 2
  }
}

people = {
  1 : {
    "name" : "billy bob joe",
    "location" : 2,
    "quests" : {
      1 : {
        "trigger_quest" : 0,
        "give_text" : "hi can you go kill the monster in the forest for me?",
        "active_text" : "shoo now go kill the monster",
        "reward" : {
          "text" : "thank you for killing the monster here is your reward",
          "coins" : 10,
          "items" : ["small health potion","small health potion"]
        },
        "completed_text" : "thank you for killing the monster"
      }
    }
  }
}
quests = {
  1 : {
    "type" : "kill",
    "number" : 1
  }
}

shops = {
  1 : {
  "name" : "shoppy shop",
  "info" : "welcome to shoppy shop what do ye want to buy?!?!?!?!?!?!",
  "items" : {
    "items" : ["small health potion"],
    "small health potion" : 10
    },
  "area" : 2
  }
}