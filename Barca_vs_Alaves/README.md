# Football Event Data Analysis - Complete Solution

## 📋 Project Overview

This is a **comprehensive football data analysis** of a match between **Barcelona** and **Deportivo Alavés**, based on detailed event-level data from `15946.json`.

### What's Included:
- ✅ **Complete statistical analysis** of 3,762 football events
- ✅ **6 professional visualizations** with charts and dashboards
- ✅ **Multiple analysis scripts** for reproducibility
- ✅ **Detailed performance metrics** for both teams
- ✅ **Player-level event tracking** for all 28 players
- ✅ **Match timeline analysis** with 5-minute intervals

---

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| **Total Events** | 3,762 |
| **Teams** | Barcelona vs Deportivo Alavés |
| **Players** | 28 total |
| **Match Duration** | 92 minutes |
| **Possession (Barcelona)** | 74.1% |
| **Possession (Alavés)** | 25.9% |
| **Barcelona Passes** | 917 |
| **Barcelona Shots** | 25 |
| **Alavés Passes** | 246 |
| **Alavés Shots** | 3 |

---

## 📈 Analysis Files

### Python Scripts
1. **`football_analysis_pure.py`** (10 KB)
   - Pure Python implementation (no external dependencies)
   - Generates comprehensive statistics
   - Creates text report: `football_analysis_report.txt`
   
2. **`football_visualization.py`** (13 KB)
   - Creates all 6 PNG visualizations
   - Uses matplotlib for high-quality charts
   - Generates dashboard summary
   
3. **`football_analysis.py`** & **`football_analysis_simple.py`**
   - Alternative analysis implementations
   - Pandas-based analysis options

### How to Run

```bash
# Install dependencies (optional for visualizations)
pip install pandas numpy matplotlib seaborn

# Run pure Python analysis (no dependencies)
python3 football_analysis_pure.py

# Generate visualizations
python3 football_visualization.py
```

---

## 📊 Visualizations

### 1. **Event Type Distribution** (`1_event_types.png`)
Top 15 event types in the match
- **Key**: Passes (30.9%), Ball Receipts (28.1%), Carries (23.7%)

### 2. **Team Possession** (`2_possession.png`)
Possession split between teams
- **Barcelona**: 74.1% (dominant)
- **Alavés**: 25.9% (counter-attacking)

### 3. **Performance Metrics** (`3_performance_metrics.png`)
4-chart comparison of:
- Passes: Barcelona 917 vs Alavés 246
- Shots: Barcelona 25 vs Alavés 3
- Fouls: Barcelona 7 vs Alavés 16
- Interceptions: Barcelona 6 vs Alavés 18

### 4. **Match Timeline** (`4_timeline.png`)
Event frequency by 5-minute intervals
- Shows activity patterns throughout match
- Barcelona maintained high activity
- Alavés had targeted pressure moments

### 5. **Top Players** (`5_top_players.png`)
Top 15 players by event contribution
- Ivan Rakitić (408), Jordi Alba (355), Messi (304)
- Color-coded by team (Red: Barcelona, Teal: Alavés)

### 6. **Comprehensive Dashboard** (`6_dashboard.png`)
Full analytical dashboard with all key metrics
- Event types, possession, passes, shots, defense, timeline

---

## 🎯 Key Findings

### Barcelona's Dominance
- **Possession**: 74.1% of all events
- **Passing**: 917 passes vs 246 by Alavés (3.7x more)
- **Shot Creation**: 25 shots vs 3 by Alavés
- **Passing Rate**: 29.4% of possession events
- **Style**: Possession-based, short passing, patient build-up

### Alavés' Defensive Strategy
- **Possession**: 25.9% (counter-attacking approach)
- **Pressure**: 142 pressure actions vs 70 by Barcelona
- **Defense**: 32 clearances, 18 interceptions
- **Fouls**: 16 fouls (physical approach to defense)
- **Style**: Compact defense, quick transitions, pressure tactics

### Top Performers

**Barcelona**:
1. Ivan Rakitić - 408 events (midfielder control)
2. Jordi Alba - 355 events (left-side dominance)
3. Lionel Messi - 304 events (attacking presence)

**Alavés**:
1. Ibai Gómez - 110 events
2. Manuel García - 103 events
3. Mubarak Wakaso - 97 events

---

## 📁 Directory Structure

```
/home/sohamkc/something/
├── 15946.json                          # Original event data (3,762 events)
├── README.md                           # This file
├── ANALYSIS_REPORT.md                  # Detailed analysis report
│
├── Scripts:
├── football_analysis_pure.py           # Pure Python analysis ⭐
├── football_visualization.py           # Chart generation
├── football_analysis.py                # Alternative implementation
├── football_analysis_simple.py         # Simplified version
│
├── Reports:
├── football_analysis_report.txt        # Text summary
│
└── Visualizations (PNG charts):
    ├── 1_event_types.png               # Top 15 event types (82 KB)
    ├── 2_possession.png                # Possession analysis (64 KB)
    ├── 3_performance_metrics.png       # Team performance (74 KB)
    ├── 4_timeline.png                  # Match timeline (67 KB)
    ├── 5_top_players.png               # Top 15 players (110 KB)
    └── 6_dashboard.png                 # Dashboard summary (157 KB)
```

---

## 💻 Technical Details

### Data Source
- **Format**: JSON (3,762 events)
- **Schema**: Event-level data with:
  - Timestamp and match minute
  - Team and player identification
  - Event type classification
  - Possession sequence tracking
  - Match tactics and formations

### Analysis Methodology
1. **Data Loading**: Parse 3,762 events from JSON
2. **Aggregation**: Group by team, player, event type
3. **Statistics**: Calculate rates, percentages, and efficiency metrics
4. **Visualization**: Create 6 high-quality charts using matplotlib
5. **Summary**: Generate comprehensive analysis report

### Event Types Tracked (24 total)
- Pass, Shot, Tackle, Duel, Pressure, Carry
- Clearance, Interception, Block, Dribble
- Foul Committed, Dispossessed, Ball Recovery
- Substitution, and more...

---

## 🎓 Educational Value

This analysis demonstrates:
- ✅ Data parsing and cleaning
- ✅ Statistical aggregation techniques
- ✅ Performance metrics calculation
- ✅ Data visualization best practices
- ✅ Sports analytics methodology
- ✅ Python programming for data analysis

---

## 🔍 Interpretation Guide

### Possession %
- **Barcelona (74.1%)**: Controlled match with ball dominance
- **Alavés (25.9%)**: Counter-attacking, winning ball back quickly

### Pass Rate (passes per possession event)
- **Barcelona (29.4%)**: Patient, possession-focused
- **Alavés (38.2%)**: Efficient, direct play

### Shot Conversion
- **Barcelona (2.73%)**: Creating many chances
- **Alavés (1.22%)**: Limited attacking opportunities

### Pressure Actions
- **Alavés (142 > 70)**: More aggressive defense
- **Barcelona (70)**: Conservative, relying on possession

---

## 🚀 How to Use

### View Analysis
```bash
# Read detailed report
cat ANALYSIS_REPORT.md

# View summary statistics
python3 football_analysis_pure.py
```

### Regenerate Visualizations
```bash
# Install matplotlib and numpy
pip install matplotlib numpy

# Generate all charts
python3 football_visualization.py
```

### Extend Analysis
The scripts are modular and can be extended to:
- Calculate xG (expected goals)
- Generate player heat maps
- Analyze passing networks
- Track positional data

---

## 📞 Analysis Summary

**Match**: Barcelona vs Deportivo Alavés
**Date**: Event data from 15946.json
**Duration**: 92 minutes (2 periods)
**Events**: 3,762 total
**Teams**: 2
**Players**: 28
**Event Types**: 24

**Conclusion**: Barcelona dominated with 74% possession, 917 passes, and 25 shots, while Alavés employed an aggressive defensive strategy with 142 pressure actions and 16 fouls despite limited possession (25.9%).

---

**Generated**: January 31, 2026
**Analysis Type**: Complete statistical and visual analysis
**Status**: ✅ Complete and Ready to Use
