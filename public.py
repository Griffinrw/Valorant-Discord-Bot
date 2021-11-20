import valorant

KEY = "ENTER YOUR KEY HERE"
client = valorant.Client(KEY)



global valid_commands
valid_commands = ['!leaderboard', '!agents', '!gunbuddies', '!maps', '!skins', '!sprays', '!playercards', '!playertitles', '!commands', '!serverstatus', '!stop']



def print_leaderboard():
    '''prints out the top 100 leaderboard of the NA region'''

    counter = 0
    leaderboard = client.get_leaderboard()
    for player in leaderboard.players:
        counter += 1
        try:
            print(str(counter) + '.', player.rankedRating, player.gameName)
        except:
            #if there is a player who has a private profile, it lists them as 'Secret Agent' instead
            print(str(counter) + '.', player.rankedRating, 'Secret Agent')

def print_agents():
    '''prints out all of the playable agents in Valorant'''
    agents = client.get_characters()
    agent_names = []
    for agent in agents:
        if agent.name != 'Null UI Data!':
            #not sure why this is here at the end but the user doesn't want to see it
            agent_names.append(agent.name)

    for agent in sorted(agent_names):
        #sorts the names in alphabetical order
        print(agent)



def print_gunbuddies():
    '''prints out all of the gun buddies in Valorant'''
    gun_buddies = client.get_charms()
    gun_buddy_names_sorted = []

    for gun_buddy in gun_buddies:
        gun_buddy_names_sorted.append(gun_buddy.name)

    for gun_buddy in sorted(gun_buddy_names_sorted):
        print(gun_buddy)


def print_maps():
    '''prints out all of playable maps in Valorant'''
    maps = client.get_maps()
    map_list = []
    for map in maps:
        if map.name != 'Null UI Data!' and map.name != 'The Range':
            map_list.append(map.name)

    for map in sorted(map_list):
        print(map)


def print_skins():
    '''prints out all of the skins in Valorant'''
    skins = client.get_skins()
    skin_list = []
    for skin in skins:
        if skin.name != 'Null UI Data!':
            skin_list.append(skin.name)

    for skin in sorted(skin_list):
        print(skin)


def print_sprays():
    '''prints out all of the sprays in Valorant'''
    sprays = client.get_sprays()
    sprays_list = []
    for spray in sprays:
        if spray.name != 'Null UI Data!':
            sprays_list.append(spray.name)

    for spray in sorted(sprays_list):
        print(spray)


def print_playercards():
    '''prints out all of the playercards in Valorant'''
    playercards = client.get_player_cards()
    playercardlist = []
    for cards in playercards:
        if cards.name != 'Null UI Data!':
            playercardlist.append(cards.name)

    for card in sorted(playercardlist):
        print(card)



def print_playertitles():
    '''prints out all of the playertitles in Valorant'''
    titles = client.get_player_titles()
    titlelist = []
    for title in titles:
        if title.name != 'Null UI Data!':
            titlelist.append(title.name)

    for title in sorted(titlelist):
        print(title)

def print_serverstatus():
    '''prints out the current server status'''
    status = client.get_platform_status()
    if len(status.maintenances) == 0:
        print('no scheduled maintenance')
    if len(status.incidents) == 0:
        print('no current incidents')

def print_commands():
    '''prints out the list of acceptable commands to the user'''
    for command in valid_commands:
        print(command)


if __name__ == '__main__':
    user_input = ''
    while user_input != '!stop':
        user_input = input('please enter a command (type !commands for more info)')
        if user_input == '!leaderboard':
            print_leaderboard()
        elif user_input == '!agents':
            print_agents()
        elif user_input == '!gunbuddies':
            print_gunbuddies()
        elif user_input == '!maps':
            print_maps()
        elif user_input == '!skins':
            print_skins()
        elif user_input == '!sprays':
            print_sprays()
        elif user_input == '!playercards':
            print_playercards()
        elif user_input == '!playertitles':
            print_playertitles()
        elif user_input == '!serverstatus':
            print_serverstatus()
        elif user_input == '!commands':
            print_commands()


