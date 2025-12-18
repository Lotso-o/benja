import oracledb
import os
import dontenv import load_dontenv
import bcrypt

load_dontenv()

usename = os.getenv("ORACLE_USER")
dns