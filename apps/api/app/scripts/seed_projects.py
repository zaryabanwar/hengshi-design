from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from app.db.session import create_db_engine
from app.models.project import Project, ProjectMedia
from app.projects.schemas import ProjectMediaType

PROJECT_SEEDS: list[dict] = [
    {
        'slug': 'atlas-immersive-launch',
        'title': 'Atlas Immersive Launch',
        'summary': 'A cinematic WebGL platform that elevated a luxury product launch.',
        'body': 'We built a real-time 3D experience with interactive hotspots, integrating CMS-driven content.',
        'tags': ['immersive', 'webgl'],
        'is_featured': True,
        'sort_order': 0,
        'media': [
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/atlas/hero.jpg',
                'caption': 'Launch hero scene',
                'sort_order': 0
            },
            {
                'type': ProjectMediaType.VIDEO.value,
                'url': 'https://assets.example.com/projects/atlas/teaser.mp4',
                'caption': 'Teaser reel',
                'sort_order': 1
            }
        ]
    },
    {
        'slug': 'vertex-saas-platform',
        'title': 'Vertex SaaS Platform',
        'summary': 'Scaled a multi-tenant SaaS platform for global B2B logistics.',
        'body': 'We delivered a modernized platform with resilient APIs, analytics, and onboarding automation.',
        'tags': ['saas', 'platform'],
        'is_featured': True,
        'sort_order': 1,
        'media': [
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/vertex/dashboard.png',
                'caption': 'Operations dashboard',
                'sort_order': 0
            },
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/vertex/workflows.png',
                'caption': 'Workflow automation',
                'sort_order': 1
            },
            {
                'type': ProjectMediaType.VIDEO.value,
                'url': 'https://assets.example.com/projects/vertex/demo.mp4',
                'caption': 'Platform walkthrough',
                'sort_order': 2
            }
        ]
    },
    {
        'slug': 'signal-ai-command',
        'title': 'Signal AI Command Center',
        'summary': 'Agentic intelligence hub for compliance and risk monitoring.',
        'body': 'We orchestrated multi-agent workflows for audit trails and real-time anomaly detection.',
        'tags': ['ai', 'automation'],
        'is_featured': True,
        'sort_order': 2,
        'media': [
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/signal/overview.jpg',
                'caption': 'Command overview',
                'sort_order': 0
            },
            {
                'type': ProjectMediaType.VIDEO.value,
                'url': 'https://assets.example.com/projects/signal/agents.mp4',
                'caption': 'Agent flow',
                'sort_order': 1
            }
        ]
    },
    {
        'slug': 'drift-commerce-suite',
        'title': 'Drift Commerce Suite',
        'summary': 'Headless commerce platform with performance-first storefronts.',
        'body': 'We delivered a unified commerce core with subscriptions, payments, and analytics.',
        'tags': ['commerce', 'growth'],
        'is_featured': False,
        'sort_order': 3,
        'media': [
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/drift/storefront.jpg',
                'caption': 'Storefront design',
                'sort_order': 0
            },
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/drift/checkout.jpg',
                'caption': 'Checkout flow',
                'sort_order': 1
            }
        ]
    },
    {
        'slug': 'lumen-data-foundation',
        'title': 'Lumen Data Foundation',
        'summary': 'Enterprise data lakehouse with governance and streaming analytics.',
        'body': 'We implemented data pipelines, lineage, and real-time dashboards for executive insight.',
        'tags': ['data', 'analytics'],
        'is_featured': False,
        'sort_order': 4,
        'media': [
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/lumen/pipelines.png',
                'caption': 'Pipeline orchestration',
                'sort_order': 0
            },
            {
                'type': ProjectMediaType.VIDEO.value,
                'url': 'https://assets.example.com/projects/lumen/streaming.mp4',
                'caption': 'Streaming analytics',
                'sort_order': 1
            }
        ]
    },
    {
        'slug': 'aegis-security-overhaul',
        'title': 'Aegis Security Overhaul',
        'summary': 'Security transformation for a global fintech platform.',
        'body': 'We delivered zero-trust foundations, compliance automation, and secure SDLC workflows.',
        'tags': ['security', 'cloud'],
        'is_featured': False,
        'sort_order': 5,
        'media': [
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/aegis/zero-trust.jpg',
                'caption': 'Zero-trust layers',
                'sort_order': 0
            },
            {
                'type': ProjectMediaType.IMAGE.value,
                'url': 'https://assets.example.com/projects/aegis/audit.jpg',
                'caption': 'Audit readiness',
                'sort_order': 1
            },
            {
                'type': ProjectMediaType.VIDEO.value,
                'url': 'https://assets.example.com/projects/aegis/incident.mp4',
                'caption': 'Incident response',
                'sort_order': 2
            }
        ]
    }
]


def seed_projects(db: Session) -> int:
    created = 0

    for seed in PROJECT_SEEDS:
        entry = {**seed}
        media_items = entry.pop('media', [])
        project = db.execute(
            select(Project).where(Project.slug == entry['slug'])
        ).scalar_one_or_none()

        if project:
            for key, value in entry.items():
                setattr(project, key, value)
        else:
            project = Project(**entry)
            db.add(project)
            db.flush()
            created += 1

        for media in media_items:
            existing_media = db.execute(
                select(ProjectMedia).where(
                    ProjectMedia.project_id == project.id,
                    ProjectMedia.url == media['url']
                )
            ).scalar_one_or_none()

            if existing_media:
                for key, value in media.items():
                    setattr(existing_media, key, value)
            else:
                db.add(ProjectMedia(project_id=project.id, **media))

    db.commit()
    return created


def main() -> None:
    engine = create_db_engine()
    session_local = sessionmaker(bind=engine, class_=Session, expire_on_commit=False)
    db = session_local()
    try:
        created = seed_projects(db)
        print(f'Seeded projects (created {created})')
    finally:
        db.close()
        engine.dispose()


if __name__ == '__main__':
    main()
