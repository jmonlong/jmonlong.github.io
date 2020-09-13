This repo contains the content of my personal page hosted at https://jmonlong.github.io/.
It's a [blogdown](https://bookdown.org/yihui/blogdown/) website so it can be built using:

```
Rscript -e "blogdown::build_site()"
```

I write my CV in latex, see the [misc](misc) folder which contains the BibTeX library with my publications and the LaTeX document and style.
Note: the BibTeX file is also used for the ["Selected  Publications" section](content/home/publications.Rmd) of the website (using the [RefManageR package](https://cran.r-project.org/web/packages/RefManageR/index.html))
