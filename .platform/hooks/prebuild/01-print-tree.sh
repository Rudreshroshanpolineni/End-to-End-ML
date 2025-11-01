#!/bin/bash
set -e
echo "== pwd =="  | tee -a /var/log/eb-hooks.log
pwd             | tee -a /var/log/eb-hooks.log
echo "== tree =="| tee -a /var/log/eb-hooks.log
ls -la          | tee -a /var/log/eb-hooks.log