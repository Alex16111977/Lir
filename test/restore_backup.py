"""
Скрипт відновлення з backup
Створено для безпечного рефакторингу
"""
import shutil
from pathlib import Path
from datetime import datetime

def restore_from_backup():
    """Відновити проект з останнього backup."""
    backup_dir = Path(r'F:\AiKlientBank\Lir_backup')
    
    if not backup_dir.exists():
        print("[ERROR] Директорія backup не існує")
        return False
        
    # Знайти останній backup
    backups = sorted([d for d in backup_dir.iterdir() if d.is_dir() and d.name.startswith('backup_')])
    
    if not backups:
        print("[ERROR] Немає доступних backup")
        return False
        
    latest_backup = backups[-1]
    print(f"[RESTORE] Відновлення з {latest_backup.name}")
    
    # Відновлення src/
    backup_src = latest_backup / 'src'
    target_src = Path(r'F:\AiKlientBank\Lir\src')
    
    if backup_src.exists():
        shutil.rmtree(target_src, ignore_errors=True)
        shutil.copytree(backup_src, target_src)
        print("[OK] Директорія src/ відновлена")
        
        # Тест запуску
        import subprocess
        import sys
        result = subprocess.run(
            [sys.executable, r'F:\AiKlientBank\Lir\main.py'],
            capture_output=True,
            text=True,
            cwd=r'F:\AiKlientBank\Lir'
        )
        
        if result.returncode == 0:
            print("[OK] Проект працює після відновлення")
            return True
        else:
            print(f"[ERROR] Проект не працює: {result.stderr[:200]}")
            return False
    else:
        print("[ERROR] Backup не містить src/")
        return False

if __name__ == "__main__":
    restore_from_backup()
