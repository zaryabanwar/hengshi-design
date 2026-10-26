// HSD-002 Figma layouts and capability copy accepted by the founder 2026-10-26.
// Capability descriptions are not delivery evidence; all proof collections remain empty.
export const wings = [
  {
    "title": "Strategy & Transformation",
    "path": "/services/strategy-transformation",
    "description": "Work through your goals, priorities and technical choices before you commit to a plan.",
    "tags": "Planning / Architecture / Roadmaps"
  },
  {
    "title": "Digital Products & Growth",
    "path": "/services/digital-products-growth",
    "description": "Design and build websites, platforms and digital products around the people who use them.",
    "tags": "Websites / Platforms / Product design"
  },
  {
    "title": "AI, Data & Automation",
    "path": "/services/ai-data-automation",
    "description": "Find practical ways to use AI, automate repetitive work and make better use of your data.",
    "tags": "AI tools / Automation / Data"
  },
  {
    "title": "Immersive & Creative",
    "path": "/services/immersive-creative",
    "description": "Explain ideas through visual design, interactive experiences and 3D.",
    "tags": "Visual design / Interactive / 3D"
  },
  {
    "title": "Cloud, Reliability & Trust",
    "path": "/services/cloud-reliability-trust",
    "description": "Build and maintain the infrastructure, security and reliability your systems need.",
    "tags": "Cloud / Reliability / Security"
  }
] as const

export const formalServices = [
  {
    "title": "Strategy & Architecture",
    "path": "/services/strategy-transformation/strategy-architecture",
    "wingPath": "/services/strategy-transformation",
    "description": "Clarify priorities, compare technical options and shape a practical direction for your project.",
    "decision": "Which approach fits your goals and constraints?",
    "focus": [
      "Goals, constraints and priorities",
      "Architecture options and trade-offs",
      "A roadmap for the work"
    ],
    "boundary": "Recommendations depend on the information available. Scope, responsibilities and deliverables are agreed before work begins."
  },
  {
    "title": "Platform & Product Engineering",
    "path": "/services/digital-products-growth/platform-product-engineering",
    "wingPath": "/services/digital-products-growth",
    "description": "Plan and develop the software, integrations and foundations behind a digital product.",
    "decision": "What does your product need to work reliably?",
    "focus": [
      "Product requirements and technical design",
      "Application and integration development",
      "Testing and maintainability"
    ],
    "boundary": "A project scope defines the supported systems, integrations and ongoing responsibilities."
  },
  {
    "title": "Product Design & Experience Engineering",
    "path": "/services/digital-products-growth/product-design-experience-engineering",
    "wingPath": "/services/digital-products-growth",
    "description": "Understand user journeys and turn them into clear, usable interfaces and interaction patterns.",
    "decision": "How should the product work for the people using it?",
    "focus": [
      "User journeys and information architecture",
      "Interface design and design systems",
      "Prototypes and usability evaluation"
    ],
    "boundary": "Research access, supported devices and accessibility criteria are agreed for each project. Designs alone do not establish accessibility compliance."
  },
  {
    "title": "Commerce, Content & Growth Platforms",
    "path": "/services/digital-products-growth/commerce-content-growth-platforms",
    "wingPath": "/services/digital-products-growth",
    "description": "Connect commerce and content journeys with the systems used to manage and improve them.",
    "decision": "How can content and commerce support your goals?",
    "focus": [
      "Commerce and content journeys",
      "Content platforms and integrations",
      "Measurement requirements"
    ],
    "boundary": "Sales, traffic and growth outcomes are not guaranteed. Platform costs and third-party services are scoped separately."
  },
  {
    "title": "AI Systems & Agentic Automation",
    "path": "/services/ai-data-automation/ai-systems-agentic-automation",
    "wingPath": "/services/ai-data-automation",
    "description": "Explore AI-assisted workflows and automation with clear information, evaluation and human-control boundaries.",
    "decision": "Where could AI help, and where is human control needed?",
    "focus": [
      "Workflow and suitability assessment",
      "Source and data boundaries",
      "Evaluation and human oversight"
    ],
    "boundary": "AI can produce incorrect output. Data access, source policy, evaluation and human approval need explicit agreement; no autonomous commitments are implied."
  },
  {
    "title": "Data Platforms & Analytics",
    "path": "/services/ai-data-automation/data-platforms-analytics",
    "wingPath": "/services/ai-data-automation",
    "description": "Organise data flows and analytical views around the decisions your team needs to make.",
    "decision": "What data would help your team make a decision?",
    "focus": [
      "Data sources and quality requirements",
      "Pipelines and analytical models",
      "Reporting and decision support"
    ],
    "boundary": "Useful analysis depends on source quality, access rights and agreed definitions. Data accuracy is not assumed."
  },
  {
    "title": "Spatial Computing & Immersive Platforms",
    "path": "/services/immersive-creative/spatial-computing-immersive-platforms",
    "wingPath": "/services/immersive-creative",
    "description": "Explore interactive 3D and spatial experiences with an equivalent accessible path to essential content.",
    "decision": "When would a spatial experience make an idea clearer?",
    "focus": [
      "Spatial journeys and interaction concepts",
      "Interactive 3D experiences",
      "Performance and accessible alternatives"
    ],
    "boundary": "Device support, asset rights and performance targets need project-specific validation. Essential content must remain accessible without 3D."
  },
  {
    "title": "Creative & Visual Design Services",
    "path": "/services/immersive-creative/creative-visual-design-services",
    "wingPath": "/services/immersive-creative",
    "description": "Develop visual ideas and design assets that explain your message and support a coherent identity.",
    "decision": "What should your audience understand or recognise?",
    "focus": [
      "Visual direction and communication",
      "Digital design assets",
      "Design guidelines and handover"
    ],
    "boundary": "Asset formats, usage rights and the deliverable set are agreed in scope. No unlicensed imagery or third-party rights are implied."
  },
  {
    "title": "Cloud, DevOps & Platform Reliability",
    "path": "/services/cloud-reliability-trust/cloud-devops-platform-reliability",
    "wingPath": "/services/cloud-reliability-trust",
    "description": "Plan infrastructure, delivery workflows and operational practices around your system’s requirements.",
    "decision": "What does your system need to run and recover?",
    "focus": [
      "Infrastructure and deployment planning",
      "Delivery workflows and observability",
      "Reliability and recovery requirements"
    ],
    "boundary": "Provider choice follows project needs. Costs, service levels and operational cover require separate agreement; no uptime guarantee is implied."
  },
  {
    "title": "Security, Privacy & Trust Engineering",
    "path": "/services/cloud-reliability-trust/security-privacy-trust-engineering",
    "wingPath": "/services/cloud-reliability-trust",
    "description": "Identify security and privacy requirements and plan how controls will be implemented and evaluated.",
    "decision": "Which risks and data responsibilities need attention?",
    "focus": [
      "Risk and data-flow assessment",
      "Security and privacy requirements",
      "Control implementation and verification"
    ],
    "boundary": "This describes an engineering capability, not certification, legal advice or a compliance guarantee. Qualified review and evidence are required for assurance claims."
  }
] as const

export type Wing = typeof wings[number]
export type FormalService = typeof formalServices[number]
