#!/usr/bin/env bash

# set database name
DATABASE_NAME="farmer_market"

# set path to backup directory
BACKUP_DIR="./backend/database/mongo-backup"

# dump to create backup
mongodump --db="$DATABASE_NAME" --out="$BACKUP_DIR"
