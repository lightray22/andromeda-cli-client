## Overview

This script is a simple wrapper that emulates using the command-line Andromeda server API, but over a remote HTTP connection.
This allows making remote API calls manually without a local console available.

#### Differences

Any features that rely on the higher privileges of the real CLI interface are not available. Examples:
* Changing the database configuration file
* PHP printr format (JSON only)
* Changing debug/metrics output
* Doing a request dryrun

The general usage is the same as the real CLI interface, with an added URL.  
Parameter syntax, attaching/uploading files and using environment variables is the same.

#### Quick Example

Run the script with no arguments to show basic usage.  
Run ```./a2cli.py server usage``` to show the list of API calls.

## Prerequisites

Requires python3 and python3-requests.