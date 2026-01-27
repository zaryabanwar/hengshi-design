from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from app.db.session import create_db_engine
from app.models.world import WorldHotspot, WorldNode

SERVICE_NODE_DEFS: list[dict] = [
    {
        'key': 'strategy_architecture',
        'title': 'Strategy & Architecture',
        'description': 'Vision, discovery, and system direction.'
    },
    {
        'key': 'platform_engineering',
        'title': 'Platform & Product Engineering',
        'description': 'Modern platform and product execution.'
    },
    {
        'key': 'ai_systems',
        'title': 'AI Systems & Automation',
        'description': 'Intelligent systems and agentic workflows.'
    },
    {
        'key': 'spatial_immersive',
        'title': 'Spatial & Immersive',
        'description': 'Realtime 3D, WebGL, AR/VR experiences.'
    },
    {
        'key': 'product_design',
        'title': 'Product Design',
        'description': 'Experience engineering and design systems.'
    },
    {
        'key': 'cloud_devops',
        'title': 'Cloud & DevOps',
        'description': 'Reliability, CI/CD, and platform operations.'
    },
    {
        'key': 'security_trust',
        'title': 'Security & Trust',
        'description': 'Privacy, risk reduction, and secure delivery.'
    },
    {
        'key': 'data_platforms',
        'title': 'Data Platforms',
        'description': 'Data engineering, analytics, and governance.'
    },
    {
        'key': 'commerce_growth',
        'title': 'Commerce & Growth',
        'description': 'Commerce stacks, CMS, and growth tooling.'
    }
]

WORLD_NODE_DEFS: list[dict] = [
    {
        'key': 'exterior',
        'title': 'Hengshi HQ Exterior',
        'description': 'Approach the main entrance of Hengshi HQ.',
        'is_entry': True,
        'sort_order': 0,
        'camera_position': [18.0, 10.5, 24.0],
        'camera_target': [0.0, 3.2, 0.0],
        'camera_fov': 46
    },
    {
        'key': 'lobby',
        'title': 'Lobby',
        'description': 'Welcome to the Hengshi HQ lobby.',
        'is_entry': False,
        'sort_order': 1,
        'camera_position': [0.2, 1.6, 5.4],
        'camera_target': [0.0, 1.6, 0.0],
        'camera_fov': 50
    },
    *[
        {
            **node_def,
            'is_entry': False,
            'sort_order': index + 2
        }
        for index, node_def in enumerate(SERVICE_NODE_DEFS)
    ]
]

SERVICE_NODE_KEYS = {node['key'] for node in SERVICE_NODE_DEFS}
SERVICE_NODE_INDEX = {node['key']: index for index, node in enumerate(SERVICE_NODE_DEFS)}


def _camera_position(index: int) -> list[float]:
    return [round(index * 0.3, 2), 1.6, round(6.0 + index * 0.2, 2)]


def _camera_target(index: int) -> list[float]:
    return [round(index * 0.1, 2), 1.6, 0.0]


def _hotspot_positions(index: int) -> tuple[list[float], list[float], list[float]]:
    service = [round(0.2 + index * 0.05, 2), 1.2, round(-0.8 + index * 0.05, 2)]
    navigate = [round(1.4 + index * 0.05, 2), 1.1, round(-1.6 + index * 0.05, 2)]
    contact = [round(-1.2 - index * 0.02, 2), 1.1, round(-0.4 + index * 0.03, 2)]
    return service, navigate, contact


def seed_world(db: Session) -> tuple[int, int]:
    created_nodes = 0
    created_hotspots = 0

    total_nodes = len(WORLD_NODE_DEFS)
    for index, node_def in enumerate(WORLD_NODE_DEFS):
        node_key = node_def['key']
        next_key = WORLD_NODE_DEFS[(index + 1) % total_nodes]['key']
        next_title = WORLD_NODE_DEFS[(index + 1) % total_nodes]['title']

        service_index = SERVICE_NODE_INDEX.get(node_key, index)
        data = {
            **node_def,
            'is_entry': node_def.get('is_entry', False),
            'sort_order': node_def.get('sort_order', index),
            'camera_position': node_def.get('camera_position', _camera_position(service_index)),
            'camera_target': node_def.get('camera_target', _camera_target(service_index)),
            'camera_fov': node_def.get('camera_fov', 50)
        }

        node = db.execute(
            select(WorldNode).where(WorldNode.key == node_key)
        ).scalar_one_or_none()

        if node:
            for key, value in data.items():
                setattr(node, key, value)
        else:
            node = WorldNode(**data)
            db.add(node)
            db.flush()
            created_nodes += 1

        service_pos, navigate_pos, contact_pos = _hotspot_positions(service_index)
        hotspot_seeds = []

        if node_key in SERVICE_NODE_KEYS:
            hotspot_seeds.append(
                {
                    'key': 'service_panel',
                    'title': f'{node_def["title"]} Services',
                    'description': 'Open services for this room.',
                    'kind': 'OPEN_PANEL',
                    'position': service_pos,
                    'payload': {
                        'panel': 'service_category',
                        'category': node_key
                    },
                    'sort_order': 0
                }
            )

        hotspot_seeds.append(
            {
                'key': 'navigate_next',
                'title': f'Next: {next_title}',
                'description': 'Move to the next room.',
                'kind': 'NAVIGATE_NODE',
                'position': navigate_pos,
                'payload': {
                    'target_node_key': next_key
                },
                'sort_order': 1 if node_key in SERVICE_NODE_KEYS else 0
            }
        )

        if node_key == 'strategy_architecture':
            hotspot_seeds.append(
                {
                    'key': 'contact_panel',
                    'title': 'Contact',
                    'description': 'Open the contact panel.',
                    'kind': 'OPEN_PANEL',
                    'position': contact_pos,
                    'payload': {
                        'panel': 'contact'
                    },
                    'sort_order': 2
                }
            )

        for hotspot_data in hotspot_seeds:
            existing = db.execute(
                select(WorldHotspot).where(
                    WorldHotspot.node_id == node.id,
                    WorldHotspot.key == hotspot_data['key']
                )
            ).scalar_one_or_none()

            if existing:
                for key, value in hotspot_data.items():
                    setattr(existing, key, value)
            else:
                db.add(WorldHotspot(node_id=node.id, **hotspot_data))
                created_hotspots += 1

    db.commit()
    return created_nodes, created_hotspots


def main() -> None:
    engine = create_db_engine()
    session_local = sessionmaker(bind=engine, class_=Session, expire_on_commit=False)
    db = session_local()
    try:
        created_nodes, created_hotspots = seed_world(db)
        print(f'Seeded world (nodes {created_nodes}, hotspots {created_hotspots})')
    finally:
        db.close()
        engine.dispose()


if __name__ == '__main__':
    main()
