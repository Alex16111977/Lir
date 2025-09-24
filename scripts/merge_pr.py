"""
Script to merge Pull Request #1
"""
import subprocess
import os
import sys

def run_git_command(command, cwd):
    """Execute git command and return result"""
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        cwd=cwd,
        shell=True
    )
    return result

def main():
    repo_path = r'F:\AiKlientBank\Lir'
    os.chdir(repo_path)
    
    print("[MERGE PR #1 SCRIPT]")
    print("=" * 50)
    
    # 1. Fetch all branches
    print("\n[1] Fetching all branches...")
    result = run_git_command('git fetch --all', repo_path)
    print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # 2. Check current branch
    print("\n[2] Current branch...")
    result = run_git_command('git branch --show-current', repo_path)
    current_branch = result.stdout.strip()
    print("Current branch:", current_branch)
    
    # 3. Show remote branches
    print("\n[3] Remote branches...")
    result = run_git_command('git branch -r', repo_path)
    print(result.stdout)
    
    # 4. Try to checkout PR branch
    print("\n[4] Checking out PR branch...")
    result = run_git_command('git checkout origin/codex/integrate-interactive-exercises-from-kinglearcomic', repo_path)
    print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # 5. Return to main
    print("\n[5] Returning to main...")
    result = run_git_command('git checkout main', repo_path)
    print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # 6. Try merge
    print("\n[6] Attempting merge...")
    result = run_git_command('git merge origin/codex/integrate-interactive-exercises-from-kinglearcomic --no-edit', repo_path)
    print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    # 7. Check for conflicts
    print("\n[7] Checking for conflicts...")
    result = run_git_command('git status --short', repo_path)
    print(result.stdout)
    
    # 8. Show diff if any
    print("\n[8] Show changes...")
    result = run_git_command('git diff --stat', repo_path)
    print(result.stdout)
    
    print("\n" + "=" * 50)
    print("[SCRIPT COMPLETED]")

if __name__ == "__main__":
    main()
