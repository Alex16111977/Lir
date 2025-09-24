"""
Скрипт для перевірки Pull Request #4
"""
import subprocess
import os
import sys

os.chdir(r'F:\AiKlientBank\Lir')

def run_git_command(command):
    """Виконання git команди з виводом"""
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

# 1. Оновлення з remote
print("[STEP 1] Fetching from origin...")
result = run_git_command('git fetch origin')
print(f"Result: {result['stdout'] if result['success'] else result.get('stderr', 'Error')}")

# 2. Отримання PR #4
print("\n[STEP 2] Fetching PR #4...")
result = run_git_command('git fetch origin pull/4/head:pr-4')
print(f"Result: {result['stdout'] if result['success'] else result.get('stderr', 'Error')}")

# 3. Показати останні коміти в PR
print("\n[STEP 3] Commits in PR #4:")
result = run_git_command('git log pr-4 --oneline -10')
if result['success']:
    print(result['stdout'])

# 4. Показати зміни
print("\n[STEP 4] Changes in PR #4:")
result = run_git_command('git diff main...pr-4 --stat')
if result['success']:
    print(result['stdout'])

# 5. Поточна гілка
print("\n[STEP 5] Current branch:")
result = run_git_command('git branch --show-current')
if result['success']:
    print(f"Current branch: {result['stdout'].strip()}")

# 6. Статус
print("\n[STEP 6] Git status:")
result = run_git_command('git status --short')
if result['success']:
    print(result['stdout'] if result['stdout'] else "Working tree clean")
