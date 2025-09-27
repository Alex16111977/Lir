"""
Emergency Restore Script
Використовуй для швидкого відновлення після невдалого рефакторингу
"""
import shutil
from pathlib import Path

def restore_from_backup():
    """Відновити файли з backup."""
    backups = [
        ('exercises_assets.py.backup', 'exercises_assets.py'),
        ('json_generator.py.backup', 'json_generator.py'),
        ('book_generator.py.backup', 'book_generator.py'),
        ('exercises_generator.py.backup', 'exercises_generator.py'),
        ('original_styles.py.backup', 'original_styles.py')
    ]
    
    base_dir = Path(r'F:\AiKlientBank\Lir\src\generators')
    restored = 0
    
    for backup_name, original_name in backups:
        backup_path = base_dir / backup_name
        original_path = base_dir / original_name
        
        if backup_path.exists():
            shutil.copy2(backup_path, original_path)
            print(f"[OK] Restored: {original_name}")
            restored += 1
    
    # Видалити модульні директорії якщо є
    module_dirs = ['exercises_assets_modules', 'json_generator_modules', 
                   'book_generator_modules', 'exercises_generator_modules']
    
    for module_dir in module_dirs:
        module_path = base_dir / module_dir
        if module_path.exists():
            shutil.rmtree(module_path, ignore_errors=True)
            print(f"[REMOVED] {module_dir}")
    
    print(f"\n[COMPLETE] Restored {restored} files")
    return restored

if __name__ == "__main__":
    restore_from_backup()
