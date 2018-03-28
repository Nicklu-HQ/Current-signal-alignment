
Here we show some current signal data from MinION with “CCS” model and give some ideals

Fig1, show the current signal data from one fast5 file. There are 84806 current points and 15747nt (about 6:1). The insert target sequence about 100nt, so there are about 80 duplicate subreads. The adaptor sequence (TATATATATATAT……) signal is very clear.


With the same nanopore, the same motor protein, the same DNA sequence, the MinION emit a little different current signal. Alignment these current signal lead us to explore the more details about the deletions, insertions and mismatch. 


Fig2, show the current signal of three subreads (two on the start side, another on the end side) and alignment.


The original data and tools (python) are loaded. 

It seems that:
1.	The subreads are almost similar from start to end on the same read, so the hardware MinION is stable.
2.	The difference between the subreads signal are random, and most probably cause by the motor protein.
3.	The tandem sequence (even theduplicate subread is very short) can be record well by the MinION.
4.	Chimeras is obviously not a big problem on the amplification 
5.	An algorithm making full use of these signal will produce a very high accuracy final read just like CCS from Pacbio.



Unfortunately, we haven’t the reference sequence about the demo data, because it’s an unexpected product from PCR.  But it has a short repeat sequence (easy to calculator) and many duplicate subreads.
We load some other fast5 files with a reference sequence, if you have an interest in the algorithm, you’re welcome to try these, and we are pleasure to know you meet the target of 100% accuracy.

