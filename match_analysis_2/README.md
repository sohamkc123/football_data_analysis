# ⚽ Football Match Events Analysis

A comprehensive data analysis toolkit for football match managers and analysts, providing actionable insights from match event data through interactive visualizations and statistical analysis.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 📊 Overview

This project analyzes football match event data to extract meaningful insights for coaching staff and match analysts. It processes granular event-level data (passes, shots, tackles, etc.) to generate comprehensive performance metrics, visualizations, and tactical insights.

**Key Features:**
- 🎯 Real-time match event processing (3,388+ events analyzed)
- 📈 Interactive dashboards with Plotly visualizations
- 🤖 Machine learning-powered player clustering and performance prediction
- 📍 Spatial analysis of player positions and movements
- 🏆 Team and player performance metrics
- 📉 Advanced statistical analysis with scipy and sklearn

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.11+
Jupyter Notebook or JupyterLab
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/football-match-analysis.git
cd football-match-analysis
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Launch Jupyter Notebook**
```bash
jupyter notebook Football_Match_Analysis.ipynb
```

## 📦 Dependencies

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
plotly>=5.14.0
scipy>=1.10.0
```

Create a `requirements.txt`:
```bash
pip freeze > requirements.txt
```

## 📁 Project Structure

```
football-match-analysis/
│
├── match_analysis.ipynb   # Main analysis notebook
├── 16056.json                       # Sample match event data
├── README.md                        # Project documentation
```

## 🎯 Analysis Sections

### 1. **Data Loading & Exploration**
- Load JSON match event data
- Initial data exploration (3,388 events across 36 features)
- Data type inspection and validation

### 2. **Team Performance Metrics**
- Possession distribution analysis
- Pass accuracy comparison
- Shot conversion rates
- Goals and shooting efficiency
- Defensive actions (tackles, interceptions, fouls)

### 3. **Player Analytics**
- Individual player performance metrics
- Activity heatmaps
- Position-based analysis
- Top performers identification

### 4. **Advanced Analysis**
- **Machine Learning**: K-means clustering for player segmentation
- **PCA**: Dimensionality reduction for pattern discovery
- **Logistic Regression**: Performance outcome prediction
- **Statistical Testing**: Scipy-based hypothesis testing

### 5. **Interactive Visualizations**
- Comprehensive match dashboard
- Event momentum tracking (events per minute)
- Spatial analysis of player movements
- Real-time performance comparisons

## 📊 Sample Output

The notebook generates multiple visualization types:

1. **Possession Distribution** - Pie chart showing ball control
2. **Pass Accuracy Comparison** - Bar charts for team passing efficiency
3. **Shots & Goals** - Offensive performance metrics
4. **Defensive Actions** - Tackles, interceptions, and fouls
5. **Player Activity Heatmap** - Top 10 most active players
6. **Event Momentum** - Time-series of match intensity

## 🔧 Usage Example

```python
import pandas as pd
import json

# Load match data
with open('16056.json', 'r') as f:
    events = json.load(f)

# Convert to DataFrame
df = pd.json_normalize(events)

# Quick analysis
print(f"Total events: {len(df)}")
print(f"Teams: {df['team.name'].unique()}")
print(f"Event types: {df['type.name'].nunique()}")
```

## 📈 Key Insights Generated

- **Barcelona** vs **Opponent** match analysis
- Formation analysis (4-3-3 tactical setup)
- Player positioning and movement patterns
- Critical moments identification
- Performance trends over match time

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Data Format

The analysis expects JSON data with the following structure:

```json
{
  "id": "event-uuid",
  "index": 1,
  "period": 1,
  "timestamp": "00:00:00.000",
  "minute": 0,
  "second": 0,
  "type": {"id": 30, "name": "Pass"},
  "team": {"id": 217, "name": "Barcelona"},
  "player": {"id": 5503, "name": "Lionel Messi"},
  "location": [60.0, 40.0],
  "pass": {...},
  ...
}
```

## 🎓 Use Cases

- **Coaching Staff**: Post-match tactical analysis
- **Performance Analysts**: Player evaluation and recruitment
- **Sports Scientists**: Physical performance tracking
- **Scouts**: Opposition analysis and scouting reports
- **Researchers**: Football analytics research and education

## ⚠️ Notes

- Data sample includes 3,388 match events
- Visualizations require sufficient screen resolution for optimal viewing
- Processing time depends on dataset size (avg. 2-3 seconds per 1000 events)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- StatsBomb for open football data standards
- The football analytics community
- Plotly and scikit-learn development teams

## 📧 Contact

**Soham KC** - [@soham.kc.1](https://www.instagram.com/soham.kc.1/) - lapsipurenep@gmail.com


---

⭐ **Star this repository** if you find it helpful!

🐛 **Found a bug?** [Open an issue](https://github.com/yourusername/football-match-analysis/issues)

💡 **Have a suggestion?** We'd love to hear it!
