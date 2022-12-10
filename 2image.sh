printf 'Trim margins (y/n)?'
read answer
if [ $answer == 'y' ] ; then
    convert -density 300 -background white -alpha remove -trim $1 img_%02d.png
else
	convert -density 300 -background white -alpha remove $1 img_%02d.png
fi
