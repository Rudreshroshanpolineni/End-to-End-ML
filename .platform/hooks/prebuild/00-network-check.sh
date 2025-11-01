#!/bin/bash
set -e
echo "== net test ==" >> /var/log/eb-hooks.log
curl -I https://pypi.org 2>&1 | tee -a /var/log/eb-hooks.log