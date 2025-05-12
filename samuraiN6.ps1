$DB_NAME = "Samurai"
$DB_USER = "postgres"
$BACKUP_DIR ="C:\Users\juego\OneDrive\Desktop\SQL\Nivel 6\Reto 2\Copias"
$TIMESTAMP = Get-Date -Format "yyyyMMdd_HHmmss"
$BACKUP_FILE ="$BACKUP_DIR\$DB_NAME_$TIMESTAMP.sql"

pg_dump -U $DB_USER -F c -f $BACKUP_FILE $DB_NAME

Write-Output "Backup de $DB_NAME realizado correctamente."