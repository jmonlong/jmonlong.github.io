serve: static/MonlongJeanCV.pdf
	Rscript -e "blogdown::build_site()"
	Rscript -e "blogdown::serve_site()"

static/MonlongJeanCV.pdf: misc/MonlongJeanCV.pdf
	cp $< $@
