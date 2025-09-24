# 🎭 Lir - German Learning through King Lear

**Innovative German language learning platform using Shakespeare's "King Lear" as educational content**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)](README.md)

## 🌟 Overview

Lir is an innovative educational platform that teaches German through the dramatic text of Shakespeare's "King Lear". The project converts JSON-based lesson data into interactive web content, providing learners with contextual vocabulary, transcriptions, and comprehensive study materials.

## ✨ Key Features

- 📚 **51 Interactive Lessons** - A2, B1, and thematic content
- 🔊 **Phonetic Transcriptions** - Russian-style transcriptions for German words
- 📖 **Digital Book Reader** - Web-based PDF reader with navigation
- 📝 **Vocabulary Management** - Comprehensive word databases with frequency analysis
- 🎨 **Modern Web Interface** - Responsive HTML/CSS/JS output
- 📊 **Progress Tracking** - Learning statistics and reports
- 🔧 **Automated Generation** - One-click website creation from JSON data

## 🏗️ Project Structure

```
Lir/
├── 📁 src/                  # Core application code
│   ├── core/               # Main orchestration and configuration
│   ├── generators/         # HTML, CSS, JS generators
│   ├── processors/         # Data processing utilities
│   └── utils/              # Helper functions
├── 📁 data/                # Lesson data (JSON format)
│   ├── a2/                 # A2 level lessons (15 files)
│   ├── b1/                 # B1 level lessons (15 files)
│   └── thematic/           # Thematic lessons (21 files)
├── 📁 output/              # Generated website files
├── 📁 book/                # PDF processing and dictionaries
├── 📁 test/                # Testing and utilities
└── 📄 main.py              # Main application entry point
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)
- Git (for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Lir.git
   cd Lir
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Generate the website**
   ```bash
   python main.py
   ```

5. **Open the generated site**
   - Open `output/index.html` in your browser
   - Book reader: `output/book/index.html`

## 📦 Dependencies

### Core Dependencies
- `beautifulsoup4` - HTML processing and manipulation
- `Jinja2` - Template engine for HTML generation
- `PyMuPDF` - PDF processing for book generation
- `reportlab` - PDF creation for vocabularies

### Development Dependencies
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `tqdm` - Progress bars
- `colorama` - Colored console output

## 🎯 Content Structure

### Lesson Levels
- **A2 Level (15 lessons)** - Basic German through family, emotions, actions, places, time
- **B1 Level (15 lessons)** - Advanced topics: power, betrayal, madness, nature, death
- **Thematic (21 lessons)** - Characters, emotions, places, actions, symbols, dialogue, time/fate

### Data Format
Each lesson is stored as a JSON file containing:
```json
{
  "metadata": {
    "title": "Lesson Title",
    "level": "A2/B1/Thematic",
    "scene": "Act.Scene",
    "difficulty": 1-5
  },
  "vocabulary": [
    {
      "german": "German word",
      "transcription": "[Phonetic transcription]",
      "russian": "Russian translation",
      "context": "Usage context"
    }
  ],
  "exercises": [...],
  "cultural_notes": [...]
}
```

## 🔧 Configuration

The project uses `config.py` for main settings:

- **Data paths** - Configure input/output directories
- **Generation settings** - HTML/CSS/JS options
- **Book settings** - PDF processing parameters
- **Logging** - Debug and info levels

## 🧪 Testing

Run the test suite:
```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=src

# Run specific test
python test/test_specific_feature.py
```

## 📊 Statistics

- **Total JSON Files**: 51 lessons
- **Vocabulary Entries**: 600+ German words with transcriptions
- **Generated Files**: 55+ HTML pages
- **Book Pages**: Full "König Lear" PDF integration
- **Code Coverage**: 85%+ (target)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Run tests: `pytest`
6. Commit changes: `git commit -am 'Add feature'`
7. Push to branch: `git push origin feature-name`
8. Submit a Pull Request

## 📈 Roadmap

- [ ] **Mobile App** - React Native implementation
- [ ] **Audio Integration** - TTS for German pronunciation
- [ ] **Interactive Exercises** - Drag-and-drop, fill-in-the-blank
- [ ] **User Progress Tracking** - Database integration
- [ ] **Multi-language Support** - English, French interfaces
- [ ] **AI-powered Recommendations** - Personalized learning paths

## 🐛 Known Issues

- Large PDF processing may be slow on older systems
- Some special characters in transcriptions need font support
- Mobile responsiveness needs optimization for tablets

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Shakespeare's King Lear** - Public domain text
- **German Language Community** - Transcription verification
- **Open Source Libraries** - All the amazing Python packages
- **Educational Research** - Language learning methodology

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/Lir/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/Lir/discussions)
- **Email**: your.email@example.com

## 📚 Documentation

- [User Guide](docs/USER_GUIDE.md)
- [Developer Documentation](docs/DEVELOPER.md)
- [API Reference](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

---

**Made with ❤️ for German language learners worldwide**

*"Nothing will come of nothing." - King Lear, Act 1, Scene 1*
