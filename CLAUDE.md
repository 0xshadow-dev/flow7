# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Flow7 is an AI agent workspace platform that creates autonomous "digital employees" working 24/7 across existing tools. The platform uses natural language to create intelligent agents that orchestrate tasks across Slack, GitHub, Gmail, calendars, and other productivity tools.

**MVP Vision**: Multi-agent automation platform with 100+ app integrations where specialized AI agents collaborate on complex cross-platform workflows through natural language commands.

**Ultimate Vision**: OS-level digital assistant layer that replaces individual app interfaces. Users interact with a single natural language interface to control their entire digital workspace - from scheduling meetings to designing in Figma to managing finances - without ever opening individual apps.

**Current Status**: Early development phase with a minimal homepage deployed and FastAPI backend foundation implemented. The agent execution engine and MCP integrations are planned for next development phase.

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

### Backend (Implemented)
- **`apps/api`**: FastAPI backend with Python
  - ✅ FastAPI application with health endpoints
  - ✅ PostgreSQL database with Docker setup
  - ✅ SQLAlchemy ORM with session management  
  - ✅ Pydantic settings and configuration
  - ✅ Database connection and health monitoring
  - ⏳ Agent models and CRUD operations (in progress)
  - 🔜 Redis + Celery for background agent execution
  - 🔜 Model Context Protocol (MCP) integrations

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

## Backend Development Commands

```bash
# FastAPI Backend (from apps/api/)
pipenv install                    # Install Python dependencies
pipenv run uvicorn app.main:app --reload --port 8000  # Start API server

# Database (Docker PostgreSQL)
docker-compose up -d postgres     # Start PostgreSQL container
docker-compose logs postgres      # View database logs
docker-compose exec postgres psql -U flow7_user -d flow7  # Connect to database

# API Testing
curl http://localhost:8000/api/v1/health     # Test API health
curl http://localhost:8000/api/v1/health/db  # Test database connection
open http://localhost:8000/api/docs          # Interactive API documentation
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

### Priority Integrations (MVP - 20+ Apps)
1. **Communication**: Slack, WhatsApp, Telegram, Discord, Teams
2. **Development**: GitHub, GitLab, Jira, Linear, Figma
3. **Productivity**: Gmail, Google Calendar, Notion, Google Drive, Trello
4. **Business**: Salesforce, HubSpot, Stripe, QuickBooks, Airtable

### Ultimate Integration Vision (100+ Apps)
- **All Major Categories**: Communication, Creative Tools, Finance, E-commerce, Analytics, Social Media, Infrastructure, CRM, Knowledge Management
- **Universal Connectivity**: Any app with an API can be integrated through MCP protocol
- **OS-Level Integration**: Direct integration with desktop applications and system APIs

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

### Current Backend Setup (Working)
```bash
# Database (Docker PostgreSQL - automatically configured)
DATABASE_URL=postgresql://flow7_user:flow7_password@localhost:5432/flow7

# API Configuration
DEBUG=true
ENVIRONMENT=development
```

### Future Environment Variables (Planned)
```bash
# Redis (for background workers)
REDIS_URL=redis://localhost:6379

# AI Services  
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# Communication Platforms
SLACK_CLIENT_ID=your_slack_client_id
SLACK_CLIENT_SECRET=your_slack_client_secret
WHATSAPP_API_KEY=your_whatsapp_key
DISCORD_BOT_TOKEN=your_discord_token

# Development Platforms
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
FIGMA_ACCESS_TOKEN=your_figma_token

# Productivity Platforms  
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
NOTION_INTEGRATION_TOKEN=your_notion_token

# Business Platforms
SALESFORCE_CLIENT_ID=your_salesforce_id
STRIPE_SECRET_KEY=your_stripe_key
QUICKBOOKS_CLIENT_ID=your_quickbooks_id
```

## Business Context

- **Target Market**: SMB teams (10-100 people), developer teams, productivity-focused professionals, ultimately expanding to all computer users
- **Revenue Model**: Freemium (1 agent free, $20/month Pro, $50/month Team, Enterprise custom)
- **Value Proposition**: 
  - **MVP**: Eliminate the 40% of time spent on repetitive tasks and 11+ daily app switches
  - **Ultimate**: Replace the need to learn new app interfaces by providing universal natural language control

The platform aims to "commoditize the digital worker" by making AI agent automation accessible through natural language rather than complex technical configuration. The ultimate vision is to become the primary interface between humans and their digital tools.

## Development Progress

### Current Implementation Status
- ✅ **FastAPI Backend Foundation**: Health endpoints, PostgreSQL setup, SQLAlchemy ORM
- ✅ **Next.js Frontend**: Minimal homepage deployed to flow7.ai
- ✅ **Database Infrastructure**: Docker PostgreSQL with session management
- ⏳ **Agent Models**: Database schema design in progress
- 🔜 **MCP Client Architecture**: Model Context Protocol integration framework
- 🔜 **Multi-Agent Orchestration**: Agent coordination and collaboration system
- 🔜 **OAuth Integration**: Secure authentication for 100+ platforms