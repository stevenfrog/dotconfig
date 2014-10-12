#!/bin/sh

TOMCAT_WEBAPP_PATH=./webapps/wdt
CODE_PATH=/home/stevenfrog/TC_Assembly_2014/Workday_Data_Toolkit_Schema_and_Workbook_Frontend/wdt/src/main/webapp

cp -f $TOMCAT_WEBAPP_PATH/js/script.js $CODE_PATH/js/
cp -f $TOMCAT_WEBAPP_PATH/jsp/*.jsp       $CODE_PATH/js/

echo "Write back to dev code completely!"