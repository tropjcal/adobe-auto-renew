# adobe-auto-renew
Very simple script to renew the trial serial number of an Adobe product.

NOTE: Highly recommend backing up the target application.xml file before you run the script so you can easily restore if things go nutty.

Written mostly as a small challenge and probably will be painful for any experienced programmers to look at (sorry). Written to change the trial number of InDesign 2021, but can easily be rewritten to modify any Adobe program's application.xml file. 

To allow the script to write the changes to the file, you'll need to enable modify permissions on the application.xml file.
To make the script run automatically, use Task Scheduler or add the script to the startup folder.
