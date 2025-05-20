# Database Migration and Management

This project demonstrates how to migrate a legacy application's database from MySQL to MongoDB and implement a hybrid architecture to manage both existing (relational) and new (document-based) data.

## Repository Contents

| File/Folder               | Description                                      |
|---------------------------|--------------------------------------------------|
| app.py                    | Main backend server (likely using Flask)         |
| mysql_db.py               | MySQL connection script                          |
| mongo_db.py               | MongoDB connection script                        |
| migrate_mysql_to_mongo.py| Python script to perform data migration          |
| docs/                     | Project documentation                            |
| README.md                 | Project overview and instructions                |

## Project Phases

- Phase 1: Research – Completed
- Phase 2: Design – Completed
- Phase 3: Development – In Progress
- Phase 4: Testing – Pending
- Phase 5: Deployment – Pending

## Technologies Used

- MySQL – Legacy relational database
- MongoDB – NoSQL database for new modules
- Python – For data migration and backend
- Flask – Backend API (assumed based on `app.py`)
- Pandas – For data manipulation during migration

## Folder Structure
/database-migration-project
├── scripts/
│ └── migrate_mysql_to_mongo.py
├── backend/
│ ├── app.py
│ ├── mysql_db.py
│ └── mongo_db.py
├── docs/
├── README.md


## Migration Script

The script `migrate_mysql_to_mongo.py` does the following:
- Connects to the MySQL database using `pymysql`
- Reads data from `Users`, `Orders`, and `Payments` tables
- Converts the data using `pandas` into a MongoDB-compatible format
- Inserts the data into MongoDB using `pymongo`

### To Run the Script:

```bash
cd scripts
python migrate_mysql_to_mongo.py

