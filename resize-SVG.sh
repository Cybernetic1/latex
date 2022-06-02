# inkscape --batch-process --actions="select-all:all;FitCanvasToSelection;FileSave;FileClose;" $1
inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose --verb=FileQuit $1
# ***** inkscape --verb-list | grep "File"
