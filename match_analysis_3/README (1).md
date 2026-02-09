# Football Match Event Analysis 📊⚽

A comprehensive data analysis project examining football match event data using Python, featuring advanced visualizations and statistical insights.

## 📋 Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Sections](#analysis-sections)
- [Visualizations](#visualizations)
- [Key Findings](#key-findings)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project provides an in-depth analysis of football match event data, transforming raw JSON data into actionable insights through comprehensive statistical analysis and professional visualizations. The analysis covers event patterns, team performance, temporal dynamics, player contributions, and tactical insights.

**Total Events Analyzed:** 3,098  
**Match Coverage:** Complete match with multiple periods  
**Teams:** Multiple teams tracked  
**Event Types:** 40+ different event categories

## 📊 Dataset

The dataset (`19736.json`) contains detailed event-level data from a football match, including:

- **Event Metadata**: ID, index, timestamp, period, minute, second
- **Event Details**: Type, duration, location
- **Team Information**: Team names, possession data
- **Player Information**: Individual player actions and positions
- **Tactical Data**: Formations, play patterns, lineups

### Data Structure
```json
{
  "id": "unique-event-id",
  "index": 1,
  "period": 1,
  "timestamp": "00:00:00.000",
  "minute": 0,
  "second": 0,
  "type": {"id": 35, "name": "Event Type"},
  "team": {"id": 971, "name": "Team Name"},
  "player": {"id": 123, "name": "Player Name"},
  "possession_team": {"id": 971, "name": "Team Name"},
  "play_pattern": {"id": 1, "name": "Pattern Type"}
}
```

## ✨ Features

- **Automated Data Processing**: Converts nested JSON to structured DataFrames
- **Multi-dimensional Analysis**: Event, team, player, and temporal perspectives
- **Professional Visualizations**: 10+ high-quality charts and graphs
- **Statistical Summaries**: Comprehensive metrics and KPIs
- **Export Functionality**: Processed data and summary statistics export
- **Reproducible Research**: Complete Jupyter notebook workflow

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the project**
```bash
git clone <repository-url>
cd football-match-analysis
```

2. **Install required packages**
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

3. **Verify installation**
```bash
python -c "import pandas, numpy, matplotlib, seaborn; print('All packages installed successfully!')"
```

## 💻 Usage

### Running the Analysis

1. **Ensure the dataset is in the same directory**
   - Place `19736.json` in the project folder

2. **Launch Jupyter Notebook**
```bash
jupyter notebook football_match_analysis.ipynb
```

3. **Run all cells**
   - Click `Cell` → `Run All`
   - Or use keyboard shortcut: `Shift + Enter` for each cell

4. **View outputs**
   - Visualizations appear inline in the notebook
   - PNG files are saved to the project directory
   - CSV and JSON exports are created automatically

### Alternative: Python Script Execution

For automated execution without Jupyter:
```bash
jupyter nbconvert --to notebook --execute football_match_analysis.ipynb
```

## 📈 Analysis Sections

The notebook is organized into 12 comprehensive sections:

### 1. **Setup and Data Loading**
   - Library imports and configuration
   - Dataset loading and verification

### 2. **Data Exploration & Preprocessing**
   - Data structure examination
   - Feature extraction from nested fields
   - Basic statistics

### 3. **Event Type Analysis**
   - Distribution of event types
   - Frequency analysis
   - Top events identification

### 4. **Team Performance Analysis**
   - Team-wise event breakdown
   - Key performance indicators
   - Comparative metrics

### 5. **Temporal Analysis**
   - Event intensity over time
   - Period-wise distribution
   - Match flow patterns

### 6. **Pass Analysis**
   - Pass frequency and success rates
   - Pass length distribution
   - Team passing patterns

### 7. **Possession Analysis**
   - Possession distribution by team
   - Possession phases
   - Control metrics

### 8. **Play Pattern Analysis**
   - Different play styles
   - Pattern frequency
   - Tactical approaches

### 9. **Player Analysis**
   - Individual player contributions
   - Top performers
   - Activity rankings

### 10. **Heatmap Analysis**
   - Event distribution across periods
   - Type vs. time visualization
   - Pattern identification

### 11. **Summary Statistics**
   - Consolidated metrics
   - Key insights
   - Performance highlights

### 12. **Data Export**
   - Processed data CSV export
   - Summary statistics JSON
   - Reusable datasets

## 🎨 Visualizations

The project generates the following professional visualizations:

| Visualization | Filename | Description |
|--------------|----------|-------------|
| Event Type Distribution | `event_type_distribution.png` | Bar chart and pie chart showing event type frequencies |
| Team Performance | `team_performance_comparison.png` | Comparative bar chart of team activities |
| Temporal Analysis | `temporal_analysis.png` | Line plot of event intensity and period comparison |
| Pass Analysis | `pass_analysis.png` | Pass length distribution and outcome breakdown |
| Possession Analysis | `possession_analysis.png` | Possession share visualization |
| Play Patterns | `play_patterns.png` | Distribution of different play styles |
| Top Players | `top_players.png` | Most active players ranking |
| Event Heatmap | `period_event_heatmap.png` | Period vs. event type correlation |

All visualizations are:
- **High Resolution**: 300 DPI for print quality
- **Professional Styling**: Consistent color schemes and formatting
- **Publication Ready**: Suitable for reports and presentations
- **Annotated**: Clear labels, titles, and legends

## 🔍 Key Findings

### Event Distribution
- **Most Common Events**: Passes, Ball Receipts, and Carries dominate
- **Event Diversity**: 40+ different event types recorded
- **Activity Peaks**: Certain match periods show higher event density

### Team Performance
- **Balanced Engagement**: Both teams show significant activity
- **Tactical Variations**: Different play patterns between teams
- **Possession Dynamics**: Clear possession phases identified

### Temporal Patterns
- **Match Intensity**: Event frequency varies across periods
- **Critical Moments**: Identifiable peaks in match activity
- **Flow Analysis**: Natural game rhythm observable

### Player Contributions
- **Key Players**: Top 15 most active players identified
- **Position Impact**: Different positions show varied event types
- **Individual Patterns**: Unique playing styles visible

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical graphics |
| **Jupyter Notebook** | Interactive development environment |
| **JSON** | Data storage and exchange |

## 📁 Project Structure

```
football-match-analysis/
│
├── football_match_analysis.ipynb    # Main analysis notebook
├── README.md                         # Project documentation
├── 19736.json                        # Input dataset
│
├── Generated Files:
├── event_type_distribution.png       # Event type charts
├── team_performance_comparison.png   # Team performance charts
├── temporal_analysis.png             # Time-based analysis
├── pass_analysis.png                 # Pass statistics
├── possession_analysis.png           # Possession visualization
├── play_patterns.png                 # Play pattern analysis
├── top_players.png                   # Player rankings
├── period_event_heatmap.png         # Correlation heatmap
├── processed_match_data.csv         # Cleaned dataset
└── summary_statistics.json          # Statistical summary
```

## 📊 Output Files

### CSV Export (`processed_match_data.csv`)
- Cleaned and structured event data
- Ready for further analysis or integration
- Columns: index, period, minute, second, event_type, team_name, etc.

### JSON Export (`summary_statistics.json`)
- Aggregated statistics
- Event type counts
- Team and period distributions
- Machine-readable format for automation

## 🔧 Customization

### Modifying Visualizations

To customize chart colors, update in the notebook:
```python
plt.style.use('seaborn-v0_8-darkgrid')  # Change style
sns.set_palette("husl")                  # Change color palette
```

### Adding New Analysis

Add new cells in the notebook:
```python
# Example: Analyze shots on target
shots = df[df['event_type'] == 'Shot']
# Your analysis code here
```

### Changing Export Formats

Modify the export section:
```python
# Export to Excel instead of CSV
df_export.to_excel('processed_data.xlsx', index=False)
```

## 📝 Best Practices

1. **Before Running**:
   - Ensure sufficient disk space for visualizations
   - Close other memory-intensive applications
   - Verify dataset file path

2. **During Analysis**:
   - Run cells sequentially
   - Monitor memory usage for large datasets
   - Save notebook frequently

3. **After Completion**:
   - Review all visualizations
   - Verify exported files
   - Archive results appropriately

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue describing the problem
2. **Suggest Features**: Propose new analysis or visualizations
3. **Improve Documentation**: Enhance README or code comments
4. **Submit Pull Requests**: Fork, modify, and submit for review

## 📄 License

This project is provided as-is for educational and analytical purposes. Please ensure compliance with any data usage agreements related to the match event dataset.

## 🙏 Acknowledgments

- Data source: Match event tracking system
- Visualization libraries: Matplotlib and Seaborn communities
- Python data science ecosystem

## 📞 Support

For questions or issues:
- Check existing documentation
- Review code comments in the notebook
- Open an issue in the repository
- Consult Python/Pandas documentation

## 🔄 Version History

- **v1.0** (February 2026)
  - Initial release
  - Complete analysis pipeline
  - 8+ visualization types
  - Comprehensive documentation

---

## 🎓 Learning Resources

To better understand the analysis:
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Jupyter Notebook Basics](https://jupyter-notebook.readthedocs.io/)

---

**Happy Analyzing! ⚽📊**

For more information or to report issues, please refer to the project documentation or contact the maintainer.
