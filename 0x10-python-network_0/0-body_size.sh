#!/bin/bash
# displays the size of the body of the response in bytes
curl -i $1 | grep Content-Length | tail -c 4
