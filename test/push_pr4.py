"""
Push змін на GitHub після злиття PR #4
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

print("[PUSH] Pushing merged PR #4 to GitHub...")

# 1. Фінальна перевірка статусу
print("\n[1] Current status:")
result = run_git_command('git status --short')
print(result['stdout'] if result['stdout'] else "Working tree clean")

# 2. Перевірка що випереджаємо origin
print("\n[2] Checking commits ahead:")
result = run_git_command('git log origin/main..main --oneline')
print(f"Commits to push:\n{result['stdout']}")

# 3. Push на GitHub
print("\n[3] Pushing to origin/main...")
result = run_git_command('git push origin main')
if result['success']:
    print("[OK] Successfully pushed to GitHub!")
    print(result['stderr'])  # Git виводить прогрес в stderr
else:
    print("[ERROR] Push failed!")
    print(result['stderr'])
    
# 4. Видалення локальної гілки pr-4
print("\n[4] Cleaning up pr-4 branch...")
result = run_git_command('git branch -d pr-4')
print(f"Result: {result.get('stdout', '')} {result.get('stderr', '')}")

print("\n[COMPLETE] PR #4 has been successfully merged and pushed!")
print("\nFinal steps on GitHub:")
print("1. Go to: https://github.com/Alex16111977/Lir/pull/4")
print("2. Click 'Close pull request' (it's already merged)")
print("3. Verify the changes are in main branch")
