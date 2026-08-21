module.exports = {
  ci: {
    collect: {
      staticDistDir: './apps/web/dist',
      isSinglePageApplication: true,
      url: ['http://localhost/'],
      numberOfRuns: 1,
      settings: {
        chromeFlags: '--headless=new --no-sandbox'
      }
    },
    assert: {
      assertions: {
        'categories:performance': ['warn', { minScore: 0.5 }],
        'categories:accessibility': ['warn', { minScore: 0.8 }],
        'categories:best-practices': ['warn', { minScore: 0.8 }],
        'categories:seo': ['warn', { minScore: 0.8 }]
      }
    },
    upload: {
      target: 'filesystem',
      outputDir: './.lighthouseci'
    }
  }
}
