if WScript.Arguments.Count = 0 then
    msgbox("no arguments")
else

    ' bring in the initial arguments
    dim source_dir
    dim export_dir
    source_dir = Replace(WScript.Arguments(0), "%", " ")
    export_dir = Replace(WScript.Arguments(1), "%", " ")

    ' initialize the file system object library
    dim fso
    set fso = CreateObject("Scripting.FileSystemObject")

    ' initialize the pc-dmis application
    dim pc_dmis
    set pc_dmis = CreateObject("PCDLRN.Application")
    pc_dmis.visible = False

    ' iterate through all the subfolders in the source directory
    dim file_name
    dim part
    dim i
    i = 0
    for each folder in fso.GetFolder(source_dir).SubFolders

        ' iterate through the measurement routine file(s) in the current subfolder
        for each file in fso.GetFolder(folder.Path).Files
            if LCase(file.type) = "pc-dmis measurement routine file" then
                file_name = LCase(fso.buildpath(export_dir, Split(file.name, ".")(0) + ".xml"))
                WScript.Echo file_name
                set part = pc_dmis.partprograms.open(file.path, "Offline")
                part.exporttoxml(fso.buildpath(export_dir, file_name + ".xml"))
                part.close
            end if
        next
        i = 1
    next

    ' close the pc-dmis instance
    pc_dmis.quit

    ' signal the all clear
    msgbox("Script completed")

end if