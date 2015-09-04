###############################################################################
# This script populates the database with 8 genres and 33 games               #
#                                                                             #
# The script replicates data retrieved from steam.com and populates the       #
# database with information from 33 different games belonging to 8 different  #
# genres                                                                      #
###############################################################################

import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Genre, Game


# define the flask session for connecting with the previously created
# SQLite database
engine = create_engine('sqlite:///game_catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# first, the entire database is cleared
session.query(Game).delete()
session.query(Genre).delete()
session.commit()


# Add the general genres to the catalog
genre1 = Genre(name="Action", id=1)
session.add(genre1)

genre2 = Genre(name="Adventure", id=2)
session.add(genre2)

genre3 = Genre(name="Indie", id=3)
session.add(genre3)

genre4 = Genre(name="Racing", id=4)
session.add(genre4)

genre5 = Genre(name="RPG", id=5)
session.add(genre5)

genre6 = Genre(name="Simulation", id=6)
session.add(genre6)

genre7 = Genre(name="Sports", id=7)
session.add(genre7)

genre8 = Genre(name="Strategy", id=8)
session.add(genre8)
session.commit()

# Add action games
game = Game(title="METAL GEAR SOLID V: GROUND ZEROES",
            description="World-renowned Kojima Productions brings the Metal "
                        "Gear Solid franchise to Steam with METAL GEAR "
                        "SOLID V: GROUND ZEROES. Play as the legendary hero "
                        "Snake and infiltrate a Cuban military base to rescue "
                        "the hostages. Can you make it out alive?",
            releaseDate=datetime.date(year=2014, month=12, day=18),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/"
                       "311340/header.jpg?t=1438910624",
            genre_id=1)
session.add(game)
session.commit()

game = Game(title="Grand Theft Auto V",
            description="When a young street hustler, a retired bank robber "
                        "and a terrifying psychopath find themselves "
                        "entangled with some of the most frightening and "
                        "deranged elements of the criminal underworld, the "
                        "U.S. government and the entertainment industry, they "
                        "must pull off a series of dangerous heists to "
                        "survive in a ruthless city in which they can trust "
                        "nobody, least of all each other.",
            releaseDate=datetime.date(year=2015, month=4, day=14),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/271590/"
                       "header.jpg?t=1436378200",
            genre_id=1)
session.add(game)
session.commit()

game = Game(title="Counter-Strike: Global Offensive",
            description="Counter-Strike: Global Offensive (CS: GO) will "
                        "expand upon the team-based action gameplay that it "
                        "pioneered when it was launched 14 years ago. CS: GO "
                        "features new maps, characters, and weapons and "
                        "delivers updated versions of the classic CS content "
                        "(de_dust, etc.).",
            releaseDate=datetime.date(year=2012, month=8, day=21),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/730/"
                       "header.jpg?t=1440086526",
            genre_id=1)
session.add(game)
session.commit()

game = Game(title="Call of Duty",
            description="Call of Duty delivers the gritty realism and "
                        "cinematic intensity of World War II's epic "
                        "battlefield moments like never before - through "
                        "the eyes of citizen soldiers and unsung heroes from "
                        "an alliance of countries who together helped shape "
                        "the course of modern history.",
            releaseDate=datetime.date(year=2003, month=10, day=29),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/2620/"
                       "header.jpg?t=1415927637",
            genre_id=1)
session.add(game)
session.commit()

game = Game(title="Company of Heroes",
            description="Delivering a visceral WWII gaming experience, "
                        "Company of Heroes redefines real time strategy "
                        "gaming by bringing the sacrifice of heroic soldiers, "
                        "war-ravaged environments, and dynamic battlefields "
                        "to life.",
            releaseDate=datetime.date(year=2006, month=9, day=11),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/4560/"
                       "header.jpg?t=1440800772",
            genre_id=1)
session.add(game)
session.commit()

game = Game(title="Left 4 Dead",
            description="From Valve (the creators of Counter-Strike, "
                        "Half-Life and more) comes Left 4 Dead, a co-op "
                        "action horror game for the PC and Xbox 360 that "
                        "casts up to four players in an epic struggle for "
                        "survival against swarming zombie hordes and "
                        "terrifying mutant monsters.",
            releaseDate=datetime.date(year=2008, month=11, day=17),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/500/"
                       "header.jpg?t=1432336121",
            genre_id=1)
session.add(game)
session.commit()


# Add adventure games
game = Game(title="The Elder Scrolls V: Skyrim",
            description="EPIC FANTASY REBORN The next chapter in the highly "
                        "anticipated Elder Scrolls saga arrives from the "
                        "makers of the 2006 and 2008 Games of the Year, "
                        "Bethesda Game Studios. Skyrim reimagines and "
                        "revolutionizes the open-world fantasy epic, bringing "
                        "to life a complete virtual world open for you to "
                        "explore",
            releaseDate=datetime.date(year=2011, month=11, day=10),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/72850/"
                       "header.jpg?t=1438622529",
            genre_id=2)
session.add(game)
session.commit()

game = Game(title="DayZ",
            description="Welcome to the world of DayZ, hit by a new and "
                        "presently unknown infection which has wiped out "
                        "most of the world's population. You are one of the "
                        "few that have survived and now you must search this "
                        "new wasteland in order to fight for your life "
                        "against what is left of the indigenous population "
                        "now infected with the disease. Go solo, team up "
                        "with friends or take on the world, as you choose "
                        "your path in this brutal and chilling landscape "
                        "using whatever means you stumble upon to survive.",
            releaseDate=datetime.date(year=2013, month=12, day=16),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/221100/"
                       "header.jpg?t=1427963019",
            genre_id=2)
session.add(game)
session.commit()

game = Game(title="The Witcher",
            description="Become The Witcher, Geralt of Rivia, a legendary "
                        "monster slayer caught in a web of intrigue woven by "
                        "forces vying for control of the world. Make "
                        "difficult decisions and live with the consequences "
                        "in an game that will immerse you in an extraordinary "
                        "tale like no other. Representing the pinnacle of "
                        "storytelling in role-playing games, The Witcher "
                        "shatters the line between good and evil in a world "
                        "where moral ambiguity reigns. The Witcher emphasizes "
                        "story and character development in a vibrant world "
                        "while incorporating tactically-deep real-time "
                        "combat like no game before it.",
            releaseDate=datetime.date(year=2008, month=9, day=16),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/20900/"
                       "header.jpg?t=1424254491",
            genre_id=2)
session.add(game)
session.commit()

game = Game(title="Portal",
            description="Portal is a new single player game from Valve. Set "
                        "in the mysterious Aperture Science Laboratories, "
                        "Portal has been called one of the most innovative "
                        "new games on the horizon and will offer gamers "
                        "hours of unique gameplay.",
            releaseDate=datetime.date(year=2007, month=10, day=10),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/400/"
                       "header.jpg?t=1418842605",
            genre_id=2)
session.add(game)
session.commit()


# Add indie games
game = Game(title="Terraria",
            description="Dig, fight, explore, build! Nothing is impossible "
                        "in this action-packed adventure game. Four Pack "
                        "also available!",
            releaseDate=datetime.date(year=2011, month=5, day=16),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/105600/"
                       "header.jpg?t=1439404386",
            genre_id=3)
session.add(game)
session.commit()

game = Game(title="Fight The Dragon",
            description="A COMMUNITY CREATED Hack'n Slash RPG where players "
                        "can team up and tackle exciting adventures made by "
                        "other community members in our in-game Adventure "
                        "Construction Kit - It's DIABLO meets LITTLE BIG "
                        "PLANET!",
            releaseDate=datetime.date(year=2014, month=12, day=4),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/250560/"
                       "header.jpg?t=1440971228",
            genre_id=3)
session.add(game)
session.commit()

game = Game(title="Kerbal Space Program",
            description="Kerbal Space Program has left Early Access. 1.0 "
                        "comes packed with new features, optimizations, "
                        "bugfixing, and tons more! Conquering Space Was "
                        "Never This Easy!",
            releaseDate=datetime.date(year=2015, month=4, day=27),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/220200/"
                       "header.jpg?t=1430202234",
            genre_id=3)
session.add(game)
session.commit()

game = Game(title="Subnautica",
            description="Descend into the depths of an alien underwater "
                        "world filled with wonder and peril. Craft equipment, "
                        "pilot submarines, terraform voxel terrain, and "
                        "out-smart wildlife to explore lush coral reefs, "
                        "volcanoes, cave systems, and more - All while "
                        "trying to survive.",
            releaseDate=datetime.date(year=2014, month=12, day=16),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/264710/"
                       "header.jpg?t=1439370291",
            genre_id=3)
session.add(game)
session.commit()


# Add racing games
game = Game(title="DiRT Rally",
            description="DiRT Rally marks the return to a more authentic and "
                        "dangerous off-road racing experience. We deliver "
                        "free new content every month, plus a continuous "
                        "stream of gameplay improvements.",
            releaseDate=datetime.date(year=2015, month=4, day=27),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/310560/"
                       "header.jpg?t=1440692126",
            genre_id=4)
session.add(game)
session.commit()

game = Game(title="Project CARS",
            description="Project CARS is the ultimate driver journey! ",
            releaseDate=datetime.date(year=2015, month=5, day=6),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/234630/"
                       "header.jpg?t=1441055118",
            genre_id=4)
session.add(game)
session.commit()

game = Game(title="F1 2015",
            description="Race like a champion in F1 2015 A stunning new game "
                        "engine and all-new broadcast presentation puts you "
                        "in the heart of the action.",
            releaseDate=datetime.date(year=2015, month=7, day=9),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/286570/"
                       "header.jpg?t=1440411827",
            genre_id=4)
session.add(game)
session.commit()

game = Game(title="GRID",
            description="Discover a stunning world of motor sport brought "
                        "to life, from racing muscle cars through the iconic "
                        "streets of San Francisco and competing in the "
                        "legendary 24 hours of Le Mans to drifting around "
                        "the docks of Yokohama.",
            releaseDate=datetime.date(year=2008, month=6, day=4),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/12750/"
                       "header.jpg?t=1440420907",
            genre_id=4)
session.add(game)
session.commit()


# Add RPG games
game = Game(title="Fallout",
            description="You've just unearthed the classic post-apocalyptic "
                        "role-playing game that revitalized the entire CRPG "
                        "genre. The Fallout SPECIAL system allows "
                        "drastically different types of characters, "
                        "meaningful decisions and development that puts you "
                        "in complete control. Explore the devastated ruins "
                        "of a golden age",
            releaseDate=datetime.date(year=1997, month=11, day=1),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/38400/"
                       "header.jpg?t=1406646326",
            genre_id=5)
session.add(game)
session.commit()

game = Game(title="Mount & Blade: Warband",
            description="In a land torn asunder by incessant warfare, it is "
                        "time to assemble your own band of hardened warriors "
                        "and enter the fray. Lead your men into battle, "
                        "expand your realm, and claim the ultimate prize: "
                        "the throne of Calradia!",
            releaseDate=datetime.date(year=2010, month=3, day=31),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/48700/"
                       "header.jpg?t=1440696051",
            genre_id=5)
session.add(game)
session.commit()

game = Game(title="Heroes of Might & Magic V",
            description="Witness the amazing evolution of the genre-defining "
                        "strategy game as it becomes a next-generation "
                        "phenomenon, melding classic deep fantasy with "
                        "next-generation visuals and gameplay. In the "
                        "renowned Might & Magic universe, demon swarms "
                        "spread chaos over the land in a relentless assault.",
            releaseDate=datetime.date(year=2006, month=5, day=23),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/15170/"
                       "header.jpg?t=1376847033",
            genre_id=5)
session.add(game)
session.commit()


# Add simulation games
game = Game(title="Cities: Skylines",
            description="Cities: Skylines is a modern take on the classic "
                        "city simulation. The game introduces new game play "
                        "elements to realize the thrill and hardships of "
                        "creating and maintaining a real city whilst "
                        "expanding on some well-established tropes of the "
                        "city building experience.",
            releaseDate=datetime.date(year=2015, month=3, day=10),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/255710/"
                       "header.jpg?t=1430910532",
            genre_id=6)
session.add(game)
session.commit()

game = Game(title="Sid Meier's Civilization V",
            description="Create, discover, and download new player-created "
                        "maps, scenarios, interfaces, and more!",
            releaseDate=datetime.date(year=2010, month=9, day=23),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/8930/"
                       "header.jpg?t=1436891075",
            genre_id=6)
session.add(game)
session.commit()

game = Game(title="LEGO Worlds",
            description="In a galaxy of procedural worlds made entirely from "
                        "LEGO bricks, will you... EXPLORE environments "
                        "filled with adventure, then alter them? DISCOVER "
                        "secrets and treasures, then play with them? CREATE "
                        "your own models, then make a world your own? In "
                        "LEGO Worlds, it's up to you...",
            releaseDate=datetime.date(year=2015, month=6, day=1),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/332310/"
                       "header.jpg?t=1440440685",
            genre_id=6)
session.add(game)
session.commit()

game = Game(title="Farming Simulator 15",
            description="Welcome to the new generation of Farming Simulator! "
                        "With a brand new graphics and physics engine, "
                        "Farming Simulator 15 offers an immense open world, "
                        "filled with details and visual effects transporting "
                        "the Farming Simulator franchise to a new era.",
            releaseDate=datetime.date(year=2014, month=10, day=30),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/313160/"
                       "header.jpg?t=1435307365",
            genre_id=6)
session.add(game)
session.commit()


# Add Sports games
game = Game(title="Football Manager 2015",
            description="Football Manager 2015, the latest in the "
                        "award-winning and record-breaking series, is coming "
                        "to PC, Macintosh and Linux computers in November "
                        "2014. Football Manager is the most realistic, "
                        "in-depth and immersive simulation of football "
                        "management available, putting you in the hot-seat "
                        "of almost any",
            releaseDate=datetime.date(year=2014, month=11, day=1),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/295270/"
                       "header.jpg?t=1433503204",
            genre_id=7)
session.add(game)
session.commit()

game = Game(title="NBA 2K16",
            description="NBA 2K is back with the most true-to-life NBA "
                        "experience to date with NBA 2K16. Featuring an "
                        "all-new MyCAREER experience written, directed & "
                        "produced by acclaimed filmmaker Spike Lee.",
            releaseDate=datetime.date(year=2015, month=9, day=29),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/370240/"
                       "header.jpg?t=1440435013",
            genre_id=7)
session.add(game)
session.commit()

game = Game(title="Pro Evolution Soccer 2015",
            description="KONAMI returns to the field with PES 2015, a return "
                        "to core PES values. Thanks to the incredible FOX "
                        "Engine, PES 2015 delivers stunning visuals and "
                        "animation where the world's greatest players play "
                        "just their real-life counterparts, as PES ID ensures "
                        "that the whole team matches their playing style.",
            releaseDate=datetime.date(year=2014, month=11, day=12),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/287680/"
                       "header.jpg?t=1427883669",
            genre_id=7)
session.add(game)
session.commit()


# Add Strategy games
game = Game(title="Age of Empires III",
            description="Microsoft Studios brings you three epic Age of "
                        "Empires III games in one monumental collection for "
                        "the first time.",
            releaseDate=datetime.date(year=2009, month=9, day=15),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/105450/"
                       "header.jpg?t=1430149346",
            genre_id=8)
session.add(game)
session.commit()

game = Game(title="Command & Conquer: Red Alert 3",
            description="The desperate leadership of a doomed Soviet Union "
                        "travels back in time to change history and restore "
                        "the glory of Mother Russia. The time travel mission "
                        "goes awry, creating an alternate timeline where "
                        "technology has followed an entirely different "
                        "evolution, a new superpower has been thrust on "
                        "to the world stage",
            releaseDate=datetime.date(year=2008, month=10, day=28),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/17480/"
                       "header.jpg?t=1427136587",
            genre_id=8)
session.add(game)
session.commit()

game = Game(title="Empire: Total War",
            description="Command the seas, control the land, forge a new "
                        "nation, and conquer the globe.",
            releaseDate=datetime.date(year=2009, month=3, day=3),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/10500/"
                       "header.jpg?t=1435332925",
            genre_id=8)
session.add(game)
session.commit()

game = Game(title="XCOM: Enemy Unknown",
            description="XCOM: Enemy Unknown will place you in control of a "
                        "secret paramilitary organization called XCOM. As the "
                        "XCOM commander, you will defend against a terrifying "
                        "global alien invasion by managing resources, "
                        "advancing technologies, and overseeing combat "
                        "strategies and individual unit tactics.",
            releaseDate=datetime.date(year=2012, month=10, day=10),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/200510/"
                       "header.jpg?t=1413482568",
            genre_id=8)
session.add(game)
session.commit()

game = Game(title="Hearts of Iron III",
            description="Hearts of Iron III lets you play the most engaging "
                        "conflict in world history, World War 2, on all "
                        "fronts as any country and through multiple different "
                        "scenarios. Guide your nation to glory between 1936 "
                        "and 1948 and wage war, conduct diplomacy and build "
                        "your industry in the most detailed World War 2 "
                        "game ever",
            releaseDate=datetime.date(year=2009, month=8, day=7),
            pictureURL="http://cdn.akamai.steamstatic.com/steam/apps/25890/"
                       "header.jpg?t=1410853423",
            genre_id=8)
session.add(game)
session.commit()
