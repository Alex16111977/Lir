"""
Злиття Pull Request #4 в main
"""
import subprocess
import os
import sys

os.chdir(r'F:\AiKlientBank\Lir')

def run_git_command(command):
    """Виконання git команди"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='cp1251')
        return {
            'success': result.returncode == 0,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'code': result.returncode
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

print("[INFO] Starting PR #4 merge process...")

# 1. Переконаємося що на main
print("\n[1] Switching to main branch...")
result = run_git_command('git checkout main')
print(f"Result: {result.get('stderr', '')} {result.get('stdout', '')}")

# 2. Pull останні зміни з origin/main
print("\n[2] Pulling latest from origin/main...")
result = run_git_command('git pull origin main')
print(f"Result: {result.get('stderr', '')} {result.get('stdout', '')}")

# 3. Злиття pr-4 в main
print("\n[3] Merging pr-4 into main...")
result = run_git_command('git merge pr-4 --no-ff -m "Merge PR #4: Expand sentence builder to cover all lesson vocabulary"')
if result['success']:
    print("[OK] Successfully merged PR #4!")
    print(result['stdout'])
else:
    print("[ERROR] Merge failed!")
    print(result['stderr'])

# 4. Показати результат
print("\n[4] Current status:")
result = run_git_command('git status')
print(result['stdout'])

# 5. Показати останній коміт
print("\n[5] Last commit:")
result = run_git_command('git log --oneline -1')
print(result['stdout'])

print("\n[DONE] PR #4 merge completed!")
print("\nNext steps:")
print("1. Test the changes: python main.py")
print("2. Push to GitHub: git push origin main")
print("3. Close PR #4 on GitHub")
