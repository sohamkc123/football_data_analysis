# Quick Start Guide 🚀

## Getting Started in 3 Easy Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Choose Your Method

#### Option A: Interactive Jupyter Notebook (Recommended)
```bash
jupyter notebook football_match_analysis.ipynb
```
Then click "Cell" → "Run All"

#### Option B: Automated Python Script
```bash
python match_analysis.py
```

### Step 3: View Results
- All visualizations will be saved as PNG files (in `output/` folder for script)
- Processed data will be exported as CSV
- Summary statistics will be saved as JSON

---

## What You'll Get

### 📊 Visualizations (8 Charts)
1. **Event Type Distribution** - Bar chart and pie chart
2. **Team Performance Comparison** - Multi-team analysis
3. **Temporal Analysis** - Event intensity over time
4. **Pass Analysis** - Pass length and outcomes
5. **Possession Analysis** - Team possession share
6. **Play Patterns** - Tactical pattern distribution
7. **Top Players** - Most active players ranking
8. **Event Heatmap** - Period vs. event type correlation

### 📁 Data Exports
- `processed_match_data.csv` - Clean, structured data
- `summary_statistics.json` - Aggregated metrics

---

## System Requirements

- **Python**: 3.7 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 50MB for outputs
- **OS**: Windows, macOS, or Linux

---

## Troubleshooting

### Issue: "Module not found"
**Solution**: Install required packages
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Issue: "File not found: 19736.json"
**Solution**: Ensure the dataset is in the same directory
```bash
ls -la 19736.json
```

### Issue: Jupyter won't start
**Solution**: Try installing/updating Jupyter
```bash
pip install --upgrade jupyter notebook
```

---

## Need Help?

1. Check the **README.md** for detailed documentation
2. Review code comments in the notebook
3. Verify all dependencies are installed

---

**Happy Analyzing! 📊⚽**
