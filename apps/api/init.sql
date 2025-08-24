-- Create extensions we might need
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Set timezone
SET timezone = 'UTC';

-- Create basic table structure will be handled by Alembic migrations
-- This file is for any one-time database setup
