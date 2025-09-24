# GitHub Setup Instructions

## 🚀 Quick Start for GitHub

### 1. Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click "New repository" or go to [github.com/new](https://github.com/new)
3. Fill in repository details:
   - **Repository name**: `Lir`
   - **Description**: `German Learning Platform through King Lear - Interactive language learning with Shakespeare`
   - **Visibility**: Public (recommended) or Private
   - ✅ **Initialize with README**: NO (we already have one)
   - ✅ **Add .gitignore**: NO (already exists)
   - ✅ **Choose license**: NO (MIT license already added)

### 2. Connect Local Repository to GitHub

After creating the repository on GitHub, run these commands:

```bash
# Add GitHub as remote origin (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Lir.git

# Rename branch to main (GitHub standard)
git branch -M main

# Push to GitHub
git push -u origin main
```

### 3. Verify Upload

After pushing, your repository should contain:
- ✅ 51 JSON lesson files (A2, B1, thematic levels)
- ✅ Complete source code (`src/` directory)
- ✅ PDF generation tools (`book/` directory)
- ✅ Test suite and utilities (`test/` directory)
- ✅ Professional documentation (`README.md`, `CONTRIBUTING.md`)
- ✅ Requirements and configuration files

### 4. Repository Settings (Optional)

In your GitHub repository settings, you can:

1. **Add Topics/Tags**:
   - `german-language`
   - `language-learning`
   - `shakespeare`
   - `king-lear`
   - `education`
   - `python`
   - `pdf-generation`

2. **Enable GitHub Pages** (if you want to host the website):
   - Go to Settings → Pages
   - Source: Deploy from branch
   - Branch: main, folder: /output

3. **Add Repository Description**:
   ```
   🎭 Innovative German learning platform using Shakespeare's King Lear. Features 51 interactive lessons (A2/B1), PDF generation, vocabulary management, and web-based content creation. Perfect for intermediate German learners seeking engaging, literature-based language education.
   ```

### 5. Future Development Workflow

```bash
# Daily development workflow
git add .
git commit -m "Your descriptive commit message"
git push

# Create feature branch
git checkout -b feature-new-functionality
# ... make changes ...
git add .
git commit -m "Add new functionality"
git push -u origin feature-new-functionality
# Create Pull Request on GitHub
```

### 6. Collaboration Setup

If you want others to contribute:

1. **Enable Issues** in repository settings
2. **Add Collaborators** in Settings → Manage access
3. **Create Project Board** for task management
4. **Set up Branch Protection Rules** for main branch

### 7. Continuous Integration (Future)

Consider adding GitHub Actions for:
- ✅ Automated testing on push
- ✅ Code quality checks
- ✅ Automatic website deployment
- ✅ PDF generation on release

## 📞 Support

If you encounter issues:
1. Check [GitHub Docs](https://docs.github.com)
2. Ensure git is properly configured
3. Verify internet connection and GitHub access
4. Try using GitHub Desktop if command line fails

---

**🎯 Goal**: Make Lir accessible to the global German learning community through GitHub!
