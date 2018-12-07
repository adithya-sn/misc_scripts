#!/bin/sh

build_status=$(curl -su "$jenkins_cred" "$BUILD_URL"/api/xml | grep result | sed 's/^.*<result>//' | sed 's/<\/result>.*$//')
echo Build-status="$build_status"

curl -X POST --data-urlencode "payload={\"channel\": \"#channel_name\", \"username\": \"Slack_user\", \"text\": \"$JOB_BASE_NAME build - $BUILD_DISPLAY_NAME\nBuild status = "$build_status"\", \"icon_emoji\": \":smile:\"}" https://hooks.slack.com/services/$SLACK_TOKEN