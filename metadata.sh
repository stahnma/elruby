#!/bin/bash

repodata() {
    find $1 | grep debuginfo | xargs rm -f
    find $1 | grep repodata | xargs rm -rf
    for dir in `find $1 -type d | egrep 'i386|x86|SRPMS'`
    do
        echo $dir
        pushd $dir
        createrepo -d .
        popd
    done
}

repodata  ruby-1.9.3
