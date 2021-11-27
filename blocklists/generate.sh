#!/bin/bash
rm hosts
touch hosts
BASEURL="https://raw.githubusercontent.com/jmdugan/blocklists/master/corporations/"

declare -a corporations=("apple" "amazon" "pinterest")
for corporation in "${corporations[@]}"
do
	curl -sS "$BASEURL$corporation/all" >> hosts
done

curl -sS "$BASEURL/facebook/all-but-whatsapp" >> hosts
