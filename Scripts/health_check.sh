#!/bin/bash

STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000)

if [ "$STATUS" -eq 200 ]; then
	echo "$(date) -InfraPulse is healthy" >> logs/health.log
else
	echo "$(date) -InfraPulse is DOWN" >> logs/health.log
fi


