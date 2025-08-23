# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flow7 is an AI agent workspace platform that creates autonomous "digital employees" working 24/7 across existing tools. The platform uses natural language to create intelligent agents that orchestrate tasks across Slack, GitHub, Gmail, calendars, and other productivity tools.

**Current Status**: Early development phase with a minimal homepage deployed. The core platform (FastAPI backend, agent execution engine, MCP integrations) is not yet implemented.

**Note**: The root package.json shows project name as "conductor" which may be the internal codename, while "Flow7" is the public brand name.

## Architecture

This is a **Turborepo monorepo** with the following structure:

### Frontend Applications
- **`apps/web`**: Main Next.js 15 application with TypeScript
  - Contains minimal homepage with mysterious messaging
  - Uses system fonts and minimal CSS modules for styling
  - Deployed to Cloudflare Pages at flow7.ai
- **`apps/docs`**: Documentation site (Next.js 15 with TypeScript)
  - Standard Turborepo docs template structure

### Backend (Planned)
- **FastAPI** with Python for API layer
- **PostgreSQL** with JSONB for flexible agent configurations  
- **Redis + Celery** for background agent execution (24/7 processing)
- **Model Context Protocol (MCP)** for external API integrations

### Shared Packages
- **`packages/ui`**: Shared React components (button, card, code)
- **`packages/eslint-config`**: ESLint configurations (base, next, react-internal)
- **`packages/typescript-config`**: TypeScript configurations (base, nextjs, react-library)

## Core Development Commands

```bash
# Development
pnpm dev              # Start all apps in development mode
pnpm dev --filter=web # Start only the web app

# Building
pnpm build            # Build all apps and packages
pnpm build --filter=web # Build only the web app

# Code Quality
pnpm lint             # Lint all packages
pnpm format           # Format code with Prettier
pnpm check-types      # TypeScript type checking across all packages
```

## Key Technical Decisions

### Package Manager
- Uses **pnpm 9.15.0** (recently updated from 9.0.0 for deployment compatibility)
- Workspace configuration in `pnpm-workspace.yaml`

### Deployment
- **Web app**: Cloudflare Pages with custom build command: `pnpm install --no-frozen-lockfile && cd apps/web && pnpm build`
- **Domain**: flow7.ai (registered)
- **Build output**: `apps/web/.next`

### Brand Strategy
- **Minimal, mysterious homepage** - only describes problems, not solutions
- No social links, company descriptions, or feature explanations
- Inspired by tinygrad and Thinking Machines Lab design aesthetics
- Light theme only, faded typography, problem-focused messaging

## Planned Integration Architecture

The platform will integrate with external services via the **Model Context Protocol (MCP)**:

```
Next.js Frontend → FastAPI Backend → MCP Client → MCP Servers
                                   ↓
                             Agent Orchestrator  
                                   ↓
                             Background Workers (Celery)
                                   ↓
                             PostgreSQL Database
```

### Priority Integrations (MVP)
1. **Slack** - Message monitoring, posting, channel management
2. **GitHub** - PR management, issue tracking, code review automation  
3. **Gmail/Google Calendar** - Email processing, meeting scheduling
4. **Jira/Linear** - Ticket creation, status updates

## Agent Configuration Example

Agents are configured with natural language triggers and actions:

```python
agent_config = {
    "name": "Bug Triage Assistant",
    "trigger": {
        "platform": "slack",
        "channels": ["#support", "#bug-reports"], 
        "conditions": ["contains_keyword('bug')", "reaction_count('😡') >= 2"]
    },
    "actions": [
        {"platform": "jira", "action": "create_issue", "priority": "high"},
        {"platform": "slack", "action": "post_message", "template": "🎫 Ticket created: {ticket_url}"}
    ],
    "schedule": "continuous"
}
```

## Environment Setup

Required environment variables for full platform (not yet implemented):

```bash
# Database
DATABASE_URL=postgresql://localhost:5432/flow7
REDIS_URL=redis://localhost:6379

# AI Services  
OPENAI_API_KEY=your_openai_key

# Platform Integrations
SLACK_CLIENT_ID=your_slack_client_id
SLACK_CLIENT_SECRET=your_slack_client_secret  
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
```

## Business Context

- **Target Market**: SMB teams (10-100 people), developer teams, productivity-focused professionals
- **Revenue Model**: Freemium (1 agent free, $20/month Pro, $50/month Team, Enterprise custom)
- **Value Proposition**: Eliminate the 40% of time spent on repetitive tasks and 11+ daily app switches

The platform aims to "commoditize the digital worker" by making AI agent automation accessible through natural language rather than complex technical configuration.