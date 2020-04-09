# ---------------------------
# Python frameworks to import
# ---------------------------
from flask import Flask
from flask import render_template
from flask import request # to get input from HTML form
import psycopg2 # for database connection and SQL execution

# ---------------------
# Connect to PostgreSQL
# ---------------------
t_host = "127.0.0.1"
t_port = "5432" #5432 is typically default port
t_dbname = "rmtopo"
t_name_user = "rakuten"
t_password = "rakuten123"
data_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_name_user, password=t_password)
data_cursor = data_conn.cursor()

@app.route("/Upload_File", methods=["GET", "POST"])

# ----------------------------------------
# Function for retrieving form data (file)
# ----------------------------------------
def Upload_File():
    if request.method == "POST":
        if request.files:
            blob_saved_file = request.files["file_name"]
            # IMPORTANT: Be sure to have an item ID.
            id_item = 52
            # Call function for saving to Postgres, with two parameters
            Save_File_To_Database(id_item, blob_saved_file)

    return render_template("save-file.html")

# ------------------------------------------
# Function for saving the file to PostgreSQL
# ------------------------------------------
def Save_File_To_Database(id_item, blob_saved_file):
    s = ""
    s += "INSERT INTO tbl_saved_files"
    s += "("
    s += "id_item"
    s += ", blob_saved_file"
    s += ") VALUES ("
    s += "(%id_item)"
    s += ", '(%blob_saved_file)'"
    s += ")"
    # We recommend adding TRY here to trap errors.
    data_cursor.execute(s, [id_item, blob_saved_file])
    # Use commit here if you do not have auto-commits turned on.