#import packages
import data
from os import system, name
import time
import random
import math
import sys

def sleep(x):
  time.sleep(x)


def write(text,pause = data.game_info["text_speed"]):
  global dubug
  if debug == True:
    print(text)
  else:
    for x in text:
      print(x, end='')
      sys.stdout.flush()
      time.sleep(pause)
    print()


def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

#get start stats
items = data.start_stats['items']
coins = data.start_stats['coins']
stats = data.start_stats['stats']
abilities = data.start_stats['abilities']
fights_won = data.start_stats['fights_won']
equipped = {
  "equipped":[],
  "hand": "none"
}
active_quests = []
completed_quests = [0]

#room navagator
def room(num):
  global items,coins,stats,abilities,equipped,active_quests,completed_quests,fights_won,debug
  clear()
  if debug:
    print(f"items({items}),coins({coins}),stats({stats}),abilities({abilities}),equipped({equipped}),active_quests({active_quests}),completed_quests({completed_quests}),fights_won({fights_won}),debug({debug})")
  write(data.rooms[num]["info"])

  #print the options
  for option in range(1 , (data.rooms[num]["options"]["amount"] + 1)):
    write(f"press {option} to go {data.rooms[num]['options'][option]['name']}")
  choice = input("what do you want to do? \n")
  try:
    choice = int(choice)
  except:
    print("invalid input.")
    sleep(0.5)
    room(num)
  #go to next place
  if debug:
    if data.rooms[num]["options"][choice]["type"] == "room":
      room(data.rooms[num]["options"][choice]["number"])
    if data.rooms[num]["options"][choice]["type"] == "fight":
      fight(data.rooms[num]["options"][choice]["number"])
    if data.rooms[num]["options"][choice]["type"] == "shop":
      shop(data.rooms[num]["options"][choice]["number"])
    if data.rooms[num]["options"][choice]["type"] == "person":
      person(data.rooms[num]["options"][choice]["number"],0)
  else:
    try:
      if data.rooms[num]["options"][choice]["type"] == "room":
        room(data.rooms[num]["options"][choice]["number"])
      if data.rooms[num]["options"][choice]["type"] == "fight":
        fight(data.rooms[num]["options"][choice]["number"])
      if data.rooms[num]["options"][choice]["type"] == "shop":
        shop(data.rooms[num]["options"][choice]["number"])
      if data.rooms[num]["options"][choice]["type"] == "person":
        person(data.rooms[num]["options"][choice]["number"],0)
    except:
      print("invalid input.")
      sleep(0.5)
      room(num)

#combat handler
def fight(num):
  global items,coins,stats,abilities,equipped,active_quests,completed_quests,fights_won,debug
  if random.randint(0,100) > data.fights[num]["spawn_chance %"]:
    room(data.fights[num]["place"])
  if num in fights_won and data.fights[num]["repeat"] == 0:
    room(data.fights[num]["place"])
  
  self_health = stats["health"]
  enemy_health_start = (data.enemys[data.fights[num]["enemy"]]["health"] * (data.fights[num]["level"]))
  level = data.fights[num]["level"]
  
  enemy_health = enemy_health_start
  enemy = data.fights[num]['enemy']
  
  clear()
  write(data.fights[num]["info"])
  sleep(1)
  clear()
  print("""
******** **   ********  **      ** ********** **
/**///// /**  **//////**/**     /**/////**/// /**
/**      /** **      // /**     /**    /**    /**
/******* /**/**         /**********    /**    /**
/**////  /**/**    *****/**//////**    /**    /**
/**      /**//**  ////**/**     /**    /**    // 
/**      /** //******** /**     /**    /**     **
//       //   ////////  //      //     //     // """)
  sleep(0.5)
  clear()
  alive = True
  while alive:
    clear()
    print(data.enemys[enemy]["image"])
    if debug:
      print(f"items({items}),coins({coins}),stats({stats}),abilities({abilities}),equipped({equipped}),active_quests({active_quests}),completed_quests({completed_quests}),fights_won({fights_won}),debug({debug})")
    print(f"the {enemy} stares at you")
    print(f"health {self_health}/{stats['health']}")
    print(f"enemy health {enemy_health}/{enemy_health_start}")
    print("press 1 to attack")
    print("press 2 to look at your items")
    print("press 3 to look at your abilities")
    choice = input("what do you want to do?\n")
    try:
      choice = int(choice)
    except:
      print("invalid input.")
      continue
    if choice == 4:
      enemy_health = 0
      choice = 1
      
    if choice == 1:
      clear()
      damage = random.randint((stats["dex"] * 10) , ((stats["dex"] * 10) + 100))
      print(f"you did {(damage/100) * stats['str']}")
      if damage > 100:
        print("Crit!")
      enemy_health -= (damage/100) * stats['str']
      if enemy_health <= 0:
        print("you won!")
        fights_won.append(num)
        print("you got")
        print(f"{data.fights[num]['rewards']['coins']} coins")
        coins += data.fights[num]['rewards']['coins']
        for item in data.fights[num]["rewards"]['items']:
          print(item)
          items.append(item)
        input("press enter to continue")
        room(data.fights[num]["place"])
      sleep(1)
      clear()

    if choice == 2:
      clear()
      for item in range(0 , len(items)):
        if item in equipped["equipped"]:
          equip_dequip = "dequip"
        else:
          equip_dequip = "equip"
        print(f"press {item+1} to {data.items[items[item]]['message']}")
        a = item
      print(f"press {a+2} to go back")
      choice1 = input("what do you want to do? \n")
      try:
        choice1 = int(choice1)
      except:
        continue
      if choice1 != a+2:
        item = items[choice1-1]

        if data.items[item]["consume/equip"] == "consume":
          if data.items[item]["type"] == "heal":
            self_health += data.items[item]["amount"]
            if self_health > 100:
              self_health = 100
          items.remove(item)
          if data.items[item]["consume/equip"] == "equip":
            if data.items[item][type] == "hand":
              if equipped["hand"] != "none":
                equipped["equipped"].remove(equipped["hand"])
              equipped["hand"] = item
              equipped["equipped"].append(item)
        clear()
      continue
    damage = random.randint((data.enemys[enemy]["dex"] * 10) , (((data.enemys[enemy]["dex"] * level) * 10) + 100))
    print(f"the {data.fights[num]['enemy']} attacked and did {data.enemys[enemy]['str'] * level * damage/100}")
    self_health -= (data.enemys[enemy]['str'] * level) * damage/100
    if self_health <= 0:
      print("you done died")
      input("press enter to continue")
      room(1,items,coins-math.floor(coins*0.1),stats,abilities,equipped,active_quests,completed_quests,fights_won)
    sleep(1)
    
def shop(num):
  global items,coins,stats,abilities,equipped,active_quests,completed_quests,fights_won,debug
  while True:
    clear()
    if debug:
      print(f"items({items}),coins({coins}),stats({stats}),abilities({abilities}),equipped({equipped}),active_quests({active_quests}),completed_quests({completed_quests}),fights_won({fights_won}),debug({debug})")
    print(data.shops[num]["info"])
    print(f"you have {coins} coins")
    a = 1
    for item in data.shops[num]["items"]["items"]:
      print(f"press {a} for {item}")
      a += 1
    print(f"or press {a} to go back")
    choice = input("what do you want to do \n")
    if int(choice) == a:
      room(data.shops[num]["area"],)
    else:
      if coins < data.shops[num]["items"][data.shops[num]["items"]["items"][int(choice)-1]]:
        print("you dont have enough moneys")
        sleep(1)
      else:
        coins -= data.shops[num]["items"][data.shops[num]["items"]["items"][int(choice)-1]]
        items.append(data.shops[num]["items"]["items"][int(choice)-1])
        print(f"you got {data.shops[num]['items']['items'][int(choice)-1]}")
        input("press enter to continue")

def person(num,reward) :
  global items,coins,stats,abilities,equipped,active_quests,completed_quests,fights_won,debug
  clear()
  max = 0
  
  if debug:
   print(f"items({items}),coins({coins}),stats({stats}),abilities({abilities}),equipped({equipped}),active_quests({active_quests}),completed_quests({completed_quests}),fights_won({fights_won}),debug({debug})")
      
  for i in range(0,len(data.people[num]["text"]["quests"])):
    if data.people[num]["text"]["quests"][i] in completed_quests:
      if max < data.people[num]["text"]["quests"][i]:
        max = data.people[num]["text"]["quests"][i]
    
    if data.people[num]["text"][max]["type"] == "reward":
      if reward == 1:
        print(data.people[num]["text"][max][1]["text"])
        print("you got")
        print(f"{data.people[num]['text'][max][1]['coins']} coins")
        coins += data.fights[num]['rewards']['coins']
        for item in data.people[num]["text"][max][1]["rewards"]:
          items.append(item)
          print(item)
        input("press enter to continue")
        room(data.people[num]["area"],)
        
  if data.people[num]["text"][max]["type"] == "quest":
    
    if data.quests[data.people[num]["text"][max]["quest"]]["type"] == "kill":
      
      if data.quests[data.people[num]["text"][max]["quest"]]["number"] in fights_won: 
        completed_quests.append(data.people[num]["text"][max]["quest"])
        active_quests.remove(data.people[num]["text"][max]["quest"])
        person(num,1)
    
    if data.people[num]["text"][max]["quest"] not in active_quests:
      print(data.people[num]["text"][max][1])
      if input("accept y/n") == "y":
        active_quests.append(data.people[num]["text"][max]["quest"])
        room(data.people[num]["area"],)
      else:
        
        room(data.people[num]["area"],)
    else:
      
      print(data.people[num]["text"][max][2])
      input("press enter")
      room(data.people[num]["area"],)
        
        

def menu():
  global debug
  print("""
        [logo go logo go]
        [yes no logo]
        [need logo i do]
        [hehehehehehehehehehehehehehehehehheheeh]
        [HEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEHEH]
        [HAHAHHAHAHAHAHHAHAHAHAHAHAHAHAHAHAHAHAH]
                  pypg game engine
                    by mr.hooman""")
  print("loading")
  sleep(2)
  clear()
  print(data.game_info["name"])
  print(f"by {data.game_info['creator']}")
  choice = input("press enter to start")
  if choice == "d":
    debug = True
  else:
    debug = False
  room(1)

menu()