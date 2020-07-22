#!/bin/sh

if [ $JAVA_HOME ]; then
    if [ -f $JAVA_HOME/bin/java ]; then
        JAVA=$JAVA_HOME/bin/java         
    fi
fi

if [ $JRE_HOME ]; then
    if [ -f $JRE_HOME/bin/java ]; then 
        JAVA=$JRE_HOME/bin/java
    fi
fi

if [ -z $JAVA ]; then
    echo "No java installed. please install JRE/JDK in this system."
    exit;
fi

echo "Starting ACS_Server ... "

PWD=$(dirname $0)

if [ "$PWD"x = "."x ]; then
    PWD=$(pwd)
fi

cd $PWD

#$JAVA -Xms128M -Xmx1024M -cp .:../lib/acs_server.jar:../lib/log4j-1.2.9.jar:../lib/classes12.jar:../lib/xsu12.jar:../lib/servlet-api.jar:../lib/bcprov-jdk16-146.jar:../lib/commons-lang-2.3.jar:../lib/commons-httpclient-3.0.jar:../lib/dom4j-1.5.2.jar:../lib/jaxen-1.1-beta-9.jar:../lib/commons-codec-1.3.jar:../lib/commons-logging-1.0.4.jar:../lib/json-lib-2.2-jdk15.jar:../lib/jce.jar:../lib/ezmorph-1.0.5.jar:../lib/commons-collections-3.2.1.jar:../lib/commons-beanutils.jar:../lib/ifc.jar:../lib/cxf-2.7.8.jar:../lib/neethi-3.0.2.jar:../lib/stax2-api-3.1.1.jar:../lib/woodstox-core-asl-4.2.0.jar:../lib/wsdl4j-1.6.3.jar:../lib/xmlschema-core-2.0.3.jar com.interlib.ACS.ACS_Server 

/usr/sbin/daemonize -p $PWD/acs.pid $JAVA -Xms128M -Xmx1024M -cp $PWD:$PWD/../lib/acs_server.jar:$PWD/../lib/log4j-1.2.9.jar:$PWD/../lib/classes12.jar:$PWD/../lib/xsu12.jar:$PWD/../lib/servlet-api.jar:$PWD/../lib/bcprov-jdk16-146.jar:$PWD/../lib/commons-lang-2.3.jar:$PWD/../lib/commons-httpclient-3.0.jar:$PWD/../lib/dom4j-1.5.2.jar:$PWD/../lib/jaxen-1.1-beta-9.jar:$PWD/../lib/commons-codec-1.3.jar:$PWD/../lib/commons-logging-1.0.4.jar:$PWD/../lib/json-lib-2.2-jdk15.jar:$PWD/../lib/jce.jar:$PWD/../lib/ezmorph-1.0.5.jar:$PWD/../lib/commons-collections-3.2.1.jar:$PWD/../lib/commons-beanutils.jar:$PWD/../lib/ifc.jar:$PWD/../lib/cxf-2.7.8.jar:$PWD/../lib/neethi-3.0.2.jar:$PWD/../lib/stax2-api-3.1.1.jar:$PWD/../lib/woodstox-core-asl-4.2.0.jar:$PWD/../lib/wsdl4j-1.6.3.jar:$PWD/../lib/xmlschema-core-2.0.3.jar com.interlib.ACS.ACS_Server
 

