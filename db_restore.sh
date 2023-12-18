#!/usr/bin/env bash

# set database name
DATABASE_NAME="farmer_market"

# set path to backup directory
BACKUP_DIR="./backend/database/mongo-backup"

# restore the database from the dump
mongorestore --db="$DATABASE_NAME" "$BACKUP_DIR"
