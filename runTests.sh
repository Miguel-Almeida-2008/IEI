#!/bin/sh
REPORT_PATH="/app/lintingReports.txt"

sh /app/scripts/ruff.sh > ${REPORT_PATH} 2>&1
echo "Report saved to: ${REPORT_PATH}"

