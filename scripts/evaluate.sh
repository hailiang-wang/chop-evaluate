#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
# functions
trim() {
    local var="$*"
    # remove leading whitespace characters
    var="${var#"${var%%[![:space:]]*}"}"
    # remove trailing whitespace characters
    var="${var%"${var##*[![:space:]]}"}"   
    echo -n "$var"
}

function segment(){
    echo "seg: $1"
}

function batch_process(){
    ## import data
    processor=$1
    corpus=$2
    output=$3

    if [ -f $output ]; then
        rm $output
    fi

    IFS=$'\n'
    file=`cat $corpus`
    for x in $file; do
        x=`trim $x`
        if [ ! -z $x ]; then
            echo "$processor processing $corpus: " $x
            $processor $x >> $output
        fi
    done
    echo "saved to $output"
    echo "done."
}

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..
source ~/venv-py3/bin/activate
batch_process segment icwb2-data/testing/pku_test.utf8 result/chop.pku_test.utf8

