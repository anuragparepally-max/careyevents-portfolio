#!/usr/bin/env python3
import re

# Read the index.html file
with open('/Users/aparepally/careyevents-portfolio/index.html', 'r') as f:
    content = f.read()

# Define updates for each event
# Format: event_url: (vehicles, people, fleet_type)
event_updates = {
    'madonna-european-tour': {
        'vehicles': '700',
        'people': '2,300',
        'fleet': 'SUV, Sprinter Van, Mini Bus',
        'has_stats': True
    },
    'kylie-minogue-european-tour': {
        'vehicles': '600',
        'people': '1,900',
        'fleet': 'SUV, Sprinter Van, Mini Bus',
        'has_stats': True
    },
    'foo-fighters-european-tour': {
        'vehicles': '500',
        'people': '1,800',
        'fleet': 'SUV, Sprinter Van, Mini Bus',
        'has_stats': True
    },
    'global-citizens-concert': {
        'vehicles': '300',
        'people': '2,000',
        'fleet': 'Executive SUV, Sprinter Van',
        'has_stats': False
    },
    'super-bowl': {
        'vehicles': '1,200',
        'people': '5,000',
        'fleet': 'Executive SUV, Sedan, Sprinter Van',
        'has_stats': True,
        'keep_role': True
    },
    'nba-all-stars': {
        'vehicles': '500',
        'people': '3,000',
        'fleet': 'Executive SUV, Sedan',
        'has_stats': True
    },
    'nfl-honors': {
        'vehicles': '350',
        'people': '1,500',
        'fleet': 'Executive SUV, Sedan',
        'has_stats': False
    },
    'pga-golf': {
        'vehicles': '250',
        'people': '1,200',
        'fleet': 'Executive SUV, Sedan',
        'has_stats': False
    },
    'louis-vuitton-miami': {
        'vehicles': '400',
        'people': '1,000',
        'fleet': 'Executive SUV, Luxury Sedan',
        'has_stats': True,
        'replace_stats': True
    },
    'louis-vuitton-cruise': {
        'vehicles': '300',
        'people': '800',
        'fleet': 'Executive SUV, Luxury Sedan',
        'has_stats': False
    },
    'gucci-new-york': {
        'vehicles': '200',
        'people': '600',
        'fleet': 'Executive SUV, Luxury Sedan',
        'has_stats': False
    },
    'bcg-summit': {
        'vehicles': '150',
        'people': '500',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': True,
        'replace_stats': True
    },
    'vanguard-conference': {
        'vehicles': '150',
        'people': '500',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': True,
        'add_people': True
    },
    'blackrock-summit': {
        'vehicles': '150',
        'people': '500',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': True,
        'add_people': True
    },
    'jpmorgan-healthcare': {
        'vehicles': '200',
        'people': '800',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': True,
        'add_people': True
    },
    'nvidia-conference': {
        'vehicles': '200',
        'people': '1,500',
        'fleet': 'Executive Sedan, SUV, Shuttle Bus',
        'has_stats': True,
        'replace_stats': True
    },
    'oracle-openworld': {
        'vehicles': '250',
        'people': '2,000',
        'fleet': 'Executive Sedan, SUV, Shuttle Bus',
        'has_stats': True,
        'replace_stats': True
    },
    'ibm-think': {
        'vehicles': '200',
        'people': '1,500',
        'fleet': 'Executive Sedan, SUV, Shuttle Bus',
        'has_stats': True,
        'replace_stats': True
    },
    'nbc-events': {
        'vehicles': '150',
        'people': '800',
        'fleet': 'Executive SUV, Sedan',
        'has_stats': True,
        'replace_stats': True
    },
    'toshiba-corporate': {
        'vehicles': '120',
        'people': '600',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': True,
        'replace_stats': True
    },
    'abbott-conference': {
        'vehicles': '180',
        'people': '600',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': False
    },
    'cigna-summit': {
        'vehicles': '150',
        'people': '500',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': False
    },
    'boston-scientific': {
        'vehicles': '200',
        'people': '600',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': False
    },
    'eli-lilly-summit': {
        'vehicles': '180',
        'people': '550',
        'fleet': 'Executive Sedan, SUV',
        'has_stats': False
    },
}

# Process each event
for event_url, data in event_updates.items():
    # Find the event card
    pattern = rf'(<a href="events/{event_url}\.html".*?</a>)'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        print(f"Could not find event: {event_url}")
        continue

    event_block = match.group(1)
    updated_block = event_block

    # Add fleet section if just has event-fleet with generic text
    if not data.get('has_stats', False):
        # Replace the event-fleet section with stats + fleet
        fleet_pattern = r'(<div class="event-fleet">.*?</div>)'
        stats_and_fleet = f'''<div class="event-stats">
                        <div class="stat">
                            <span class="stat-number">{data['vehicles']}</span>
                            <span class="stat-label">Vehicles</span>
                        </div>
                        <div class="stat">
                            <span class="stat-number">{data['people']}</span>
                            <span class="stat-label">People Served</span>
                        </div>
                    </div>
                    <div class="event-fleet">
                        <strong>Fleet:</strong> {data['fleet']}
                    </div>'''
        updated_block = re.sub(fleet_pattern, stats_and_fleet, updated_block, flags=re.DOTALL)

    # For events that have stats but need fleet added
    elif data.get('has_stats') and not data.get('replace_stats') and not data.get('add_people') and not data.get('keep_role'):
        # Add fleet after stats
        stats_pattern = r'(</div>\s*</div>)(\s*<span class="view-details")'
        fleet_section = f'''\\1
                    <div class="event-fleet">
                        <strong>Fleet:</strong> {data['fleet']}
                    </div>\\2'''
        updated_block = re.sub(stats_pattern, fleet_section, updated_block)

    # For events that need stats replaced
    elif data.get('replace_stats'):
        # Replace entire stats section and add/update fleet
        stats_pattern = r'<div class="event-stats">.*?</div>\s*</div>'
        new_stats = f'''<div class="event-stats">
                        <div class="stat">
                            <span class="stat-number">{data['vehicles']}</span>
                            <span class="stat-label">Vehicles</span>
                        </div>
                        <div class="stat">
                            <span class="stat-number">{data['people']}</span>
                            <span class="stat-label">People Served</span>
                        </div>
                    </div>'''
        updated_block = re.sub(stats_pattern, new_stats, updated_block, flags=re.DOTALL)

        # Check if fleet exists, if not add it
        if '<strong>Fleet:</strong>' not in updated_block:
            stats_end_pattern = r'(</div>\s*</div>)(\s*<span class="view-details")'
            fleet_section = f'''\\1
                    <div class="event-fleet">
                        <strong>Fleet:</strong> {data['fleet']}
                    </div>\\2'''
            updated_block = re.sub(stats_end_pattern, fleet_section, updated_block)

    # For events that need people added to existing stats
    elif data.get('add_people'):
        # Add second stat for people
        stats_pattern = r'(</div>\s*</div>)(\s*</div>)(\s*<span class="view-details")'
        people_stat = f'''\\1
                        <div class="stat">
                            <span class="stat-number">{data['people']}</span>
                            <span class="stat-label">People Served</span>
                        </div>\\2
                    <div class="event-fleet">
                        <strong>Fleet:</strong> {data['fleet']}
                    </div>\\3'''
        updated_block = re.sub(stats_pattern, people_stat, updated_block)

    # For Super Bowl - keep role and add fleet
    elif data.get('keep_role'):
        # Add fleet after the role section
        role_pattern = r'(<div class="event-fleet">\s*<strong>Role:</strong>.*?</div>)'
        fleet_section = f'''\\1
                    <div class="event-fleet">
                        <strong>Fleet:</strong> {data['fleet']}
                    </div>'''
        updated_block = re.sub(role_pattern, fleet_section, updated_block, flags=re.DOTALL)

    # Replace in content
    content = content.replace(event_block, updated_block)
    print(f"Updated: {event_url}")

# Write the updated content
with open('/Users/aparepally/careyevents-portfolio/index.html', 'w') as f:
    f.write(content)

print("\nAll events updated successfully!")
