#!/bin/bash

for i in {1..2450}
do
	#bsub -q 1nh < submitJobSexaqProd.sh -a $i
	#bsub -q 8nh < shell/$i.sh
	echo 'submitting job '$i''
	chmod u+x shell_with_antiS_eta_cut/$i.sh
	qsub shell_with_antiS_eta_cut/$i.sh
	if [ $(( $i  % 1000 )) -eq 0 ];
	then
		echo 'now going to sleep a bit'
		sleep .75h
	fi
done
