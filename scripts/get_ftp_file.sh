#! /bin/bash

platform=$1
target=$2
build_type=$3
build_num=$4
ftp_address="192.168.1.102"

function Usage {
    echo "Usage:    ./get_ftp_target.sh <platform> <target> [<build_type>] [<build_num>]"
    echo "option:"
    echo "    <platfrom> is Android or iOS"
    echo "    <target> is ccc, dev, and etc."
    echo "    <build_num> is build number of Jenkins job"
    echo "    <build_type> is debug or release. This is a option value and default value is release"
    exit 1
}

if [ -z "$platform" ]
then
    echo "<platform> is not given"
    Usage
fi

if [ -z "$target" ]
then
    echo "<target> is not given"
    Usage
fi

platform="$(echo $platform | tr '[A-Z]' '[a-z]')"

if [ "$platform" == "android" ]
then
    filename="app-$target-$build_type.apk"
elif [ "$platform" == "ios" ]
then
    filename="PicoworkPortal.app.zip"
else
    echo "Not support platform type: $platform"
    exit 1
fi

if [ -z "$build_type" ]
then
    echo "<build_type> is not given. use default value"
    build_type="release"
fi

if [ -z "$build_num" ]
then
    echo "<build_num> is not given. use latest number"

    build_num="$(ftp ftp://builder:picowork@$ftp_address << END_SCRIPT
    cd build/
    cd $platform/
    more latest
    quit
    END_SCRIPT)"
fi

echo "get ftp file with args: $platform, $target, $build_type, $build_num, $filename"

ftp ftp://builder:picowork@$ftp_address << END_SCRIPT
cd build/
cd $platform/
cd $build_num/
get $filename
quit
END_SCRIPT
