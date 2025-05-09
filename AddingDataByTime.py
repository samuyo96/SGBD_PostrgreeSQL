import psycopg2
import random
import time
from datetime import datetime, timedelta

conn = psycopg2.connect(
    dbname="Samurai",
    user="postgres",
    password="4719",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

#array con las páginas simuladas

paginas = ["/home", "/about", "/contact", "/products", "/cart"]

for i in range(100): #insertar 100 registros
    #acces_time = datetime.now().strftime('%H:%M:%S')
    base_time = datetime.strptime("00:00:00", "%H:%M:%S")
    random_hours = random.randint(0,23)
    random_minutes = random.randint(0,59)
    random_seconds = random.randint(0,59)
    acces_time = (base_time + timedelta(hours=random_hours, minutes=random_minutes, seconds=random_seconds))
    user_ip = f"192.168.1.{random.randint(1,255)}"
    visited_page = random.choice(paginas)
    visit_time = f"{random.randint(1,60)} minutes"

    query = """
    INSERT INTO pagina(accesTime, userip, visitedPage, visitTime)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (acces_time, user_ip, visited_page, visit_time))
    conn.commit()
    wait_time = random.uniform(0.5, 3)
    print(f"Registro {i+1} insertado")
    time.sleep(wait_time)

#Cerrar
cursor.close()
conn.close()
print("Finalizado")
