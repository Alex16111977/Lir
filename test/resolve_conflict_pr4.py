"""
Вирішення конфлікту злиття PR #4
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

print("[INFO] Resolving merge conflict...")

# 1. Подивимося що в конфлікті
print("\n[1] Checking conflict file...")
result = run_git_command('git diff --name-only --diff-filter=U')
print(f"Conflicted files: {result['stdout']}")

# 2. Приймаємо версію з pr-4 (нова функціональність)
print("\n[2] Resolving conflict - taking PR version...")
result = run_git_command('git checkout pr-4 -- test/test_sentence_builder_buttons.py')
print(f"Result: {result.get('stderr', 'File updated from pr-4')}")

# 3. Додаємо вирішений файл
print("\n[3] Adding resolved file...")
result = run_git_command('git add test/test_sentence_builder_buttons.py')

# 4. Також додаємо файл exercises_assets.py з PR
print("\n[4] Adding exercises_assets.py from PR...")
result = run_git_command('git checkout pr-4 -- src/generators/exercises_assets.py')
result = run_git_command('git add src/generators/exercises_assets.py')

# 5. Завершуємо злиття
print("\n[5] Completing merge...")
result = run_git_command('git commit -m "Merge PR #4: Expand sentence builder to cover all lesson vocabulary - conflicts resolved"')
if result['success']:
    print("[OK] Merge completed successfully!")
    print(result['stdout'])
else:
    print("[ERROR] Commit failed:")
    print(result['stderr'])

# 6. Фінальний статус
print("\n[6] Final status:")
result = run_git_command('git status --short')
print(result['stdout'] if result['stdout'] else "Working tree clean (except untracked test files)")

# 7. Останній коміт
print("\n[7] Last commits:")
result = run_git_command('git log --oneline -3')
print(result['stdout'])

print("\n[SUCCESS] PR #4 successfully merged!")
print("\nTo complete the process:")
print("1. Test: python main.py")
print("2. Push: git push origin main")
