serve: static/MonlongJeanCV.pdf
	Rscript -e "blogdown::build_site()"
	Rscript -e "blogdown::serve_site()"

rebuild: static/MonlongJeanCV.pdf
	Rscript -e "blogdown::build_site(build_rmd=TRUE)"

static/MonlongJeanCV.pdf: misc/MonlongJeanCV.pdf
	cp $< $@
