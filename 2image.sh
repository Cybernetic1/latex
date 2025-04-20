printf 'The old command was:\n'
printf '    convert -density 300 -background white -alpha remove $1 img_%02d.png\n'

printf '\nNow using new command:\n'
printf '     pdftoppm -png FILE.pdf -f 1 -l 10 img\n'
printf 'where -f -l are first and last pages, img is output file prefix\n\n'

printf 'first page =?'
read firstpage
printf 'last page =?'
read lastpage
pdftoppm -png $1 -f $firstpage -l $lastpage img

# printf 'Trim margins (y/n)?'
# read answer
# if [ $answer == 'y' ] ; then
#    convert -density 300 -background white -alpha remove -trim $1 img_%02d.png
# else
#	convert -density 300 -background white -alpha remove $1 img_%02d.png
# fi
