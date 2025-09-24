"""
Git Status Checker for Lir Project
Проверяет состояние git репозитория и выдает рекомендации
"""

import os
import subprocess
from pathlib import Path
import sys

def run_git_command(command):
    """Выполняет git команду и возвращает результат"""
    try:
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent
        )
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return None, str(e), -1

def check_git_status():
    """Полная проверка состояния git"""
    print("=" * 60)
    print("    GIT REPOSITORY STATUS CHECK - LIR PROJECT")
    print("=" * 60)
    print()
    
    project_dir = Path(__file__).parent.parent
    git_dir = project_dir / '.git'
    
    # 1. Проверка наличия .git
    print("[1] Git Repository Check:")
    if git_dir.exists():
        print("    [OK] .git directory exists")
        print(f"    Location: {git_dir}")
    else:
        print("    [ERROR] .git directory NOT found!")
        print("    [!] Run: git init")
        return False
    
    # 2. Проверка конфигурации
    print("\n[2] Git Configuration:")
    stdout, stderr, code = run_git_command("git config user.name")
    if code == 0 and stdout:
        print(f"    User Name: {stdout.strip()}")
    else:
        print("    [!] User name not set")
        
    stdout, stderr, code = run_git_command("git config user.email")
    if code == 0 and stdout:
        print(f"    User Email: {stdout.strip()}")
    else:
        print("    [!] User email not set")
    
    # 3. Проверка веток
    print("\n[3] Branch Information:")
    stdout, stderr, code = run_git_command("git branch")
    if code == 0:
        branches = stdout.strip().split('\n')
        for branch in branches:
            if branch.startswith('*'):
                print(f"    Current Branch: {branch[2:]}")
            print(f"    {branch}")
    else:
        print("    [ERROR] Cannot get branches")
    
    # 4. Проверка remote
    print("\n[4] Remote Repositories:")
    stdout, stderr, code = run_git_command("git remote -v")
    if code == 0 and stdout:
        print("    Remote configured:")
        for line in stdout.strip().split('\n'):
            print(f"    {line}")
    else:
        print("    [!] No remote repository configured")
        print("    [+] To add GitHub remote:")
        print("        git remote add origin https://github.com/YOUR_USERNAME/Lir.git")
    
    # 5. Проверка коммитов
    print("\n[5] Commit History:")
    stdout, stderr, code = run_git_command("git log --oneline -5")
    if code == 0 and stdout:
        print("    Last 5 commits:")
        for line in stdout.strip().split('\n'):
            print(f"    {line}")
    else:
        print("    [!] No commits found or error reading log")
    
    # 6. Проверка статуса файлов
    print("\n[6] Working Directory Status:")
    stdout, stderr, code = run_git_command("git status --short")
    if code == 0:
        if stdout:
            print("    Uncommitted changes:")
            for line in stdout.strip().split('\n')[:10]:
                print(f"    {line}")
            if len(stdout.strip().split('\n')) > 10:
                print(f"    ... and {len(stdout.strip().split('\n')) - 10} more files")
        else:
            print("    [OK] Working directory clean")
    else:
        print("    [ERROR] Cannot get status")
    
    # 7. Рекомендации
    print("\n" + "=" * 60)
    print("RECOMMENDATIONS:")
    print("=" * 60)
    
    # Проверяем, нужно ли добавить remote
    stdout, stderr, code = run_git_command("git remote")
    if not stdout:
        print("\n[ACTION REQUIRED] Add GitHub remote:")
        print("1. Create repository on GitHub: https://github.com/new")
        print("   Name: Lir")
        print("   Description: German Learning Platform through King Lear")
        print("\n2. Connect local repository to GitHub:")
        print("   git remote add origin https://github.com/YOUR_USERNAME/Lir.git")
        print("   git branch -M main")
        print("   git push -u origin main")
    else:
        print("\n[OK] Remote repository configured")
        print("To push changes: git push")
    
    # Проверяем незакоммиченные изменения
    stdout, stderr, code = run_git_command("git status --porcelain")
    if stdout:
        print("\n[INFO] You have uncommitted changes")
        print("To commit all changes:")
        print("   git add .")
        print('   git commit -m "Your commit message"')
        print("   git push")
    
    print("\n" + "=" * 60)
    print("STATUS CHECK COMPLETE")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    os.chdir(Path(__file__).parent.parent)
    check_git_status()
