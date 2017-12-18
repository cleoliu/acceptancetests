#! /bin/bash


target=$1
test_ios=$2
test_android=$3
test_web=$4

# working directory is project root
rm -rf log test_*.xml *.app *.apk *.zip testcases/test_metadata.json
mkdir -p log
appium -p 4723 &> ./log/appium.log &

if [ "$test_ios" == "true" ]
then
    # ios-sim start --devicetypeid "iPhone-7, 11.0" --exit
    ./scripts/get_ftp_file.sh iOS $target release
    unzip ./PicoworkPortal.app.zip > /dev/null
    ./generate_tested_devices.py iOS -n com.picowork.$target -p ./PicoworkPortal.app -d EFFFD0F8-6907-41DF-B3A0-B0D9DC08A5D2 -t $target
fi

if [ "$test_android" == "true" ]
then
    # ~/Library/Android/sdk/tools/emulator -avd Nexus_5X_API_26 &> /dev/null &
    ./scripts/get_ftp_file.sh Android $target release
    ./generate_tested_devices.py Android -n com.picowork.$target.app -p ./app-$target-release.apk -d emulator-5554 -t $target
fi

if [ "$test_web" == "true" ]
then
    ./generate_tested_devices.py web --url "http://$target.picowork.com" -d chrome -t $target
fi

sleep 10 # wait emulator start completely

./testcases/test_runner.py
echo "Test done ret code is $?"
merge_result.py ./*.xml > test_result.xml
