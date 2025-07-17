#!/usr/bin/env python3
"""
Update ari-validator.rst with dashboard content
"""

import re
import os

def update_documentation():
    """Update the ari-validator.rst file with dashboard content"""
    
    # File paths
    rst_file = 'docs/source/processing_pipelines/ari-validator.rst'
    dashboard_file = 'dashboard_content.rst'
    
    # Check if files exist
    if not os.path.exists(rst_file):
        print(f"Error: {rst_file} not found")
        return 1
    
    if not os.path.exists(dashboard_file):
        print(f"Error: {dashboard_file} not found")
        return 1
    
    # Read the original file
    with open(rst_file, 'r') as f:
        content = f.read()
    
    # Read the dashboard content
    with open(dashboard_file, 'r') as f:
        dashboard = f.read()
    
    # Replace the dashboard section
    # Look for the existing dashboard section and replace it completely
    pattern = r'Data Validation Dashboard\s*-------------------------.*?(?=\n\n[A-Z]|\nTroubleshooting|\Z)'
    
    if re.search(pattern, content, re.DOTALL):
        # Replace existing dashboard section
        updated_content = re.sub(pattern, dashboard.strip(), content, flags=re.DOTALL)
        print("Updated existing dashboard section")
    else:
        # If no dashboard section found, add before 'Troubleshooting'
        pattern = r'(\nTroubleshooting\s*[-=]+)'
        if re.search(pattern, content):
            updated_content = re.sub(pattern, f'\n{dashboard.strip()}\\1', content, flags=re.DOTALL)
            print("Added new dashboard section before Troubleshooting")
        else:
            # If no Troubleshooting section, add at the end
            updated_content = content + '\n\n' + dashboard.strip()
            print("Added dashboard section at the end")
    
    # Write the updated content
    with open(rst_file, 'w') as f:
        f.write(updated_content)
    
    print(f"Successfully updated {rst_file}")
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(update_documentation())