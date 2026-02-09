#!/usr/bin/env python3
"""
Football Match Event Analysis - Automated Script
=================================================

This script provides automated analysis of football match event data.
Run this as an alternative to the Jupyter notebook for batch processing.

Usage:
    python match_analysis.py

Author: Data Analysis Project
Date: February 2026
"""

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import warnings
import sys
import os

warnings.filterwarnings('ignore')

# Configuration
DATA_FILE = '19736.json'
OUTPUT_DIR = 'output'
DPI = 300

def setup_environment():
    """Setup visualization environment and create output directory."""
    print("="*80)
    print("FOOTBALL MATCH EVENT ANALYSIS")
    print("="*80)
    print("\n[1/10] Setting up environment...")
    
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"✓ Created output directory: {OUTPUT_DIR}/")
    
    print("✓ Environment configured successfully")

def load_data():
    """Load and perform initial data processing."""
    print("\n[2/10] Loading dataset...")
    
    if not os.path.exists(DATA_FILE):
        print(f"❌ Error: Dataset file '{DATA_FILE}' not found!")
        print("Please ensure the data file is in the same directory.")
        sys.exit(1)
    
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    
    print(f"✓ Dataset loaded: {len(data):,} events")
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Extract nested fields
    df['event_type'] = df['type'].apply(lambda x: x.get('name', 'Unknown') if isinstance(x, dict) else 'Unknown')
    df['team_name'] = df['team'].apply(lambda x: x.get('name', 'Unknown') if isinstance(x, dict) else 'Unknown')
    df['possession_team_name'] = df['possession_team'].apply(lambda x: x.get('name', 'Unknown') if isinstance(x, dict) else 'Unknown')
    df['play_pattern_name'] = df['play_pattern'].apply(lambda x: x.get('name', 'Unknown') if isinstance(x, dict) else 'Unknown')
    
    print(f"✓ Data processed: {len(df.columns)} features extracted")
    
    return df

def analyze_events(df):
    """Analyze event distribution."""
    print("\n[3/10] Analyzing event distribution...")
    
    event_counts = df['event_type'].value_counts()
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Bar chart
    event_counts.head(15).plot(kind='barh', ax=axes[0], color='steelblue')
    axes[0].set_title('Top 15 Event Types', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Frequency', fontsize=12)
    axes[0].set_ylabel('Event Type', fontsize=12)
    axes[0].grid(axis='x', alpha=0.3)
    
    # Pie chart
    colors = plt.cm.Set3(range(10))
    event_counts.head(10).plot(kind='pie', ax=axes[1], autopct='%1.1f%%', 
                                startangle=90, colors=colors)
    axes[1].set_title('Top 10 Event Types (% Distribution)', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('')
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/event_type_distribution.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print(f"✓ Event analysis complete: {df['event_type'].nunique()} unique event types")
    return event_counts

def analyze_teams(df):
    """Analyze team performance."""
    print("\n[4/10] Analyzing team performance...")
    
    team_events = df.groupby(['team_name', 'event_type']).size().unstack(fill_value=0)
    
    key_events = ['Pass', 'Shot', 'Duel', 'Interception', 'Clearance', 'Foul Committed']
    available_events = [e for e in key_events if e in team_events.columns]
    
    if available_events:
        fig, ax = plt.subplots(figsize=(14, 6))
        team_events[available_events].plot(kind='bar', ax=ax, width=0.8)
        ax.set_title('Team Performance Comparison - Key Events', fontsize=14, fontweight='bold')
        ax.set_xlabel('Team', fontsize=12)
        ax.set_ylabel('Event Count', fontsize=12)
        ax.legend(title='Event Type', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/team_performance_comparison.png', dpi=DPI, bbox_inches='tight')
        plt.close()
    
    print(f"✓ Team analysis complete: {df['team_name'].nunique()} teams analyzed")

def analyze_temporal(df):
    """Analyze temporal patterns."""
    print("\n[5/10] Analyzing temporal patterns...")
    
    time_df = df.groupby('minute').size().reset_index(name='event_count')
    
    fig, axes = plt.subplots(2, 1, figsize=(14, 10))
    
    # Line plot
    axes[0].plot(time_df['minute'], time_df['event_count'], marker='o', 
                 linewidth=2, markersize=4, color='darkblue', alpha=0.7)
    axes[0].fill_between(time_df['minute'], time_df['event_count'], alpha=0.3)
    axes[0].set_title('Match Event Intensity Over Time', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Minute', fontsize=12)
    axes[0].set_ylabel('Number of Events', fontsize=12)
    axes[0].grid(True, alpha=0.3)
    axes[0].axvline(x=45, color='red', linestyle='--', alpha=0.5, label='Half-time')
    axes[0].legend()
    
    # Period comparison
    period_counts = df['period'].value_counts().sort_index()
    axes[1].bar(period_counts.index, period_counts.values, 
                color=['#3498db', '#e74c3c', '#2ecc71'][:len(period_counts)])
    axes[1].set_title('Events by Match Period', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Period', fontsize=12)
    axes[1].set_ylabel('Event Count', fontsize=12)
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/temporal_analysis.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("✓ Temporal analysis complete")

def analyze_passes(df):
    """Analyze pass patterns."""
    print("\n[6/10] Analyzing pass patterns...")
    
    passes = df[df['event_type'] == 'Pass'].copy()
    
    if len(passes) > 0 and 'pass' in passes.columns:
        passes['pass_length'] = passes['pass'].apply(
            lambda x: x.get('length', np.nan) if isinstance(x, dict) else np.nan
        )
        passes['pass_outcome'] = passes['pass'].apply(
            lambda x: x.get('outcome', {}).get('name', 'Complete') if isinstance(x, dict) else 'Complete'
        )
        
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        
        # Pass length distribution
        valid_lengths = passes['pass_length'].dropna()
        if len(valid_lengths) > 0:
            axes[0].hist(valid_lengths, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
            axes[0].axvline(valid_lengths.mean(), color='red', linestyle='--', 
                           linewidth=2, label=f'Mean: {valid_lengths.mean():.1f}m')
            axes[0].set_title('Pass Length Distribution', fontsize=14, fontweight='bold')
            axes[0].set_xlabel('Pass Length (meters)', fontsize=12)
            axes[0].set_ylabel('Frequency', fontsize=12)
            axes[0].legend()
            axes[0].grid(axis='y', alpha=0.3)
        
        # Pass outcomes
        outcome_counts = passes['pass_outcome'].value_counts()
        axes[1].pie(outcome_counts.values, labels=outcome_counts.index, autopct='%1.1f%%',
                   startangle=90, colors=plt.cm.Pastel1(range(len(outcome_counts))))
        axes[1].set_title('Pass Outcomes', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/pass_analysis.png', dpi=DPI, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Pass analysis complete: {len(passes):,} passes analyzed")
    else:
        print("⚠ No pass data available for detailed analysis")

def analyze_possession(df):
    """Analyze possession distribution."""
    print("\n[7/10] Analyzing possession...")
    
    possession_stats = df['possession_team_name'].value_counts()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    wedges, texts, autotexts = ax.pie(possession_stats.values, 
                                        labels=possession_stats.index,
                                        autopct='%1.1f%%',
                                        startangle=90,
                                        colors=colors[:len(possession_stats)],
                                        explode=[0.05] * len(possession_stats),
                                        shadow=True)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)
    
    ax.set_title('Possession Distribution', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/possession_analysis.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("✓ Possession analysis complete")

def analyze_play_patterns(df):
    """Analyze play patterns."""
    print("\n[8/10] Analyzing play patterns...")
    
    play_patterns = df['play_pattern_name'].value_counts()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.barh(play_patterns.index, play_patterns.values, color='coral')
    
    for i, (bar, value) in enumerate(zip(bars, play_patterns.values)):
        ax.text(value, i, f' {value:,}', va='center', fontweight='bold')
    
    ax.set_title('Play Patterns Distribution', fontsize=14, fontweight='bold')
    ax.set_xlabel('Frequency', fontsize=12)
    ax.set_ylabel('Play Pattern', fontsize=12)
    ax.grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/play_patterns.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("✓ Play pattern analysis complete")

def analyze_players(df):
    """Analyze player contributions."""
    print("\n[9/10] Analyzing player contributions...")
    
    player_events = []
    for idx, row in df.iterrows():
        if 'player' in row and isinstance(row['player'], dict):
            player_events.append({
                'player_name': row['player'].get('name', 'Unknown'),
                'event_type': row['event_type'],
                'team': row['team_name']
            })
    
    if player_events:
        player_df = pd.DataFrame(player_events)
        top_players = player_df['player_name'].value_counts().head(15)
        
        fig, ax = plt.subplots(figsize=(12, 8))
        bars = ax.barh(range(len(top_players)), top_players.values, color='mediumpurple')
        ax.set_yticks(range(len(top_players)))
        ax.set_yticklabels(top_players.index)
        ax.set_xlabel('Number of Events', fontsize=12)
        ax.set_ylabel('Player', fontsize=12)
        ax.set_title('Top 15 Most Active Players', fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        
        for i, (bar, value) in enumerate(zip(bars, top_players.values)):
            ax.text(value, i, f' {value}', va='center', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/top_players.png', dpi=DPI, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Player analysis complete: {len(top_players)} top players identified")
    else:
        print("⚠ No player data available")

def create_heatmap(df):
    """Create period-event heatmap."""
    print("\n[10/10] Creating heatmap visualization...")
    
    period_event_matrix = df.groupby(['period', 'event_type']).size().unstack(fill_value=0)
    top_event_types = df['event_type'].value_counts().head(10).index
    period_event_matrix = period_event_matrix[top_event_types]
    
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.heatmap(period_event_matrix.T, annot=True, fmt='d', cmap='YlOrRd', 
                cbar_kws={'label': 'Event Count'}, ax=ax, linewidths=0.5)
    ax.set_title('Event Distribution: Period vs Event Type', fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Period', fontsize=12)
    ax.set_ylabel('Event Type', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/period_event_heatmap.png', dpi=DPI, bbox_inches='tight')
    plt.close()
    
    print("✓ Heatmap created successfully")

def export_data(df):
    """Export processed data and statistics."""
    print("\nExporting processed data...")
    
    # Export CSV
    df_export = df[['index', 'period', 'minute', 'second', 'event_type', 
                    'team_name', 'possession_team_name', 'play_pattern_name', 'duration']].copy()
    df_export.to_csv(f'{OUTPUT_DIR}/processed_match_data.csv', index=False)
    print(f"✓ Processed data exported to '{OUTPUT_DIR}/processed_match_data.csv'")
    
    # Export summary statistics
    summary_stats = {
        'total_events': len(df),
        'event_types': df['event_type'].value_counts().to_dict(),
        'team_distribution': df['team_name'].value_counts().to_dict(),
        'period_distribution': df['period'].value_counts().to_dict()
    }
    
    with open(f'{OUTPUT_DIR}/summary_statistics.json', 'w') as f:
        json.dump(summary_stats, f, indent=2)
    print(f"✓ Summary statistics exported to '{OUTPUT_DIR}/summary_statistics.json'")

def print_summary(df, event_counts):
    """Print comprehensive summary."""
    print("\n" + "="*80)
    print("MATCH ANALYSIS SUMMARY")
    print("="*80)
    
    print("\n📊 GENERAL STATISTICS")
    print("-" * 80)
    print(f"Total Events Recorded: {len(df):,}")
    print(f"Unique Event Types: {df['event_type'].nunique()}")
    print(f"Match Duration: {df['minute'].max()} minutes")
    print(f"Number of Periods: {df['period'].nunique()}")
    
    print("\n⚽ TOP 5 EVENT TYPES")
    print("-" * 80)
    for i, (event, count) in enumerate(event_counts.head(5).items(), 1):
        pct = (count / len(df)) * 100
        print(f"{i}. {event}: {count:,} ({pct:.1f}%)")
    
    print("\n👥 TEAM STATISTICS")
    print("-" * 80)
    for team, count in df['team_name'].value_counts().items():
        pct = (count / len(df)) * 100
        print(f"{team}: {count:,} events ({pct:.1f}%)")
    
    print("\n⏱️ PERIOD STATISTICS")
    print("-" * 80)
    for period in sorted(df['period'].unique()):
        period_data = df[df['period'] == period]
        print(f"Period {period}: {len(period_data):,} events")
    
    print("\n" + "="*80)
    print("✓ ANALYSIS COMPLETE!")
    print("="*80)
    print(f"\nAll visualizations saved to '{OUTPUT_DIR}/' directory")
    print("Check the output folder for:")
    print("  - 8 high-resolution PNG visualizations")
    print("  - processed_match_data.csv")
    print("  - summary_statistics.json")
    print("\n" + "="*80)

def main():
    """Main execution function."""
    try:
        setup_environment()
        df = load_data()
        event_counts = analyze_events(df)
        analyze_teams(df)
        analyze_temporal(df)
        analyze_passes(df)
        analyze_possession(df)
        analyze_play_patterns(df)
        analyze_players(df)
        create_heatmap(df)
        export_data(df)
        print_summary(df, event_counts)
        
        print("\n✅ Script execution successful!")
        return 0
        
    except Exception as e:
        print(f"\n❌ Error during execution: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
