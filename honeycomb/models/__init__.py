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
        print("Agregando nodo:", repr(cell1), type(cell1))
        print("cell1.title:", getattr(cell1, "title", None))
        print("cell1.contents:", getattr(cell1, "contents", None))

        app_root.add_node(cell1)
        app_root.add_edge(
            str(cell1.__parent__.id),
            {
                "source": str(cell1.__parent__.id),
                "target": str(cell1.id),
                "id": str(uuid.uuid4()),
                "type": "custom-label",
                "label": "",
                "data": {"hasArrow": False}
            }
        )

         # Nodo de Rich Text

        icon = CellIcon('logo', title="Bee Logo", icon="🐝")
        icon.__parent__ = hc
        hc['logo'] = icon

        app_root.add_node(icon)
        app_root.add_edge(
            str(icon.__parent__.id),
            {
                "source": str(icon.__parent__.id),
                "target": str(icon.id),
                "id": str(uuid.uuid4()),
                "type": "custom-label",
                "label": "",
                "data": {"hasArrow": False}
            }
        )

        web = CellWebContent('link', title="Website", url="https://www.wikipedia.org")
        web.__parent__ = hc
        hc['link'] = web

        app_root.add_node(web)
        app_root.add_edge(
            str(web.__parent__.id),
            {
                "source": str(web.__parent__.id),
                "target": str(web.id),
                "id": str(uuid.uuid4()),
                "type": "custom-label",
                "label": "",
                "data": {"hasArrow": False}
            }
        )

         # Nodo de Animación

        animation = CellAnimation('bee-dance', url="/static/bee-dance.gif", title="Bee Dance", icon="🐝")
        animation.__parent__ = hc
        hc['bee-dance'] = animation

        app_root.add_node(animation)
        app_root.add_edge(
            str(animation.__parent__.id),
            {
                "source": str(animation.__parent__.id),
                "target": str(animation.id),
                "id": str(uuid.uuid4()),
                "type": "custom-label",
                "label": "",
                "data": {"hasArrow": False}
            }
        )

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

        app_root.add_node(game_cell)
        app_root.add_edge(
            str(game_cell.__parent__.id),
            {
                "source": str(game_cell.__parent__.id),
                "target": str(game_cell.id),
                "id": str(uuid.uuid4()),
                "type": "custom-label",
                "label": "",
                "data": {"hasArrow": False}
            }
        )

         # Nodo del juego de Unity si no existe

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

            app_root.add_node(unity_game_cell)
            app_root.add_edge(
                str(unity_game_cell.__parent__.id),
                {
                    "source": str(unity_game_cell.__parent__.id),
                    "target": str(unity_game_cell.id),
                    "id": str(uuid.uuid4()),
                    "type": "custom-label",
                    "label": "",
                    "data": {"hasArrow": False}
                }
            )
            print(f"Se agregó el juego '{unity_game_name}'")
        
        zodb_root['app_root'] = app_root
        print("Nodos en índice:", list(app_root.__nodes__.keys()))
    return zodb_root['app_root']