#!/bin/bash

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title block_x
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.description Blocks internet access to X.
# @raycast.author Max Hager
# @raycast.authorURL https://twitter.com/MaxHager66

# Path to the hosts file
HOSTS_PATH="/etc/hosts"

# IP address to redirect the domains to
REDIRECT_IP="127.0.0.1"

# Domains to block
DOMAINS=("twitter.com" "www.twitter.com" "x.com" "www.x.com")

# Function to block Twitter
block_twitter() {
    for DOMAIN in "${DOMAINS[@]}"; do
        if ! grep -q "$REDIRECT_IP $DOMAIN" "$HOSTS_PATH"; then
            echo "$REDIRECT_IP $DOMAIN" | sudo /usr/bin/tee -a "$HOSTS_PATH" > /dev/null
        fi
    done
}

# Call the function
block_twitter