#!/bin/sh
set -e

if [ `adb get-state` = "offline" -o `adb get-state` = "unknown" ]
then
    emulator -avd test1 &
fi
JAVA_HOME=/usr/lib/jvm/java-6-sun/ ant debug
adb wait-for-device
ant installd
adb shell am start -a android.intent.action.MAIN -n com.dvdbng.iris/com.dvdbng.iris.Iris

