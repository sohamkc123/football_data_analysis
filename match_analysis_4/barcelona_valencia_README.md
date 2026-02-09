# Barcelona vs Valencia - Match Event Analysis ⚽📊

A professional, in-depth data analysis of the Barcelona vs Valencia football match, featuring advanced statistical analysis, tactical insights, and comprehensive visualizations.

## 🎯 Project Overview

This project delivers a complete analytical breakdown of a high-level football match between Barcelona and Valencia, examining 4,465 match events across 92 minutes of play. The analysis provides actionable insights for coaches, analysts, and football enthusiasts.

**Match Details:**
- **Teams**: Barcelona vs Valencia
- **Total Events**: 4,465
- **Match Duration**: 92 minutes
- **Players Tracked**: 27
- **Event Types**: 25+ categories

## 📊 Dataset Characteristics

### Event Distribution
- **Barcelona**: 2,793 events (62.6%)
- **Valencia**: 1,672 events (37.4%)

### Data Structure
```json
{
  "id": "event-id",
  "period": 1,
  "minute": 15,
  "event_type": "Pass",
  "team": "Barcelona",
  "player": "Player Name",
  "location": [x, y],
  "pass": {"length": 12.5, "angle": 45},
  "tactics": {"formation": 433}
}
```

## ✨ Key Features

### Comprehensive Analysis Modules
✅ **Event Distribution** - Frequency and pattern analysis  
✅ **Team Performance** - Head-to-head comparison metrics  
✅ **Temporal Analysis** - Match flow and momentum shifts  
✅ **Passing Networks** - Distribution, accuracy, and patterns  
✅ **Shot Analysis** - Shooting efficiency and locations  
✅ **Player Performance** - Individual contributions and rankings  
✅ **Defensive Metrics** - Pressure maps and defensive actions  
✅ **Possession Analysis** - Ball control and progression  
✅ **Play Patterns** - Tactical approaches and strategies  
✅ **Correlation Heatmaps** - Multi-dimensional pattern recognition  

### Professional Visualizations
✅ 9 high-resolution charts (300 DPI, publication-ready)  
✅ Team-specific color coding (Barcelona red, Valencia orange)  
✅ Interactive-ready notebook format  
✅ Consistent professional styling  

## 🚀 Quick Start

### Installation

1. **Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

2. **Run the analysis**

**Option A: Jupyter Notebook (Recommended)**
```bash
jupyter notebook barcelona_valencia_analysis.ipynb
```
Then: Cell → Run All

**Option B: View existing outputs**
- All visualizations are pre-generated in `barcelona_valencia_output/`

## 📈 Analysis Sections

### 1. Comprehensive Event Analysis
- Top 20 event types with frequency distribution
- Pie chart showing event concentration
- Team-wise event comparison
- Cumulative distribution analysis

**Key Insights:**
- Most common events: Passes, Ball Receipts, Carries
- Event diversity across teams
- 80/20 rule application to match events

### 2. Team Performance Comparison
- Total event distribution
- Key performance indicators (KPIs)
- Attacking vs defensive actions
- Possession share analysis

**Metrics Tracked:**
- Passes, Shots, Duels
- Interceptions, Clearances, Tackles
- Ball carries and progression
- Possession distribution

### 3. Temporal Match Flow
- Event intensity timeline
- Team activity patterns over time
- Period-wise breakdown
- Critical match moments identification

**Visualizations:**
- Match intensity curve
- Team activity comparison
- Period distribution bars

### 4. Advanced Pass Analysis
- Pass length distribution (mean, median, range)
- Pass outcome breakdown (complete vs incomplete)
- Pass accuracy by team
- Pass height and type analysis
- Team passing comparison

**Statistics:**
- Total passes analyzed
- Average pass length
- Completion rates
- Pass type diversity

### 5. Shot Analysis
- Shot frequency by team
- Shot outcomes distribution
- Shot types breakdown
- Body part usage statistics

**Deliverables:**
- Total shots comparison
- Goal conversion analysis
- Shot quality metrics

### 6. Player Performance
- Top 15 most active players
- Player event diversity
- Top passers ranking
- Team-wise player contributions

**Rankings:**
- Overall activity
- Passing specialists
- Defensive contributors

### 7. Defensive Actions
- Pressure intensity mapping
- Interception and tackle analysis
- Clearance patterns
- Top defensive players

**Metrics:**
- Total defensive actions
- Pressure timeline
- Team defensive comparison

### 8. Possession & Play Patterns
- Play pattern distribution
- Possession flow timeline
- Ball progression analysis
- Tactical approach identification

### 9. Correlation Heatmaps
- Period vs Event Type matrix
- Team vs Event Type analysis
- Pattern identification

## 📁 Project Structure

```
barcelona-valencia-analysis/
│
├── barcelona_valencia_analysis.ipynb    # Main Jupyter notebook
├── 16157.json                           # Match event dataset
├── README.md                            # This file
├── requirements.txt                     # Python dependencies
│
└── barcelona_valencia_output/           # Generated outputs
    ├── comprehensive_event_analysis.png
    ├── team_performance_analysis.png
    ├── temporal_match_analysis.png
    ├── advanced_pass_analysis.png
    ├── shot_analysis.png
    ├── player_performance_analysis.png
    ├── defensive_analysis.png
    ├── possession_playpattern_analysis.png
    ├── correlation_heatmaps.png
    ├── barcelona_valencia_processed_data.csv
    └── barcelona_valencia_summary_stats.json
```

## 🎨 Visualizations Gallery

### 1. Comprehensive Event Analysis
Four-panel visualization showing:
- Top 20 events horizontal bar chart
- Top 12 events pie chart
- Team event comparison
- Cumulative distribution curve

### 2. Team Performance Analysis
Multi-panel comparison featuring:
- Total events by team
- Key performance indicators
- Possession distribution pie chart
- Attacking vs defensive actions

### 3. Temporal Match Analysis
Timeline visualizations including:
- Overall event intensity curve
- Team-specific activity timelines
- Period comparison bars

### 4. Advanced Pass Analysis
Six-panel comprehensive pass breakdown:
- Pass length histogram with statistics
- Pass outcome pie chart
- Team pass comparison
- Pass height distribution
- Pass type ranking
- Passing accuracy bars

### 5. Shot Analysis
Four-panel shooting metrics:
- Total shots by team
- Shot outcome distribution
- Shot type breakdown
- Body part usage statistics

### 6. Player Performance Analysis
Four-panel player insights:
- Top 15 most active players
- Player event diversity (stacked bars)
- Top 10 passers
- Team player contributions

### 7. Defensive Analysis
Four-panel defensive metrics:
- Defensive action types
- Team defensive comparison
- Pressure intensity timeline
- Top 10 defensive players

### 8. Possession & Play Pattern Analysis
Four-panel tactical insights:
- Play pattern distribution
- Possession pie chart
- Possession flow timeline
- Ball carries by team

### 9. Correlation Heatmaps
Two comprehensive heatmaps:
- Period vs Event Type matrix
- Team vs Event Type analysis

## 📊 Key Statistics

### Match Overview
- **Total Events**: 4,465
- **Match Duration**: 92 minutes
- **Unique Event Types**: 25+
- **Total Players**: 27

### Event Distribution (Top 5)
1. Pass - ~30% of all events
2. Ball Receipt - ~24% of all events
3. Carry - ~23% of all events
4. Pressure - ~6% of all events
5. Ball Recovery - ~5% of all events

### Team Performance
**Barcelona:**
- 2,793 total events (62.6%)
- Dominant possession
- Higher passing volume
- More attacking actions

**Valencia:**
- 1,672 total events (37.4%)
- Counter-attacking approach
- More defensive actions
- Efficient ball usage

## 🛠️ Technical Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.7+ | Core language |
| Pandas | ≥1.3.0 | Data manipulation |
| NumPy | ≥1.21.0 | Numerical computing |
| Matplotlib | ≥3.4.0 | Visualization |
| Seaborn | ≥0.11.0 | Statistical graphics |
| Jupyter | ≥1.0.0 | Interactive analysis |

## 💡 Use Cases

### For Football Analysts
- Post-match performance review
- Opposition scouting reports
- Player recruitment analysis
- Tactical pattern recognition

### For Coaches
- Team performance assessment
- Training focus identification
- Tactical adjustment insights
- Player contribution evaluation

### For Data Scientists
- Sports analytics portfolio project
- Machine learning feature engineering
- Predictive modeling foundation
- Advanced statistical analysis

### For Researchers
- Football analytics methodology
- Event data processing techniques
- Visualization best practices
- Statistical sports analysis

## 🔧 Customization Guide

### Change Team Colors
```python
TEAM_COLORS = {
    'Barcelona': '#YOUR_COLOR',
    'Valencia': '#YOUR_COLOR'
}
```

### Add Custom Analysis
```python
# Example: Analyze specific player
player_name = "Lionel Messi"
player_events = df[df['player_name'] == player_name]
# Your analysis here
```

### Modify Visualization Style
```python
plt.style.use('your_style')
sns.set_palette("your_palette")
```

### Export Different Formats
```python
# Excel instead of CSV
df.to_excel('output.xlsx', index=False)

# PDF export
fig.savefig('output.pdf', format='pdf')
```

## 📖 Methodology

### Data Processing Pipeline
1. **Load** - Import JSON match event data
2. **Parse** - Extract nested event attributes
3. **Clean** - Handle missing values and outliers
4. **Enrich** - Calculate derived metrics
5. **Analyze** - Apply statistical methods
6. **Visualize** - Create professional charts
7. **Export** - Save results and insights

### Statistical Methods
- Descriptive statistics (mean, median, mode)
- Distribution analysis
- Correlation identification
- Temporal pattern recognition
- Comparative analysis

### Visualization Principles
- Consistent color schemes
- Clear labeling and titles
- Professional formatting
- High-resolution outputs
- Accessibility considerations

## 📚 Learning Outcomes

By exploring this project, you'll learn:

1. **Sports Data Analysis**
   - Event-level data processing
   - Football-specific metrics
   - Tactical insights extraction

2. **Data Science Skills**
   - Pandas advanced operations
   - Statistical visualization
   - Multi-dimensional analysis

3. **Professional Practices**
   - Code organization
   - Documentation standards
   - Reproducible research

## 🎓 Advanced Features

### Notebook Features
- **Interactive Exploration**: Modify parameters in real-time
- **Reproducible Results**: Consistent outputs every run
- **Modular Design**: Easy to extend with new analysis
- **Professional Documentation**: Clear explanations throughout

### Data Export
- **CSV Format**: Processed, clean dataset
- **JSON Format**: Structured summary statistics
- **High-Resolution Images**: Publication-ready visualizations

## ⚠️ Important Notes

### Data Considerations
- Events are timestamped with minute and second precision
- Some events contain location data (x, y coordinates)
- Player positions and formations are recorded
- Not all events have complete attribute sets

### Analysis Limitations
- Analysis based on available event data
- Some tactical nuances may not be captured
- Context-dependent events require domain knowledge
- Statistical patterns don't imply causation

## 🤝 Contributing

Contributions welcome! Areas for enhancement:
- Additional statistical methods
- Machine learning models
- Interactive dashboards
- Real-time analysis capabilities
- Video integration

## 📄 License

This project is provided for educational and analytical purposes. Ensure compliance with data usage agreements.

## 🙏 Acknowledgments

- Event data tracking systems
- Python data science community
- Sports analytics researchers
- Open-source contributors

## 📞 Support

For questions or issues:
1. Review the Jupyter notebook comments
2. Check example outputs
3. Consult Python documentation
4. Examine visualization code

## 🔄 Version History

- **v1.0** (February 2026)
  - Initial release
  - 9 visualization types
  - Complete analysis pipeline
  - Comprehensive documentation

---

## 🎯 Key Takeaways

### Match Insights
- Barcelona dominated possession and events (62.6%)
- Valencia focused on efficient counter-attacking
- Passing was the most frequent event type
- Both teams showed distinct tactical approaches

### Technical Quality
- Production-ready code and visualizations
- Comprehensive documentation
- Extensible architecture
- Professional presentation

### Learning Value
- Real-world sports analytics example
- Best practices in data visualization
- Statistical analysis methodology
- Professional project structure

---

**Ready to analyze? Open `barcelona_valencia_analysis.ipynb` and start exploring! ⚽📊**

*For the best experience, run the notebook cell by cell to understand each analysis step.*

---

**Project Status**: ✅ Production Ready  
**Last Updated**: February 2026  
**Maintained By**: Data Analysis Team
