from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from app.db.session import create_db_engine
from app.models.service import Service
from app.services.schemas import ServiceCategory

SERVICE_SEEDS: list[dict] = [
    {
        'slug': 'digital-transformation-strategy',
        'title': 'Digital Transformation Strategy',
        'category': ServiceCategory.STRATEGY_ARCHITECTURE.value,
        'summary': 'Roadmaps and decision support for modern platform shifts.',
        'body': 'We define transformation paths, align stakeholders, and design phased modernization programs.',
        'deliverables': [
            'Strategy roadmap',
            'Capability gap assessment',
            'Architecture direction'
        ],
        'tags': ['strategy', 'architecture'],
        'is_featured': True,
        'sort_order': 0
    },
    {
        'slug': 'platform-product-engineering',
        'title': 'Platform and Product Engineering',
        'category': ServiceCategory.PLATFORM_ENGINEERING.value,
        'summary': 'Build and scale web, mobile, and SaaS platforms with modern stacks.',
        'body': 'We ship production-grade applications with reliable APIs, clean architecture, and performance focus.',
        'deliverables': [
            'Architecture blueprint',
            'Delivery plan',
            'Production launch support'
        ],
        'tags': ['engineering', 'platform'],
        'is_featured': True,
        'sort_order': 1
    },
    {
        'slug': 'ai-systems-automation',
        'title': 'AI Systems and Agentic Automation',
        'category': ServiceCategory.AI_SYSTEMS.value,
        'summary': 'Deploy AI applications, agents, and automation with rigorous governance.',
        'body': 'We build AI workflows, evaluate quality, and deploy secure systems that integrate into your ops.',
        'deliverables': [
            'AI workflow design',
            'Model evaluation plan',
            'Deployment playbook'
        ],
        'tags': ['ai', 'automation'],
        'is_featured': True,
        'sort_order': 2
    },
    {
        'slug': 'immersive-spatial-platforms',
        'title': 'Spatial Computing and Immersive Platforms',
        'category': ServiceCategory.SPATIAL_IMMERSIVE.value,
        'summary': 'Create WebGL, AR, and immersive 3D experiences for brands and products.',
        'body': 'We design and build virtual spaces, optimized real-time 3D pipelines, and interactive tours.',
        'deliverables': [
            'Spatial UX map',
            'Interactive prototype',
            'Performance optimization plan'
        ],
        'tags': ['3d', 'immersive'],
        'is_featured': True,
        'sort_order': 3
    },
    {
        'slug': 'product-design-experience',
        'title': 'Product Design and Experience Engineering',
        'category': ServiceCategory.PRODUCT_DESIGN.value,
        'summary': 'Design systems, UX strategy, and premium product experiences.',
        'body': 'We align product vision with user journeys and deliver scalable design systems.',
        'deliverables': [
            'UX strategy',
            'Design system foundations',
            'Prototype library'
        ],
        'tags': ['design', 'ux'],
        'is_featured': True,
        'sort_order': 4
    },
    {
        'slug': 'cloud-devops-reliability',
        'title': 'Cloud, DevOps, and Platform Reliability',
        'category': ServiceCategory.CLOUD_DEVOPS.value,
        'summary': 'Modernize infrastructure, automate releases, and strengthen reliability.',
        'body': 'We deliver cloud migration plans, CI/CD automation, and observable, resilient platforms.',
        'deliverables': [
            'Cloud migration roadmap',
            'CI/CD pipeline',
            'Reliability metrics'
        ],
        'tags': ['cloud', 'devops'],
        'is_featured': True,
        'sort_order': 5
    },
    {
        'slug': 'security-privacy-trust',
        'title': 'Security, Privacy, and Trust Engineering',
        'category': ServiceCategory.SECURITY_TRUST.value,
        'summary': 'Harden platforms with threat modeling, secure SDLC, and privacy controls.',
        'body': 'We assess risks, build secure practices, and prepare compliance-ready engineering stacks.',
        'deliverables': [
            'Threat model',
            'Secure SDLC plan',
            'Compliance mapping'
        ],
        'tags': ['security', 'privacy'],
        'is_featured': True,
        'sort_order': 6
    },
    {
        'slug': 'data-platforms-analytics',
        'title': 'Data Platforms and Analytics',
        'category': ServiceCategory.DATA_PLATFORMS.value,
        'summary': 'Design and implement data pipelines, warehouses, and real-time analytics.',
        'body': 'We build data foundations with governance, quality controls, and analytics visibility.',
        'deliverables': [
            'Data architecture',
            'Pipeline implementation',
            'Analytics dashboards'
        ],
        'tags': ['data', 'analytics'],
        'is_featured': True,
        'sort_order': 7
    },
    {
        'slug': 'commerce-content-growth',
        'title': 'Commerce, Content, and Growth Platforms',
        'category': ServiceCategory.COMMERCE_GROWTH.value,
        'summary': 'Build commerce systems, CMS foundations, and growth analytics pipelines.',
        'body': 'We launch commerce experiences with SEO-ready infrastructure and integrated growth tooling.',
        'deliverables': [
            'Commerce architecture',
            'CMS workflow design',
            'Growth measurement plan'
        ],
        'tags': ['commerce', 'growth'],
        'is_featured': True,
        'sort_order': 8
    }
]


def seed_services(db: Session) -> int:
    created = 0
    for entry in SERVICE_SEEDS:
        existing = db.execute(
            select(Service).where(Service.slug == entry['slug'])
        ).scalar_one_or_none()

        if existing:
            for key, value in entry.items():
                setattr(existing, key, value)
        else:
            db.add(Service(**entry))
            created += 1

    db.commit()
    return created


def main() -> None:
    engine = create_db_engine()
    session_local = sessionmaker(bind=engine, class_=Session, expire_on_commit=False)
    db = session_local()
    try:
        created = seed_services(db)
        print(f'Seeded services (created {created})')
    finally:
        db.close()
        engine.dispose()


if __name__ == '__main__':
    main()
