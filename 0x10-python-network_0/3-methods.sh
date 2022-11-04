#!/bin/bash
# displays all http methods the server will accept
curl -si -X "OPTIONS" $1 | grep "Allow" | cut -d " " -f 2-
