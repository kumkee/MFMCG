#!/bin/bash
/usr/bin/rsync -av --rsh=ssh $HOME/workspace/MFMCG/data/ sunrock:/var/tmp/mfmcg/data/
/usr/bin/rsync -av --rsh=ssh $HOME/workspace/MFMCG/log/ sunrock:/var/tmp/mfmcg/log/
