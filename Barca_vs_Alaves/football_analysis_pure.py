#!/usr/bin/env python3
"""
Football Event Data Analysis
Analyzes 15946.json containing football match events
"""

import json
from collections import Counter, defaultdict

# Load data
print("🔄 Loading football events data...")
with open('/home/sohamkc/something/15946.json', 'r') as f:
    events_data = json.load(f)

print(f"✓ Loaded {len(events_data)} events\n")

# ============================================================================
# DATASET OVERVIEW
# ============================================================================
print("="*70)
print("DATASET OVERVIEW")
print("="*70)
print(f"\nTotal Events: {len(events_data)}")
print(f"First Event Keys: {list(events_data[0].keys())}")

# Extract basic information
teams = set()
event_types = Counter()
players = set()
max_period = 0
max_minute = 0

for event in events_data:
    if 'type' in event and isinstance(event['type'], dict):
        event_types[event['type'].get('name')] += 1
    
    if 'team' in event and isinstance(event['team'], dict):
        teams.add(event['team'].get('name'))
    
    if 'player' in event and isinstance(event['player'], dict):
        players.add(event['player'].get('name'))
    
    if 'period' in event:
        max_period = max(max_period, event['period'])
    
    if 'minute' in event:
        max_minute = max(max_minute, event['minute'])

# ============================================================================
# EVENT TYPES ANALYSIS
# ============================================================================
print("\n" + "="*70)
print("EVENT TYPES ANALYSIS")
print("="*70)
print(f"\nTotal unique event types: {len(event_types)}")
print("\nTop 20 event types:")
for i, (event, count) in enumerate(event_types.most_common(20), 1):
    percentage = (count / len(events_data)) * 100
    bar = "█" * int(percentage / 2)
    print(f"  {i:2d}. {event:25s} {count:5d} ({percentage:5.1f}%) {bar}")

# ============================================================================
# TEAMS ANALYSIS
# ============================================================================
print("\n" + "="*70)
print("TEAMS ANALYSIS")
print("="*70)

team_events = defaultdict(int)
team_possession = defaultdict(int)
team_data = defaultdict(lambda: defaultdict(int))

for event in events_data:
    if 'team' in event and isinstance(event['team'], dict):
        team_name = event['team'].get('name')
        team_events[team_name] += 1
    
    if 'possession_team' in event and isinstance(event['possession_team'], dict):
        team_name = event['possession_team'].get('name')
        team_possession[team_name] += 1
    
    # Extract event type and team for metrics
    if isinstance(event.get('type'), dict) and isinstance(event.get('team'), dict):
        event_name = event['type'].get('name')
        team_name = event['team'].get('name')
        team_data[team_name][event_name] += 1

print(f"\nTeams: {', '.join(sorted(teams))}")
print(f"Match Duration: {max_minute} minutes across {int(max_period)} periods")
print(f"Total Players: {len(players)}")

for team in sorted(teams):
    total = team_events[team]
    possession = team_possession[team]
    pct = (total / len(events_data)) * 100
    poss_pct = (possession / len(events_data)) * 100
    
    print(f"\n{team}:")
    print(f"  Events: {total} ({pct:.1f}% of total)")
    print(f"  Possession Events: {possession} ({poss_pct:.1f}%)")

# ============================================================================
# TEAM PERFORMANCE METRICS
# ============================================================================
print("\n" + "="*70)
print("TEAM PERFORMANCE METRICS")
print("="*70)

metrics_to_track = [
    'Pass', 'Shot', 'Foul Committed', 'Tackle', 'Interception',
    'Clearance', 'Dribble', 'Corner Awarded', 'Aerial', 'Possession Lost',
    'Pressure', 'Dispossessed', 'Own Goal', 'Goal', 'Blocked Pass'
]

for team in sorted(teams):
    print(f"\n{team}:")
    for metric in metrics_to_track:
        count = team_data[team].get(metric, 0)
        if count > 0:
            print(f"  {metric:25s}: {count:4d}")

# ============================================================================
# TOP PLAYERS
# ============================================================================
print("\n" + "="*70)
print("TOP PLAYERS BY EVENT CONTRIBUTION")
print("="*70)

player_events = defaultdict(lambda: {'count': 0, 'team': None})

for event in events_data:
    if isinstance(event.get('player'), dict):
        player_name = event['player'].get('name')
        if player_name:
            player_events[player_name]['count'] += 1
            if event.get('team') and isinstance(event['team'], dict):
                player_events[player_name]['team'] = event['team'].get('name')

# Sort by event count
sorted_players = sorted(player_events.items(), key=lambda x: x[1]['count'], reverse=True)

print("\nTop 20 Players:")
for i, (player, data) in enumerate(sorted_players[:20], 1):
    team = data['team'] or 'Unknown'
    count = data['count']
    print(f"  {i:2d}. {player:35s} ({team:12s}) - {count:4d} events")

# ============================================================================
# MATCH TIMELINE
# ============================================================================
print("\n" + "="*70)
print("MATCH TIMELINE (Events by 5-minute intervals)")
print("="*70)

timeline = defaultdict(lambda: defaultdict(int))

for event in events_data:
    if 'minute' in event and 'team' in event and isinstance(event['team'], dict):
        interval = (event['minute'] // 5) * 5
        team = event['team'].get('name')
        timeline[interval][team] += 1

print("\n Time  | ", end="")
for team in sorted(teams):
    print(f"{team:12s} | ", end="")
print()
print("-" * (len(teams) * 17 + 10))

for interval in sorted(timeline.keys()):
    print(f"{interval:2d}-{interval+5:2d}  | ", end="")
    for team in sorted(teams):
        count = timeline[interval][team]
        print(f"{count:12d} | ", end="")
    print()

# ============================================================================
# KEY EVENT ANALYSIS
# ============================================================================
print("\n" + "="*70)
print("KEY STATISTICAL INSIGHTS")
print("="*70)

# Event type distribution by team
print("\n\nMost common events by team:")
for team in sorted(teams):
    sorted_events = sorted(team_data[team].items(), key=lambda x: x[1], reverse=True)
    print(f"\n{team} - Top 5 Events:")
    for event, count in sorted_events[:5]:
        pct = (count / team_events[team]) * 100
        print(f"  • {event:25s}: {count:4d} ({pct:.1f}% of team events)")

# Possession efficiency
print("\n\nPossession Efficiency:")
for team in sorted(teams):
    passes = team_data[team].get('Pass', 0)
    shots = team_data[team].get('Shot', 0)
    possession = team_possession[team]
    
    if possession > 0:
        pass_rate = (passes / possession) * 100
        shot_rate = (shots / possession) * 100
        print(f"\n{team}:")
        print(f"  • Pass Rate: {pass_rate:.1f}% (Passes per possession event)")
        print(f"  • Shot Rate: {shot_rate:.1f}% (Shots per possession event)")
        if passes > 0:
            print(f"  • Shot Conversion: {(shots/passes)*100:.2f}% (Shots per pass)")

# Defensive stats
print("\n\nDefensive Performance:")
for team in sorted(teams):
    tackles = team_data[team].get('Tackle', 0)
    interceptions = team_data[team].get('Interception', 0)
    fouls = team_data[team].get('Foul Committed', 0)
    clearances = team_data[team].get('Clearance', 0)
    
    print(f"\n{team}:")
    print(f"  • Tackles: {tackles}")
    print(f"  • Interceptions: {interceptions}")
    print(f"  • Fouls Committed: {fouls}")
    print(f"  • Clearances: {clearances}")
    print(f"  • Total Defensive Actions: {tackles + interceptions + clearances}")

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================
print("\n" + "="*70)
print("MATCH SUMMARY STATISTICS")
print("="*70)

summary = {
    'Total Events': len(events_data),
    'Total Teams': len(teams),
    'Total Players': len(players),
    'Match Duration': f"{max_minute} minutes",
    'Number of Periods': int(max_period),
    'Unique Event Types': len(event_types),
    'Total Passes': event_types.get('Pass', 0),
    'Total Shots': event_types.get('Shot', 0),
    'Total Fouls': event_types.get('Foul Committed', 0),
    'Total Tackles': event_types.get('Tackle', 0),
    'Total Interceptions': event_types.get('Interception', 0),
}

print("\n")
for key, value in summary.items():
    if isinstance(value, int):
        print(f"  {key:30s}: {value:6d}")
    else:
        print(f"  {key:30s}: {value}")

# ============================================================================
# SAVE ANALYSIS REPORT
# ============================================================================
print("\n" + "="*70)
print("SAVING ANALYSIS REPORT")
print("="*70)

report_file = '/home/sohamkc/something/football_analysis_report.txt'
with open(report_file, 'w') as f:
    f.write("FOOTBALL EVENT DATA ANALYSIS REPORT\n")
    f.write("="*70 + "\n\n")
    f.write(f"Analysis Date: Event Data from 15946.json\n")
    f.write(f"Total Events Analyzed: {len(events_data)}\n")
    f.write(f"Teams: {', '.join(sorted(teams))}\n")
    f.write(f"Total Players: {len(players)}\n")
    f.write(f"Match Duration: {max_minute} minutes\n\n")
    
    f.write("TOP EVENT TYPES:\n")
    for event, count in event_types.most_common(20):
        f.write(f"  {event}: {count}\n")
    
    f.write("\n\nTOP PLAYERS:\n")
    for player, data in sorted_players[:20]:
        f.write(f"  {player} ({data['team']}): {data['count']} events\n")
    
    f.write("\n\nTEAM STATISTICS:\n")
    for team in sorted(teams):
        f.write(f"\n{team}:\n")
        sorted_events = sorted(team_data[team].items(), key=lambda x: x[1], reverse=True)
        for event, count in sorted_events[:10]:
            f.write(f"  {event}: {count}\n")

print(f"✓ Report saved to {report_file}")

print("\n" + "="*70)
print("✓ ANALYSIS COMPLETE!")
print("="*70 + "\n")
