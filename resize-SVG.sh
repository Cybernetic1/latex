INK_VERSION="$(inkscape --version)"
echo ${INK_VERSION}
if [[ "$INK_VERSION" == "Inkscape 1.1"* ]]; then
	echo "GUI seems required for this version... trying..."
	inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose --verb=FileQuit $1
fi

if [[ "$INK_VERSION" == "Inkscape 1.3"* ]]; then
	inkscape --actions="select-all:all;fit-canvas-to-selection;export-overwrite;export-do" $1
fi

# ***** inkscape --action-list | grep "File"
# ***** OLD: inkscape --verb-list | grep "File"
