#!/usr/bin/env python3
"""
Football Event Data Visualization
Creates charts from the football match data
"""

import json
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

# Load data
print("🔄 Loading and analyzing football data...")
with open('/home/sohamkc/something/15946.json', 'r') as f:
    events_data = json.load(f)

# Extract information
event_types = Counter()
teams_data = defaultdict(lambda: {'events': 0, 'passes': 0, 'shots': 0, 'fouls': 0, 'interceptions': 0})
timeline = defaultdict(lambda: defaultdict(int))
player_events = defaultdict(lambda: {'count': 0, 'team': None})
team_names = set()

for event in events_data:
    # Event types
    if 'type' in event and isinstance(event['type'], dict):
        event_type = event['type'].get('name')
        event_types[event_type] += 1
    
    # Team data
    if 'team' in event and isinstance(event['team'], dict):
        team = event['team'].get('name')
        team_names.add(team)
        teams_data[team]['events'] += 1
        
        # Track specific events
        if event_type == 'Pass':
            teams_data[team]['passes'] += 1
        elif event_type == 'Shot':
            teams_data[team]['shots'] += 1
        elif event_type == 'Foul Committed':
            teams_data[team]['fouls'] += 1
        elif event_type == 'Interception':
            teams_data[team]['interceptions'] += 1
    
    # Timeline
    if 'minute' in event and 'team' in event and isinstance(event['team'], dict):
        interval = (event['minute'] // 5) * 5
        team = event['team'].get('name')
        timeline[interval][team] += 1
    
    # Players
    if isinstance(event.get('player'), dict):
        player_name = event['player'].get('name')
        if player_name:
            player_events[player_name]['count'] += 1
            if event.get('team') and isinstance(event['team'], dict):
                player_events[player_name]['team'] = event['team'].get('name')

teams = sorted(team_names)

# ============================================================================
# FIGURE 1: Event Type Distribution
# ============================================================================
print("Creating visualization 1: Event type distribution...")
fig, ax = plt.subplots(figsize=(12, 8))
top_events = dict(event_types.most_common(15))
events = list(top_events.keys())
counts = list(top_events.values())

colors = ['#FF6B6B' if i < 8 else '#4ECDC4' for i in range(len(events))]
bars = ax.barh(events, counts, color=colors)

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2, f' {int(width)}',
            ha='left', va='center', fontweight='bold')

ax.set_xlabel('Number of Events', fontsize=12, fontweight='bold')
ax.set_title('Top 15 Event Types in Barcelona vs Deportivo Alavés Match', fontsize=14, fontweight='bold')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/sohamkc/something/1_event_types.png', dpi=150, bbox_inches='tight')
print("✓ Saved: 1_event_types.png")

# ============================================================================
# FIGURE 2: Team Possession and Activity
# ============================================================================
print("Creating visualization 2: Team possession...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Pie chart
team_events = [teams_data[t]['events'] for t in teams]
colors_pie = ['#FF6B6B', '#4ECDC4']
ax1.pie(team_events, labels=teams, autopct='%1.1f%%', colors=colors_pie, 
        startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
ax1.set_title('Event Distribution by Team', fontsize=12, fontweight='bold')

# Bar chart - Total events
x_pos = range(len(teams))
bars = ax2.bar(x_pos, team_events, color=colors_pie, edgecolor='black', linewidth=1.5)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(teams, fontsize=11, fontweight='bold')
ax2.set_ylabel('Number of Events', fontsize=11, fontweight='bold')
ax2.set_title('Total Events by Team', fontsize=12, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/sohamkc/something/2_possession.png', dpi=150, bbox_inches='tight')
print("✓ Saved: 2_possession.png")

# ============================================================================
# FIGURE 3: Team Performance Metrics
# ============================================================================
print("Creating visualization 3: Team performance metrics...")
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

metrics = ['passes', 'shots', 'fouls', 'interceptions']
metric_labels = ['Passes', 'Shots', 'Fouls Committed', 'Interceptions']
colors_bar = ['#FF6B6B', '#4ECDC4']

for idx, (metric, label) in enumerate(zip(metrics, metric_labels)):
    ax = [ax1, ax2, ax3, ax4][idx]
    values = [teams_data[t][metric] for t in teams]
    
    bars = ax.bar(teams, values, color=colors_bar, edgecolor='black', linewidth=1.5)
    ax.set_ylabel('Count', fontsize=10, fontweight='bold')
    ax.set_title(label, fontsize=11, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('/home/sohamkc/something/3_performance_metrics.png', dpi=150, bbox_inches='tight')
print("✓ Saved: 3_performance_metrics.png")

# ============================================================================
# FIGURE 4: Match Timeline
# ============================================================================
print("Creating visualization 4: Match timeline...")
fig, ax = plt.subplots(figsize=(14, 6))

# Prepare timeline data
time_intervals = sorted(timeline.keys())
barcelona_counts = [timeline[t][teams[0]] for t in time_intervals]
alavez_counts = [timeline[t][teams[1]] for t in time_intervals]

x_labels = [f"{int(t)}-{int(t)+5}" for t in time_intervals]
x_pos = range(len(time_intervals))

width = 0.35
bars1 = ax.bar([x - width/2 for x in x_pos], barcelona_counts, width, label=teams[0], color='#FF6B6B', edgecolor='black', linewidth=0.5)
bars2 = ax.bar([x + width/2 for x in x_pos], alavez_counts, width, label=teams[1], color='#4ECDC4', edgecolor='black', linewidth=0.5)

ax.set_xlabel('Match Time (minutes)', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Events', fontsize=12, fontweight='bold')
ax.set_title('Event Activity Timeline (5-Minute Intervals)', fontsize=14, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels, rotation=45, ha='right', fontsize=9)
ax.legend(fontsize=11, loc='upper right')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('/home/sohamkc/something/4_timeline.png', dpi=150, bbox_inches='tight')
print("✓ Saved: 4_timeline.png")

# ============================================================================
# FIGURE 5: Top Players
# ============================================================================
print("Creating visualization 5: Top players...")
fig, ax = plt.subplots(figsize=(12, 8))

# Get top 15 players
sorted_players = sorted(player_events.items(), key=lambda x: x[1]['count'], reverse=True)[:15]
player_names = [p[0][:25] for p in sorted_players]  # Truncate long names
player_counts = [p[1]['count'] for p in sorted_players]
player_teams = [p[1]['team'] for p in sorted_players]

colors_players = ['#FF6B6B' if t == teams[0] else '#4ECDC4' for t in player_teams]

bars = ax.barh(player_names, player_counts, color=colors_players, edgecolor='black', linewidth=1)
ax.set_xlabel('Number of Events', fontsize=12, fontweight='bold')
ax.set_title('Top 15 Players by Event Contribution', fontsize=14, fontweight='bold')
ax.invert_yaxis()
ax.grid(axis='x', alpha=0.3)

# Add value labels
for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2., f' {int(width)}',
            ha='left', va='center', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.savefig('/home/sohamkc/something/5_top_players.png', dpi=150, bbox_inches='tight')
print("✓ Saved: 5_top_players.png")

# ============================================================================
# FIGURE 6: Comprehensive Dashboard
# ============================================================================
print("Creating visualization 6: Comprehensive dashboard...")
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)

# 1. Event types (top 8)
ax1 = fig.add_subplot(gs[0, :2])
top_8 = dict(event_types.most_common(8))
ax1.bar(range(len(top_8)), list(top_8.values()), color='steelblue', edgecolor='black', linewidth=1)
ax1.set_xticks(range(len(top_8)))
ax1.set_xticklabels(list(top_8.keys()), rotation=45, ha='right', fontsize=9)
ax1.set_ylabel('Count', fontsize=10, fontweight='bold')
ax1.set_title('Top 8 Event Types', fontsize=11, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# 2. Possession pie
ax2 = fig.add_subplot(gs[0, 2])
ax2.pie(team_events, labels=teams, autopct='%1.0f%%', colors=['#FF6B6B', '#4ECDC4'])
ax2.set_title('Possession %', fontsize=11, fontweight='bold')

# 3. Passes
ax3 = fig.add_subplot(gs[1, 0])
passes = [teams_data[t]['passes'] for t in teams]
ax3.bar(teams, passes, color=['#FF6B6B', '#4ECDC4'], edgecolor='black', linewidth=1.5)
ax3.set_ylabel('Count', fontsize=9, fontweight='bold')
ax3.set_title('Passes', fontsize=10, fontweight='bold')
ax3.tick_params(axis='x', rotation=45)
for i, v in enumerate(passes):
    ax3.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')

# 4. Shots
ax4 = fig.add_subplot(gs[1, 1])
shots = [teams_data[t]['shots'] for t in teams]
ax4.bar(teams, shots, color=['#FF6B6B', '#4ECDC4'], edgecolor='black', linewidth=1.5)
ax4.set_ylabel('Count', fontsize=9, fontweight='bold')
ax4.set_title('Shots', fontsize=10, fontweight='bold')
ax4.tick_params(axis='x', rotation=45)
for i, v in enumerate(shots):
    ax4.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')

# 5. Defensive actions
ax5 = fig.add_subplot(gs[1, 2])
defensive = [teams_data[t]['fouls'] + teams_data[t]['interceptions'] for t in teams]
ax5.bar(teams, defensive, color=['#FF6B6B', '#4ECDC4'], edgecolor='black', linewidth=1.5)
ax5.set_ylabel('Count', fontsize=9, fontweight='bold')
ax5.set_title('Defensive Actions', fontsize=10, fontweight='bold')
ax5.tick_params(axis='x', rotation=45)
for i, v in enumerate(defensive):
    ax5.text(i, v, str(v), ha='center', va='bottom', fontweight='bold')

# 6. Timeline comparison
ax6 = fig.add_subplot(gs[2, :])
time_intervals = sorted(timeline.keys())
barcelona_counts = [timeline[t][teams[0]] for t in time_intervals]
alavez_counts = [timeline[t][teams[1]] for t in time_intervals]
x_pos = range(len(time_intervals))
width = 0.35

ax6.bar([x - width/2 for x in x_pos], barcelona_counts, width, label=teams[0], color='#FF6B6B', edgecolor='black', linewidth=0.5)
ax6.bar([x + width/2 for x in x_pos], alavez_counts, width, label=teams[1], color='#4ECDC4', edgecolor='black', linewidth=0.5)

x_labels = [f"{int(t)}" for t in time_intervals[::2]]  # Every other label
ax6.set_xticks(range(0, len(time_intervals), 2))
ax6.set_xticklabels(x_labels)
ax6.set_xlabel('Match Time (minutes)', fontsize=10, fontweight='bold')
ax6.set_ylabel('Events', fontsize=10, fontweight='bold')
ax6.set_title('Event Timeline', fontsize=11, fontweight='bold')
ax6.legend(fontsize=9, loc='upper left')
ax6.grid(axis='y', alpha=0.3)

fig.suptitle('Football Match Analysis Dashboard: Barcelona vs Deportivo Alavés', 
             fontsize=14, fontweight='bold', y=0.995)

plt.savefig('/home/sohamkc/something/6_dashboard.png', dpi=150, bbox_inches='tight')
print("✓ Saved: 6_dashboard.png")

print("\n" + "="*60)
print("✓ ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("="*60)
print("\nSaved files:")
print("  • 1_event_types.png - Top 15 event types")
print("  • 2_possession.png - Team possession distribution")
print("  • 3_performance_metrics.png - Team performance comparison")
print("  • 4_timeline.png - Match timeline")
print("  • 5_top_players.png - Top 15 players")
print("  • 6_dashboard.png - Comprehensive dashboard")
print("\n")
