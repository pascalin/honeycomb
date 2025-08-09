from .beehive import *

def appmaker(zodb_root):
    if 'app_root' not in zodb_root:
        app_root = BeeHive()
        
        # --- Creación del Honeycomb por defecto ---
        hc = Honeycomb('default', "Convida Abejas")
        hc.__parent__ = app_root
        app_root['default'] = hc

        cell1 = CellText('intro', "Welcome text", title="Introduction")
        cell1.__parent__ = hc
        hc['intro'] = cell1

        icon = CellIcon('logo', title="Bee Logo", icon="🐝")
        icon.__parent__ = hc
        hc['logo'] = icon

        web = CellWebContent('link', title="Website", url="https://www.wikipedia.org")
        web.__parent__ = hc
        hc['link'] = web

        animation = CellAnimation('bee-dance', url="/static/bee-dance.gif", title="Bee Dance", icon="🐝")
        animation.__parent__ = hc
        hc['bee-dance'] = animation

        # --- Creación de juegos ---
        games_hc = Honeycomb('panal-de-juegos', "Panal de Juegos")
        games_hc.__parent__ = app_root
        app_root['panal-de-juegos'] = games_hc

        game_url = '/static/serpiente/index.html'
        game_cell = CellWebContent(
            name='juego-de-serpiente',
            title='Juego de la Serpiente',
            url=game_url
        )
        game_cell.__parent__ = games_hc
        games_hc['juego-de-serpiente'] = game_cell

        unity_game_name = 'juego-unity'
        if unity_game_name not in games_hc:
            unity_game_url = '/static/WEB/index.html'

            unity_game_cell = CellWebContent(
                name=unity_game_name,
                title='Juego de Unity',
                url=unity_game_url
            )
            unity_game_cell.__parent__ = games_hc
            games_hc[unity_game_name] = unity_game_cell
            print(f"Se agregó el juego '{unity_game_name}'")
        
        zodb_root['app_root'] = app_root
    return zodb_root['app_root']