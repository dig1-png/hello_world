#!/bin/sh
echo This is a multiple thread process shell file!
#echo run thread1.py
#python thread1.py
#echo finished

#echo run thread2.py
#python thread2.py
#echo finished all threads

echo to run some threads in the same time!
python dev/thread1.py & python thread2.py
