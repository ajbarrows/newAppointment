# newAppointment
Python script to quickly create a file structure for each UVM Graduate Writing Center consulting appointment.

## Usage

Clone this repository to the location where you would like to save your GWC work (either clone or download and unpack this repository).


Open a Terminal window from the From a unix-like terminal (tested on macOS Ventura: Right Click on the folder --> Services --> New Terminal at Folder):

```
$ tony@Tonys-MacBook-Pro 00_newAppointment % 
$ tony@Tonys-MacBook-Pro 00_newAppointment % python3 newAppointment.py

```
You will see a user-input dialog:

```
Enter client's UVM NetID:

```

Enter the netID and press return. The script will create the following structure in __the parent directory.__

```
netID
└── yyyy-mm-dd_netID
    ├── yyyy-mm-dd_netID_crf.docx
    ├── download
    └── edit
```

`download` is for storing clean copies of files clients provide. `edit` is for those files with the consultant's edits. 

Additional appointments (i.e., on other days) with the same client will not overwrite previous appointments.