import subprocess
import os

# VULNERABILIDAD: Command Injection
def execute_command(user_input):
    # ❌ CRÍTICO: Nunca hagas esto en producción
    command = f"ls {user_input}"
    subprocess.call(command, shell=True)  # Vulnerable a command injection

# VULNERABILIDAD: Hard-coded credentials
API_KEY = "sk-1234567890abcdef"  # ❌ CRÍTICO: Credenciales hard-coded

# VULNERABILIDAD: SQL Injection potential
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Vulnerable a SQL injection
    return query